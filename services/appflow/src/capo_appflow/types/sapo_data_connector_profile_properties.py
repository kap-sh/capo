"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.application_host_url
    import capo_appflow.types.application_service_path
    import capo_appflow.types.boolean
    import capo_appflow.types.client_number
    import capo_appflow.types.logon_language
    import capo_appflow.types.o_auth_properties
    import capo_appflow.types.port_number
    import capo_appflow.types.private_link_service_name


class SAPODataConnectorProfileProperties(TypedDict, closed=True):
    application_host_url: "capo_appflow.types.application_host_url.ApplicationHostUrl"
    """<p> The location of the SAPOData resource. </p>"""
    application_service_path: (
        "capo_appflow.types.application_service_path.ApplicationServicePath"
    )
    """<p> The application path to catalog service. </p>"""
    port_number: "capo_appflow.types.port_number.PortNumber"
    """<p> The port number of the SAPOData instance. </p>"""
    client_number: "capo_appflow.types.client_number.ClientNumber"
    """<p> The client number for the client creating the connection. </p>"""
    logon_language: NotRequired["capo_appflow.types.logon_language.LogonLanguage"]
    """<p> The logon language of SAPOData instance. </p>"""
    private_link_service_name: NotRequired[
        "capo_appflow.types.private_link_service_name.PrivateLinkServiceName"
    ]
    """<p> The SAPOData Private Link service name to be used for private data transfers. </p>"""
    o_auth_properties: NotRequired[
        "capo_appflow.types.o_auth_properties.OAuthProperties"
    ]
    """<p> The SAPOData OAuth properties required for OAuth type authentication. </p>"""
    disable_sso: "capo_appflow.types.boolean.Boolean"
    """<p>If you set this parameter to <code>true</code>, Amazon AppFlow bypasses the single sign-on (SSO) settings in your SAP account when it accesses your SAP OData instance.</p> <p>Whether you need this option depends on the types of credentials that you applied to your SAP OData connection profile. If your profile uses basic authentication credentials, SAP SSO can prevent Amazon AppFlow from connecting to your account with your username and password. In this case, bypassing SSO makes it possible for Amazon AppFlow to connect successfully. However, if your profile uses OAuth credentials, this parameter has no affect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataConnectorProfileProperties) -> dict:
    out: dict = {}
    out["applicationHostUrl"] = value["application_host_url"]
    out["applicationServicePath"] = value["application_service_path"]
    out["portNumber"] = value["port_number"]
    out["clientNumber"] = value["client_number"]
    if "logon_language" in value:
        out["logonLanguage"] = value["logon_language"]
    if "private_link_service_name" in value:
        out["privateLinkServiceName"] = value["private_link_service_name"]
    if "o_auth_properties" in value:
        import capo_appflow.types.o_auth_properties

        out["oAuthProperties"] = capo_appflow.types.o_auth_properties.serialize_json(
            value["o_auth_properties"]
        )
    out["disableSSO"] = value.get("disable_sso", False)
    return out


def deserialize_json(data: dict) -> SAPODataConnectorProfileProperties:
    out: SAPODataConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if data.get("applicationHostUrl") is not None:
        out["application_host_url"] = data["applicationHostUrl"]
    else:
        out["application_host_url"] = ""
    if data.get("applicationServicePath") is not None:
        out["application_service_path"] = data["applicationServicePath"]
    else:
        out["application_service_path"] = ""
    if data.get("portNumber") is not None:
        out["port_number"] = data["portNumber"]
    else:
        out["port_number"] = 0
    if data.get("clientNumber") is not None:
        out["client_number"] = data["clientNumber"]
    else:
        out["client_number"] = ""
    if data.get("logonLanguage") is not None:
        out["logon_language"] = data["logonLanguage"]
    if data.get("privateLinkServiceName") is not None:
        out["private_link_service_name"] = data["privateLinkServiceName"]
    if data.get("oAuthProperties") is not None:
        import capo_appflow.types.o_auth_properties

        out["o_auth_properties"] = (
            capo_appflow.types.o_auth_properties.deserialize_json(
                data["oAuthProperties"]
            )
        )
    if data.get("disableSSO") is not None:
        out["disable_sso"] = data["disableSSO"]
    else:
        out["disable_sso"] = False
    return out
