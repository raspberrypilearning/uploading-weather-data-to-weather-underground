## Introduction

This guide assumes that you have already built and installed your Weather Station kit. If you have not done that yet, follow these instructions and then come back here when you've finished.

Weather Underground has a global community of people supplying data from weather stations and air quality monitors to provide hyperlocal data and forecasting. Many types of popular consumer weather stations can be used with Weather Underground and the code for the Oracle Raspberry Pi school kit can also be modified to stream data in the same way.

### What you will make
The steps in this guide assume that you will be regularly uploading data to Weather Underground. If you have limited bandwidth or poor connectivity between your station and the Internet then you might want to consider data a configuration that sends data every 15 minutes. The Weather Underground website will not display any data older than 20 minutes so batch uploads of data are only really useful for historical storage. If frequent uploads cause problems then you should probably use the Oracle database as described in the standard software build guide.
