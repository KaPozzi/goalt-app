#!/bin/bash

# Run gunny with the given arguments

gunicorn -b 0.0.0.0:5000 --workers 3 "goalt_app:create_app()"