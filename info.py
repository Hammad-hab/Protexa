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
PROTEXA_EXTERNAL_DOCUMENTATION_LINK = "Read tutorial:<br/>       <a href='http://stackoverflow.com/'>Protexa Documentation</a>"

"""
Descriptions:
SPLASHSCREEN_IMAGE: Image used in the spashscreen
PROTEXA_APP_DESCRIPTION: the text that appears below the image and the version (generation) on the splashscreen
PROTEXA_RELEASE_KIND: Beta || Stable || Unstable
PROTEXA_VERSION: Version
PROTEXA_GEN: A silly name assigned to each major build
PROTEXA_MAIN_HEADING: Shown in the main page
PROTEXA_EXTERNAL_DOCUMENTATION_LINK: Documentation link (Present on the splash screen)
"""