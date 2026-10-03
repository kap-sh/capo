"""Generated from Smithy shape ``com.amazonaws.apigateway#Account``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.string
    import capo_api_gateway.types.throttle_settings


class Account(TypedDict, closed=True):
    cloudwatch_role_arn: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The ARN of an Amazon CloudWatch role for the current Account. </p>"""
    throttle_settings: NotRequired[
        "capo_api_gateway.types.throttle_settings.ThrottleSettings"
    ]
    """<p>Specifies the API request limits configured for the current Account.</p>"""
    features: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of features supported for the account. When usage plans are enabled, the features list will include an entry of <code>"UsagePlans"</code>.</p>"""
    api_key_version: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The version of the API keys used for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Account) -> dict:
    out: dict = {}
    if "cloudwatch_role_arn" in value:
        out["cloudwatchRoleArn"] = value["cloudwatch_role_arn"]
    if "throttle_settings" in value:
        import capo_api_gateway.types.throttle_settings

        out["throttleSettings"] = (
            capo_api_gateway.types.throttle_settings.serialize_json(
                value["throttle_settings"]
            )
        )
    if "features" in value:
        import capo_api_gateway.types.list_of_string

        out["features"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["features"]
        )
    if "api_key_version" in value:
        out["apiKeyVersion"] = value["api_key_version"]
    return out


def deserialize_json(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if data.get("cloudwatchRoleArn") is not None:
        out["cloudwatch_role_arn"] = data["cloudwatchRoleArn"]
    if data.get("throttleSettings") is not None:
        import capo_api_gateway.types.throttle_settings

        out["throttle_settings"] = (
            capo_api_gateway.types.throttle_settings.deserialize_json(
                data["throttleSettings"]
            )
        )
    if data.get("features") is not None:
        import capo_api_gateway.types.list_of_string

        out["features"] = capo_api_gateway.types.list_of_string.deserialize_json(
            data["features"]
        )
    if data.get("apiKeyVersion") is not None:
        out["api_key_version"] = data["apiKeyVersion"]
    return out
