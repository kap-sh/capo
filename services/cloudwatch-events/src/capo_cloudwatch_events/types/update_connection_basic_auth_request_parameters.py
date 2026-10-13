"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#UpdateConnectionBasicAuthRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.auth_header_parameters
    import capo_cloudwatch_events.types.auth_header_parameters_sensitive


class UpdateConnectionBasicAuthRequestParameters(TypedDict, closed=True):
    username: NotRequired[
        "capo_cloudwatch_events.types.auth_header_parameters.AuthHeaderParameters"
    ]
    """<p>The user name to use for Basic authorization.</p>"""
    password: NotRequired[
        "capo_cloudwatch_events.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    ]
    """<p>The password associated with the user name to use for Basic authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionBasicAuthRequestParameters) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionBasicAuthRequestParameters:
    out: UpdateConnectionBasicAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    return out


def redact_sensitive(
    value: UpdateConnectionBasicAuthRequestParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
