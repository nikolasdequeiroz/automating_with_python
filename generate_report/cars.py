#!/usr/bin/env python3

import json
import locale
import sys
import reports
import os
import emails


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    max_revenue = {"revenue": 0}
    max_sales = {"total_sales": 0}
    most_popular = {}
    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item
        # TODO: also handle max sales
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item
        # TODO: also handle most popular car_year
        if item['car']['car_year'] not in most_popular:
            most_popular[item['car']['car_year']] = 0
        most_popular[item['car']['car_year']] += 1

    # Getting the most popular year sorting the dictionary and picking the first key after sorting based on value
    most_popular_year = sorted(most_popular.items(), key=lambda x: x[1], reverse=True)[0][0]

    # Iterating through the dictionary again to get the total sales for the most popular year, summing the values.
    total_year_sales = 0
    for item in data:
        if item['car']['car_year'] == most_popular_year:
            total_year_sales += item['total_sales']

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(
            most_popular_year, total_year_sales)

    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    info = process_data(data)
    summary = '<br/>'.join(info)
    body = "\n".join(info)
    # TODO: turn this into a PDF report
    reports.generate("/tmp/cars.pdf", "Car Sales Report", summary, cars_dict_to_table(data))
    # TODO: send the PDF report as an email attachment
    content = emails.generate('automation@example.com', 'student@example.com',
                              "Sales summary for last month", body, "/tmp/cars.pdf")
    emails.send(content)

if __name__ == "__main__":
    main(sys.argv)
