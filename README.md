<h3>API Rest GIS</h3>


## Contents

- [Overview](#overview)
- [Quick start](#quick-start)
- [What's included](#whats-included)
- [Documentation](#documentation)
- [Authors](#authors)
- [License](#license)


## Overview


The API is just a REST service that returns some data from a GeoTIFF image. The technologies used are Python, Flask and RasterIO.

Here is what this little application demonstrates:

- Percentage of area of ​​this image that is covered by some type of vegetation
- Geographic scene centroid
- Scene area
- Local date and time of the imagined location at the time of capture.


## Quick start

**Warning**

> To run the project you will need to have installed Python3,Flask and RasterIO.

1. Download or clone project

2. Go to project folder and execute command.
 ```bash
 $ python api.py
 ```
 
Once the application runs you should see something like this
```bash
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## What's included

* Get GeoTIFF image information

```
  GET /vegetation-cover
  
  ```

```
  
  Example return data (SUCCESS).
   
  RESPONSE: HTTP 200 (Ok)
  
 {
    "filename": "319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif",
    "cover": 0.49715062845406466,
    "area": 1267031.25,
    "centroid": {
        "coordinates": [
            [
                -47.597228921551284,
                -15.858576386589299
            ]
        ],
        "type": "Point"
    },
    "local_time": "2016-12-07T12:19:53-03:00",
}
```

**Notes**
> The image must be in the project's root directory.


## Documentation

(swagger_api.yml)


## Authors

* **Wilson Filho**  - [Linkedin](https://www.linkedin.com/in/wilson-filho)

## License

This project is licensed under the MIT License.
