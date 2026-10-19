"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateConnectionOAuthClientRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.auth_header_parameters
    import capo_cloudwatch_events.types.auth_header_parameters_sensitive


class CreateConnectionOAuthClientRequestParameters(TypedDict, closed=True):
    client_id: (
        "capo_cloudwatch_events.types.auth_header_parameters.AuthHeaderParameters"
    )
    """<p>The client ID to use for OAuth authorization for the connection.</p>"""
    client_secret: "capo_cloudwatch_events.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    """<p>The client secret associated with the client ID to use for OAuth authorization for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionOAuthClientRequestParameters) -> dict:
    out: dict = {}
    out["ClientID"] = value["client_id"]
    out["ClientSecret"] = value["client_secret"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateConnectionOAuthClientRequestParameters:
    out: CreateConnectionOAuthClientRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("ClientID") is not None:
        out["client_id"] = data["ClientID"]
    else:
        out["client_id"] = ""
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    else:
        out["client_secret"] = ""
    return out


def redact_sensitive(
    value: CreateConnectionOAuthClientRequestParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
