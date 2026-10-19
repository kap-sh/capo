"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateConnectionBasicAuthRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.auth_header_parameters
    import capo_eventbridge.types.auth_header_parameters_sensitive


class CreateConnectionBasicAuthRequestParameters(TypedDict, closed=True):
    username: "capo_eventbridge.types.auth_header_parameters.AuthHeaderParameters"
    """<p>The user name to use for Basic authorization.</p>"""
    password: "capo_eventbridge.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    """<p>The password associated with the user name to use for Basic authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionBasicAuthRequestParameters) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionBasicAuthRequestParameters:
    out: CreateConnectionBasicAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        out["password"] = ""
    return out


def redact_sensitive(
    value: CreateConnectionBasicAuthRequestParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
