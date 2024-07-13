# Weather Toast

Simple application that displays weather information in a toast notification. My first ***Python*** project.

## Install Dependencies

``` python
pip install python-dotenv
```

## Environment Variables

To run this code, you will need an API key from [Tomorrow.io](https://tomorrow.io). You can use an ***.env*** file or set the variables manually.

``` sh
TOMORROW_API_KEY=YOUR_TOMORROW_API_KEY
```

## Mock Usage

Tomorrow.io free tier calls get throttled, so I created a mock that can be switched on by using environment variables. To use the mock, you will need to setup a Mockaroo account, get an API key, and [create an API](https://www.mockaroo.com/apis) that uses this [schema](https://www.mockaroo.com/be37c810).

``` sh
MOCKAROO_API_KEY=YOUR_MOCKAROO_API_KEY
USE_MOCK=0 # or 1 to use Mockaroo. 
```

## Run It

``` sh
python ./weather-toast.py
```

A nice, easy to use, and *FREE* weather API was provided by ***[Tomorrow.io](https://tomorrow.io)***.

[<img src="https://github.com/Tomorrow-IO-API/tomorrow-weather-codes/blob/master/powered-by-tomorrow/Powered_by_Climacell-Halo.png?raw=true" width="250" />](https://tomorrow.io/)