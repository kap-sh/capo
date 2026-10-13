"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionHeaderParameter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.boolean
    import capo_cloudwatch_events.types.header_key
    import capo_cloudwatch_events.types.header_value_sensitive


class ConnectionHeaderParameter(TypedDict, closed=True):
    key: NotRequired["capo_cloudwatch_events.types.header_key.HeaderKey"]
    """<p>The key for the parameter.</p>"""
    value: NotRequired[
        "capo_cloudwatch_events.types.header_value_sensitive.HeaderValueSensitive"
    ]
    """<p>The value associated with the key.</p>"""
    is_value_secret: "capo_cloudwatch_events.types.boolean.Boolean"
    """<p>Specified whether the value is a secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionHeaderParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["IsValueSecret"] = value.get("is_value_secret", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionHeaderParameter:
    out: ConnectionHeaderParameter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("IsValueSecret") is not None:
        out["is_value_secret"] = data["IsValueSecret"]
    else:
        out["is_value_secret"] = False
    return out


def redact_sensitive(value: ConnectionHeaderParameter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
