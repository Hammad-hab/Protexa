"""
    This file contains enviornment variables used in the rest of the program
"""

from utilities import loadAsset

SPLASHSCREEN_IMAGE = loadAsset("Splashscreen.jpeg", 'images')
PROTEXA_APP_DESCRIPTION = "Distribute encrypted websites over the \ninternet securely to authorized personnel and not to Pirates\n\n"
PROTEXA_RELEASE_KIND = "beta"
PROTEXA_VERSION = "v0.1.0"
PROTEXA_GEN = "CookieJar(Free)"
PROTEXA_MAIN_HEADING = "Welcome to Protexa"
PROTEXA_MAIN_CONTENT = "A web-system dedicated to the distribution of encrypted\ninformation such that only authorized personnel who have\nthe specific has, can access the encrypted website.\nehtml (Encrypted Hyper Text Markup Language) websites \ncannot be opened by a regular browser"
PROTEXA_EXTERNAL_DOCUMENTATION_LINK = "Read tutorial:<br/>       <a href='http://stackoverflow.com/'>Protexa Documentation</a>"
WINDOW_DIMENSIONS = (1000, 500) # (width, height)


OPENEHTML_INSTRUCTIONS = "\nLoad an encrypted Website from the internet. Protexa Websites are \
hosted online just like regular websites but they cannot be read by a normal browser since \
they are encrypted. To open a website you will need it's encryption key file (check if you \
were given a .prenc file). Enter the URL of the website then provide the encryption file.\n"

"""
Descriptions:
SPLASHSCREEN_IMAGE:     Image used in the spashscreen
PROTEXA_APP_DESCRIPTION:    the text that appears below the image and the version (generation) on the splashscreen
PROTEXA_RELEASE_KIND:   Beta || Stable || Unstable
PROTEXA_VERSION:    Version
PROTEXA_GEN:    A silly name assigned to each major build
PROTEXA_MAIN_HEADING:   Shown in the main page
PROTEXA_MAIN_CONTENT:   Contains the content of the main page.
PROTEXA_EXTERNAL_DOCUMENTATION_LINK:    Documentation link (Present on the splash screen)
"""