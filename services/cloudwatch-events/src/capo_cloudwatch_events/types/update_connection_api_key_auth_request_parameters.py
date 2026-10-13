"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#UpdateConnectionApiKeyAuthRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.auth_header_parameters
    import capo_cloudwatch_events.types.auth_header_parameters_sensitive


class UpdateConnectionApiKeyAuthRequestParameters(TypedDict, closed=True):
    api_key_name: NotRequired[
        "capo_cloudwatch_events.types.auth_header_parameters.AuthHeaderParameters"
    ]
    """<p>The name of the API key to use for authorization.</p>"""
    api_key_value: NotRequired[
        "capo_cloudwatch_events.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    ]
    """<p>The value associated with teh API key to use for authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionApiKeyAuthRequestParameters) -> dict:
    out: dict = {}
    if "api_key_name" in value:
        out["ApiKeyName"] = value["api_key_name"]
    if "api_key_value" in value:
        out["ApiKeyValue"] = value["api_key_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionApiKeyAuthRequestParameters:
    out: UpdateConnectionApiKeyAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("ApiKeyName") is not None:
        out["api_key_name"] = data["ApiKeyName"]
    if data.get("ApiKeyValue") is not None:
        out["api_key_value"] = data["ApiKeyValue"]
    return out


def redact_sensitive(
    value: UpdateConnectionApiKeyAuthRequestParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key_value" in value:
        out["api_key_value"] = "*** Sensitive Data Redacted ***"
    return out
