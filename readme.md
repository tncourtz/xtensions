# Ruben's Xtension playground

Very simple HTTP service used for Xtensions testing/debugging.

## Setup

This uses a `virtualenv` created with

```
python3.9 -m venv .
source bin/activate
```

## HTTPS

The web service can uses HTTPS. I just get the \*.pem files from the letencrypt directory and copy all pem files from `/etc/letsencrypt/archive/pyro.prof-x.net` into here. That will have to happen every time new certs are created.
The `certifcates` folder is hidden via .gitigore.
