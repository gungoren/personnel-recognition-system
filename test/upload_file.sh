#!/bin/sh

aws s3 cp 1673-MEHMET-GUNGOREN.jpg s3://my-company-personnel-storage-wanted-amoeba/photos/portrait/ --metadata x-amz-meta-name=Mehmet,x-amz-meta-surname=Gungoren

