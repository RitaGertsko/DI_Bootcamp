from app import my_app
from flask import render_template, redirect, url_for
from app.forms import AddForm

cities_list = []


@my_app.route('/', methods=["GET"])
def home():
    return render_template("index.html", title="Home", cities=cities_list)


@my_app.route('/my_cities', methods=["GET"])
def my_cities():
    return render_template("my_cities.html", title="My Cities List", cities_list=cities_list)


@my_app.route('/add_city', methods=["GET", "POST"])
def add_city():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        country = form.country.data
        residents = form.residents.data
        area = form.area.data
        latitude = form.latitude.data
        longitude = form.longitude.data

        city_info = {
            "cityName": name,
            "cityCountry": country,
            "residents": residents,
            "cityArea": area,
            "cityLatitude": latitude,
            "cityLongitude": longitude,
        }

        cities_list.append(city_info)
        return redirect(url_for('my_cities'))

    return render_template("add_city.html", form=form, title="Add City")


@my_app.route('/delete/<cityName>', methods=["GET", "POST", "DELETE"])
def delete_city_from_cities_list(cityName):
    for i in range(len(cities_list)):
        if cities_list[i]['cityName'] == cityName:
            del cities_list[i]
    return redirect(url_for("my_cities"))
