import rasterio
from rasterio import plot
import numpy
import os
from datetime import datetime
from dateutil import tz
import re

path = r"319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif"
dataset = rasterio.open(path)


def cover():
    #Get BANDs RED and NIR
    red = dataset.read(3).astype('float64')
    nir = dataset.read(4).astype('float64')

    #Calculate NVDI
    ndvi = numpy.where((nir+red)==0., 0, (nir-red)/(nir+red))

    return ndvi.sum() / ndvi.size


def centroid():
    # return {"type":"Point", "coordinates": [dataset.lnglat()]}
    return dataset.lnglat()


def area():
    #Get width area (km)
    width = dataset.bounds[2] - dataset.bounds[0]

    #Get height area (km)
    height = dataset.bounds[3] - dataset.bounds[1]

    return width * height


def localDateTime():
    #Extract date time from name file (pattern AAAAMMDD'T'HHMMSS'Z')
    datetime_string = re.search(r'\d{8}T\d{6}Z', dataset.name).group(0)

    #Convert date string to date object
    datetime_obj = datetime.strptime(datetime_string, '%Y%m%dT%H%M%SZ')

    #Convert zone UTC to Local
    utc_datetime = datetime_obj.replace(tzinfo=tz.gettz('UTC'))
    local_datetime = utc_datetime.astimezone(tz.tzlocal())

    return local_datetime.isoformat();


def fileName():
    return dataset.name

