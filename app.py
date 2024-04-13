import flask
from utils.database_helper import get_data_from_sqlite3

app = flask.Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('index.html')

@app.route('/country_mock')
def get_data_mock():
    """ Return data for the country chart
    """
    
    return flask.jsonify({
        "Country": ["USA", "China", "India", "Brazil", "Russia", "Japan", "Germany", "UK", "France", "Italy"],
        "Value": [20, 15, 10, 5, 5, 5, 5, 5, 5, 5]
    })

@app.route('/country_db')
def get_data_mock_db():
    """ Return data from the mock database"""
    data = get_data_from_sqlite3()
    # modify data into JSON for d3
    data_json = {
        "Country": [row[0] for row in data],
        "Value": [row[1] for row in data]
    }

    return flask.jsonify(data_json)

if __name__ == "__main__":
    app.run(host='localhost', debug=True)