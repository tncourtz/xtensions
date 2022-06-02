# Notes

This is a set of python scripts that help with some Connector Connection management in NWC.
Use this at your own risk. These scripts exist because i don't like clicking around.

## Auth notes

There's various tokens that we need to use, and these are just notes on how those tokens are retrieved.

1. https://ntx-xtn.workflowcloud-test.com/logon redirects to auth0 at "https://ntxtest.auth0.com/authorize?audience=https://nintex.io&prompt=select_account&response_type=code&redirect_uri=https://ntx-xtn.workflowcloud-test.com/oidccallback&scope=openid profile email tenant_name_ntx-xtn region_WUS&client_id=d45Jmkd5N4tDX1s4gztd94uEdzA1YKqz"
2. Auth0 shows a login screen. That screen redirects us to AAD once you've entered a @nintex.com e-mail address.
3. AAD redirects you back to auth0
4. auth0 redirecs back to nintex at the oidccallback url: https://ntx-xtn.workflowcloud-test.com/oidccallback?code=HMXlT2p-OFoLw75dLnYseMojc5i2X4hwpJqV02hyrGDMh
5. oidccallback redirecs to /dashboard. OIDCCallback also sets a session cookie, which seems to be key.
   set-cookie: nwc:sess=s:uWhwl0btbPJzKGM4pR6FdT2rEqOvbgiU.5ZY0kA2d/1rIzIgBHbAcMzSYxRRGv9zV+gm4jalNlq8; Path=/; Expires=Thu, 02 Jun 2022 06:45:36 GMT; HttpOnly; Secure; SameSite=None
6. We get some app settings via https://ntx-xtn.workflowcloud-test.com/api/uxappconfig - see ###uxappconfig
7. We then generate a token via https://ntx-xtn.workflowcloud-test.com/generate-token. The simplest request is used to do that: `curl 'https://ntx-xtn.workflowcloud-test.com/generate-token' -H 'cookie: nwc:sess=s%3AuWSNIPSNIPlNlq8'`. This token is used for various calls, but doesn't seem to work against the connectors api.
8. Navigating to dashboard/Connections
9. Opening the page does a /generate-token again
10. Then, another token is requested via https://ntx-xtn.workflowcloud-test.com/api/apimanager/token with the same session cookie. This results in a 5min token that can be used for CreateConnection (/connection/api endpoints - i guess)
11. Contracts are retrieved with https://us.nintextest.io/connection/api/contracts?includePublic=true - using the short apimanager/token
12. Connectors are retrieved with https://us.nintextest.io/designer_/api/connector/connectors - using the long /generate-token it seems.

### uxappconfig

```json
{
  "apiManagerUrl": "https://us.nintextest.io",
  "zincUrl": "https://gbo-app-znc.nintextest.io/assets",
  "pdfFormConverterUrl": "https://gbo-fst-znc.nintextest.io/assets",
  "webTaggerUrl": "https://dgt.nintextest.io",
  "launchDarklyKey": "583f96472a70c80908565ca1",
  "whiteListedConnections": ["alpha", "beta", "hotel", "india"],
  "gaTrackingCode": "GTM-NTFWGG",
  "designerUrl": "https://designercdn--wus.workflowcloud-test.com/designer-xcomponent.min.js?v=1550550557322",
  "embedFormsUrl": "https://embeddedforms--wus.workflowcloud-test.com",
  "connectionsXcomponentUrl": "https://connectionscdn--gbo.workflowcloud-test.com",
  "userManagementXcomponent": {
    "redirectUri": "https://gbo-cli-vib.nintextest.io",
    "documentationUrl": "https://help.nintex.com/en-US/nwc",
    "url": "https://gbo-cli-vib.nintextest.io/wus/xcomponents/user-management.component.bundle.js"
  },
  "devTokenManagementXcomponent": {
    "url": "https://gbo-cli-vib.nintextest.io/wus/xcomponents/dev-token-management.component.bundle.js",
    "redirectUri": "https://gbo-cli-vib.nintextest.io"
  },
  "domainManagementXComponent": {
    "url": "https://gbo-cli-vib.nintextest.io/wus/xcomponents/domain-management.component.bundle.js",
    "redirectUri": "https://gbo-cli-vib.nintextest.io"
  },
  "appInsights": {
    "instrumentationKey": "920efc2d-f7e4-415a-9c43-41ea0eef26b8",
    "connectionString": "InstrumentationKey=920efc2d-f7e4-415a-9c43-41ea0eef26b8;IngestionEndpoint=https://eastus-3.in.applicationinsights.azure.com/"
  },
  "feedbackFormEndpoint": "https://ntx-test-wf.workflowcloud.com/api/v1/workflow/published/db18f320-09d1-4c2d-a781-735ec865a153/instances?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJOV0MiLCJ3b3JrZmxvd0lkIjoiZGIxOGYzMjAtMDlkMS00YzJkLWE3ODEtNzM1ZWM4NjVhMTUzIiwidGVuYW50SWQiOiI0ZDI2MWFkZC1kZTAzLTRhMWEtYjY4OS03ZWZmNDc3YTgyM2UiLCJpYXQiOjE1MzMwMDg3NjJ9.Dzp_uXVpD9IvzoqdmHOhDt5l5dfnoTN0EZFvCMyOxPs",
  "createTicketFormEndpoint": "https://ntx-test-wf.workflowcloud.com/forms/324dc2fa-cf66-4094-8719-b04f70b02dac",
  "appInsightsInstrumentationKey": "920efc2d-f7e4-415a-9c43-41ea0eef26b8",
  "cloudElementService": true,
  "serviceRegion": "wus",
  "boxAppUrl": "https://app.box.com/services/nintex_workflow_for_box",
  "allowedHawkeyeDomains": ".hawkeyecloud.com,.nintexhe.com,.nintextest.io,.nintexcloudtest.com",
  "readmeIOUrl": "https://developer.nintextest.com/v1.0",
  "devPortalUrls": {
    "queryJson": "https://developer.nintex.com/docs/nwc-tools/reference/engine-tools.yaml/paths/~1actions~1queryjson/post",
    "regex": "https://developer.nintex.com/docs/nwc-tools/reference/engine-tools.yaml/paths/~1actions~1regex/post"
  },
  "oidc": { "domain": "ntxtest.auth0.com", "clientId": "d45Jmkd5N4tDX1s4gztd94uEdzA1YKqz" },
  "user": {
    "id": "auth0|6013c51bfb06c3006957d1df",
    "email": "ruben.darco@nintex.com",
    "externalId": "ruben.darco@nintex.com",
    "firstName": "Ruben",
    "lastName": "D’Arco",
    "name": "Ruben D’Arco",
    "nintexTenantId": "00000000-0000-0000-0000-000000000001",
    "roles": ["administrator", "globalAdmin"],
    "permissions": ["workflow:publish"],
    "groups": [],
    "tenantId": "6fb13bd8-9546-41a2-ae8c-cdb91bd84118",
    "tenantName": "ntx-xtn",
    "displayName": "Ruben"
  }
}
```
