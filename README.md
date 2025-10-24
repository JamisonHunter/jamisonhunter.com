# jamisonhunter.com

## Run locally

If you wanted to run this site locally for some reason, here's how you can do that.

The following instructions are for Linux. 

First, clone this repository and cd into the jamisonhunter.com directory. 

```bash
git clone https://github.com/JamisonHunter/jamisonhunter.com
cd jamisonhunter.com
```

Then, initialize the Python virtual environment.

The line below only needs to be run in order to create the virtual environment.

```bash
python3 -m venv venv
```

Next, start the environment. 

```bash
source venv/bin/activate
```

Install necessary packages with pip. 

You might want to upgrade pip first. 

```bash
pip install --upgrade pip
```

Then install packages.

```bash
pip install -r requirements.txt
```

Finally, run the app!

```bash
python3 main.py
```

The site should be running on port 8080 now!