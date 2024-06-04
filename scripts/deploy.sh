#!/bin/bash

poetry export --without-hashes > requirements.txt
vercel --prod