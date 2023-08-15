#!/bin/bash

docker run --rm -it -v ${PWD}:/work -w /work -p 8888:8000 --name youtube_dictation youtube_dictation_image $1