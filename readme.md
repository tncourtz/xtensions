# Ruben's Xtension playground

Very simple HTTP service used for Xtensions testing/debugging.

## Setup

This uses a `virtualenv` created with

```
python3.9 -m venv .
source bin/activate
```

Up until now, there's no additional requirements/packages needed to run this.


## HTTPS

We had a complex setup with certificates being read/used in the code, and needing to update the certificate manually.
This didn't work well, as python's `HTTPServer` isn't really made for that.

So, now we just run this as HTTP and put it behind a `nginx` that does the HTTPS for us, and we host this web service on HTTP.

