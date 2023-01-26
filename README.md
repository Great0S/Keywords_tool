keyword-tool
============

A python script that uses the [SerpApi](https://serpapi.com/) API to search for keywords using user input, and then saves the results to a CSV file.

Dependencies
------------

* Python 3.7x - 3.11
* [SerpApi](https://serpapi.com/) API key (can be obtained by signing up for a free account)
* [requests](https://pypi.org/project/requests/) library
* [pandas](https://pandas.pydata.org/) library

Usage
-----

1. Clone or download the repository to your local machine.
2. Install the dependencies by running `pip install -r requirements.txt` in the terminal.
3. Replace `api_key` in the script with your SerpApi API key.
4. Run the script by executing `python keyword_research.py`.
5. Enter the keyword you want to search for when prompted.
6. The script will use the SerpApi API to search for the keyword and save the results to a CSV file named `keyword_results.csv` in the same directory as the script.

Notes
-----

* The script currently only supports searching for one keyword at a time.
* The SerpApi API returns a limited number of results per search, so the script may not return all possible results for a given keyword.
* The CSV file will be overwritten each time the script is run with a new keyword search.

Contribute
----------

* If you want to contribute to the script, please feel free to fork the repository and create a pull request with your changes.
* You can also submit any issues you encounter with the script or suggestions for improvements.

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
