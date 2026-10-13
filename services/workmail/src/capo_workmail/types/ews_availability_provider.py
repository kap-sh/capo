"""Generated from Smithy shape ``com.amazonaws.workmail#EwsAvailabilityProvider``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.external_user_name
    import capo_workmail.types.password
    import capo_workmail.types.url


class EwsAvailabilityProvider(TypedDict, closed=True):
    ews_endpoint: "capo_workmail.types.url.Url"
    """<p>The endpoint of the remote EWS server.</p>"""
    ews_username: "capo_workmail.types.external_user_name.ExternalUserName"
    """<p>The username used to authenticate the remote EWS server.</p>"""
    ews_password: "capo_workmail.types.password.Password"
    """<p>The password used to authenticate the remote EWS server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EwsAvailabilityProvider) -> dict:
    out: dict = {}
    out["EwsEndpoint"] = value["ews_endpoint"]
    out["EwsUsername"] = value["ews_username"]
    out["EwsPassword"] = value["ews_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EwsAvailabilityProvider:
    out: EwsAvailabilityProvider = {}  # type: ignore[typeddict-item]
    if data.get("EwsEndpoint") is not None:
        out["ews_endpoint"] = data["EwsEndpoint"]
    else:
        raise DeserializationError("EwsAvailabilityProvider.ews_endpoint required")
    if data.get("EwsUsername") is not None:
        out["ews_username"] = data["EwsUsername"]
    else:
        raise DeserializationError("EwsAvailabilityProvider.ews_username required")
    if data.get("EwsPassword") is not None:
        out["ews_password"] = data["EwsPassword"]
    else:
        raise DeserializationError("EwsAvailabilityProvider.ews_password required")
    return out


def redact_sensitive(value: EwsAvailabilityProvider) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ews_password" in value:
        out["ews_password"] = "*** Sensitive Data Redacted ***"
    return out
