"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#UpdateConnectionOAuthClientRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.auth_header_parameters
    import capo_cloudwatch_events.types.auth_header_parameters_sensitive


class UpdateConnectionOAuthClientRequestParameters(TypedDict, closed=True):
    client_id: NotRequired[
        "capo_cloudwatch_events.types.auth_header_parameters.AuthHeaderParameters"
    ]
    """<p>The client ID to use for OAuth authorization.</p>"""
    client_secret: NotRequired[
        "capo_cloudwatch_events.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    ]
    """<p>The client secret assciated with the client ID to use for OAuth authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionOAuthClientRequestParameters) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientID"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateConnectionOAuthClientRequestParameters:
    out: UpdateConnectionOAuthClientRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("ClientID") is not None:
        out["client_id"] = data["ClientID"]
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    return out


def redact_sensitive(
    value: UpdateConnectionOAuthClientRequestParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
