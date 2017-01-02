#### Troubleshooting

##### Vishnje opens a visualisation with an image viewer, rather than with a browser

This happened to me because the `index.html` file gets interpreted by
my system as an SVG image, because it contains an SVG tag. I fixed
setting my browser as the default opener for SVG files as well