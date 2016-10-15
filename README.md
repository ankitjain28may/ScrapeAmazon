# ScrapeAmazon
>Scrape the Users Review from Amazon supports python3

#Installation
1- Install python 3.5 from `www.python.org`

2- `sudo apt-get install python3-pip` (For Ubuntu Users)

3- `python setup.py`

  This will install all these packages

  * `pip install bs4`

  * `pip install requests`

  * `pip install urllib`

  * `pip install validators`

After the installation, open terminal at the root folder--

Run `python run.py` or `python3 run.py` to get individual reviews at the terminal screen.

OR

Run `python automatedScrape.py` or `python3 automatedScrape.py` to save all the reviews of all the items for the searched product in the file.

##Some Useful Installation Tips

If you have already installed python 2.7 install python 3 as well but it may be the problem that the packages installed with respect to python 2.7 and shows error for the python 3 packages,

So you need to install virtual Environment for the python 3 to install python3 packages.

```
	virtualenv -p /usr/bin/python3 py3env
	source py3env/bin/activate
	pip install package-name
```

After setting virtual environment install packages listed above and Enjoy.

#License

Copyright (c) 2016 Ankit Jain - Released under the Apache License