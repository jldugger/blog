#!/bin/bash

# generate and install content
pelican

# minify css

while IFS= read -r -d '' css
do
    cssmin < "$css" | sponge "$css"
done <   <(find ./output/theme/css/ -name '*.css')
