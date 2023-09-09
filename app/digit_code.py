from flask import Flask, jsonify
import pycountry
import phonenumbers

app = Flask(__name__)

def generate_country_data():
    COUNTRY_DATA = {}

    for country in pycountry.countries:
        country_code = country.alpha_2

        country_data = {'code': country_code, 'calling_code': ''}

        if hasattr(country, 'calling_codes'):
            calling_codes = country.calling_codes
            if calling_codes:
                country_data['calling_code'] = calling_codes[0]
        else:
            try:
                country_data['calling_code'] = phonenumbers.country_code_for_region(country_code)
            except phonenumbers.phonenumberutil.Error:
                pass

        COUNTRY_DATA[country_code] = country_data

    # Alphabetical sorting of the dictionary
    sorted_countries = sorted(COUNTRY_DATA.items(), key=lambda x: x[1]['code'])

    return sorted_countries

@app.route('/countries', methods=['GET'])
def get_countries():
    sorted_countries = generate_country_data()
    return jsonify(sorted_countries)

