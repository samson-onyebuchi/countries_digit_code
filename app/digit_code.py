from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for country dialing codes
country_phone_codes = {
    "United States": "+1",
    "Canada": "+1",
    "United Kingdom": "+44",
    "Australia": "+61",
    "India": "+91",
    "China": "+86",
    "Germany": "+49",
    "France": "+33",
    "Japan": "+81",
    "Brazil": "+55",
    "Russia": "+7",
    "South Africa": "+27",
    "Mexico": "+52",
    "Argentina": "+54",
    "Spain": "+34",
    "Italy": "+39",
    "Netherlands": "+31",
    "Sweden": "+46",
    "Norway": "+47",
    "Switzerland": "+41",
    "Singapore": "+65",
    "Malaysia": "+60",
    "New Zealand": "+64",
    "Saudi Arabia": "+966",
    "United Arab Emirates": "+971",
    "South Korea": "+82",
    "Egypt": "+20",
    "Turkey": "+90",
    "Greece": "+30",
    "Thailand": "+66",
    "Philippines": "+63",
    "Indonesia": "+62",
    "Vietnam": "+84",
    "Pakistan": "+92",
    "Bangladesh": "+880",
    "Sri Lanka": "+94",
    "Nepal": "+977",
    "Afghanistan": "+93",
    "Iraq": "+964",
    "Iran": "+98",
    "Kenya": "+254",
    "Nigeria": "+234",
    "Ghana": "+233",
    "Morocco": "+212",
    "Tunisia": "+216",
    "Algeria": "+213",
    "Chile": "+56",
    "Peru": "+51",
    "Colombia": "+57",
    "Venezuela": "+58",
    "Ecuador": "+593",
    "Bolivia": "+591",
    "Paraguay": "+595",
    "Uruguay": "+598",
    # Add more countries as needed
}


@app.route('/country-codes', methods=['GET'])
def get_country_codes():
    return jsonify(country_phone_codes)


