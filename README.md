# Python Legendas TV Organizer

Program to organize subtitles downloaded from [legendas.tv](http://legendas.tv). To work, run .py in a folder with the video file and the .zip downloaded from [legendas.tv](http://legendas.tv).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.x
```

### Installing

A step by step series of examples that tell you how to get a development env running

Install Python 3.x with pip

Install send2trash

```
pip install Send2Trash
```

Install PyInstaller, to generate .exe file (for Windows)

```
pip install pyinstaller
```


## Running the tests

### Linux, Mac OS X, BSD and most OSes except Windows
Turn script executable:

```
chmod +x legendas-tv-organizer.py
```

Call script inside a folder with photos:

```
./legendas-tv-organizer.py .
```

### Windows

To run a test, call the script inside a folder with photos.

```
python legendas-tv-organizer.py .
```

**For Windows in Context Menu:**

1. To generate *legendas-tv-organizer.exe* file to run on Windows.

```
pyinstaller -w -F legendas-tv-organizer.py
```

2. Add the keys on Registry or run *legendas-tv-organizer.reg*.
3. Copy .exe file on *C:\Program Files\Legendas TV Organizer*
4. Add *C:\Program Files\Legendas TV Organizer* in the *Path* on Windows Environment Variable.

## Contributing

Feel free to submitting pull requests.

## Authors

* **Matheus N. S. M. de Lima** - *Initial work* - [Site](https://imanasomali.vercel.app)


## License

This project is licensed under the [GNU General Public License](https://opensource.org/licenses/GPL-3.0).

## Acknowledgments

Codigo inspirado em:
* [photo-organizer](https://github.com/gabrielfroes/photo-organizer)
* [Código Fonte TV](https://www.youtube.com/codigofontetv), Youtube Channel.