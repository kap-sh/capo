"""Generated from Smithy shape ``com.amazonaws.workspaces#SamlProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.saml_status_enum
    import capo_workspaces.types.saml_user_access_url


class SamlProperties(TypedDict, closed=True):
    status: NotRequired["capo_workspaces.types.saml_status_enum.SamlStatusEnum"]
    """<p>Indicates the status of SAML 2.0 authentication. These statuses include the following.</p> <ul> <li> <p>If the setting is <code>DISABLED</code>, end users will be directed to login with their directory credentials.</p> </li> <li> <p>If the setting is <code>ENABLED</code>, end users will be directed to login via the user access URL. Users attempting to connect to WorkSpaces from a client application that does not support SAML 2.0 authentication will not be able to connect.</p> </li> <li> <p>If the setting is <code>ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK</code>, end users will be directed to login via the user access URL on supported client applications, but will not prevent clients that do not support SAML 2.0 authentication from connecting as if SAML 2.0 authentication was disabled.</p> </li> </ul>"""
    user_access_url: NotRequired[
        "capo_workspaces.types.saml_user_access_url.SamlUserAccessUrl"
    ]
    """<p>The SAML 2.0 identity provider (IdP) user access URL is the URL a user would navigate to in their web browser in order to federate from the IdP and directly access the application, without any SAML 2.0 service provider (SP) bindings.</p>"""
    relay_state_parameter_name: NotRequired[
        "capo_workspaces.types.non_empty_string.NonEmptyString"
    ]
    """<p>The relay state parameter name supported by the SAML 2.0 identity provider (IdP). When the end user is redirected to the user access URL from the WorkSpaces client application, this relay state parameter name is appended as a query parameter to the URL along with the relay state endpoint to return the user to the client application session.</p> <p>To use SAML 2.0 authentication with WorkSpaces, the IdP must support IdP-initiated deep linking for the relay state URL. Consult your IdP documentation for more information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SamlProperties) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_workspaces.types.saml_status_enum

        out["Status"] = capo_workspaces.types.saml_status_enum.serialize_aws_json_1_1(
            value["status"]
        )
    if "user_access_url" in value:
        out["UserAccessUrl"] = value["user_access_url"]
    if "relay_state_parameter_name" in value:
        out["RelayStateParameterName"] = value["relay_state_parameter_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SamlProperties:
    out: SamlProperties = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_workspaces.types.saml_status_enum

        out["status"] = capo_workspaces.types.saml_status_enum.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("UserAccessUrl") is not None:
        out["user_access_url"] = data["UserAccessUrl"]
    if data.get("RelayStateParameterName") is not None:
        out["relay_state_parameter_name"] = data["RelayStateParameterName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SamlProperties) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_workspaces.types.saml_status_enum

        out["Status"] = capo_workspaces.types.saml_status_enum.serialize_cbor(
            value["status"]
        )
    if "user_access_url" in value:
        out["UserAccessUrl"] = value["user_access_url"]
    if "relay_state_parameter_name" in value:
        out["RelayStateParameterName"] = value["relay_state_parameter_name"]
    return out


def deserialize_cbor(data: dict) -> SamlProperties:
    out: SamlProperties = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_workspaces.types.saml_status_enum

        out["status"] = capo_workspaces.types.saml_status_enum.deserialize_cbor(
            data["Status"]
        )
    if data.get("UserAccessUrl") is not None:
        out["user_access_url"] = data["UserAccessUrl"]
    if data.get("RelayStateParameterName") is not None:
        out["relay_state_parameter_name"] = data["RelayStateParameterName"]
    return out
