<center>
<div>
<h1>Protexa</h1>
<h3>v0.1.2 Beta (Build: <code>CookieJar</code>)</h3>
</div>
Distribute encrypted websites over the internet
</center>

## TL;DR
Protexa is an Open Source Browser based on Chromium and Qt that is used for distributing websites over the internet while preventing unauthorised access. Protexa does this by producing encrypted websites. These are `.html` files compiled into the Protexa Standard `.ehtml`, while making a `.prenc` file containing the instructions to decode the file. Only the people with the corresponding `.prenc` can read the website.

## Workings and Security
Protexa doesn't store any information regarding the decryption of the website. Once it has been encrypted, a file is produced containing the RSA key to decrypt the file. Protexa (in future updates) will also prevent the user who has a copy (but not the original) `.prenc` file from distributing it.

## Roadmap and Sharp edges
* Protexa lacks a proper encryption mechanism
* Chromium embed is slow and can crash
* Performance is extremely slow due to PyQt6
* Compiled binary is not yet available
* `.ehtml` standard has not been implemented