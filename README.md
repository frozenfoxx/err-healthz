# err-healthz

Health check plugin for Errbot.

# Usage
Send a HTTP GET request to `[server FQDN]/healthz`. The response code will tell you the status of Errbot.

## Reponse Codes
* `200`: service is online
