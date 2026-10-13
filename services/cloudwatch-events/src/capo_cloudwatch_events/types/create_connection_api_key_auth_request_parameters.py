"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateConnectionApiKeyAuthRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.auth_header_parameters
    import capo_cloudwatch_events.types.auth_header_parameters_sensitive


class CreateConnectionApiKeyAuthRequestParameters(TypedDict, closed=True):
    api_key_name: (
        "capo_cloudwatch_events.types.auth_header_parameters.AuthHeaderParameters"
    )
    """<p>The name of the API key to use for authorization.</p>"""
    api_key_value: "capo_cloudwatch_events.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    """<p>The value for the API key to use for authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionApiKeyAuthRequestParameters) -> dict:
    out: dict = {}
    out["ApiKeyName"] = value["api_key_name"]
    out["ApiKeyValue"] = value["api_key_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionApiKeyAuthRequestParameters:
    out: CreateConnectionApiKeyAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("ApiKeyName") is not None:
        out["api_key_name"] = data["ApiKeyName"]
    else:
        raise DeserializationError(
            "CreateConnectionApiKeyAuthRequestParameters.api_key_name required"
        )
    if data.get("ApiKeyValue") is not None:
        out["api_key_value"] = data["ApiKeyValue"]
    else:
        raise DeserializationError(
            "CreateConnectionApiKeyAuthRequestParameters.api_key_value required"
        )
    return out


def redact_sensitive(
    value: CreateConnectionApiKeyAuthRequestParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key_value" in value:
        out["api_key_value"] = "*** Sensitive Data Redacted ***"
    return out
