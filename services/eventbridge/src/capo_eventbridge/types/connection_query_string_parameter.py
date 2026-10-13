"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionQueryStringParameter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.boolean
    import capo_eventbridge.types.query_string_key
    import capo_eventbridge.types.query_string_value_sensitive


class ConnectionQueryStringParameter(TypedDict, closed=True):
    key: NotRequired["capo_eventbridge.types.query_string_key.QueryStringKey"]
    """<p>The key for a query string parameter.</p>"""
    value: NotRequired[
        "capo_eventbridge.types.query_string_value_sensitive.QueryStringValueSensitive"
    ]
    """<p>The value associated with the key for the query string parameter.</p>"""
    is_value_secret: "capo_eventbridge.types.boolean.Boolean"
    """<p>Specifies whether the value is secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionQueryStringParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["IsValueSecret"] = value.get("is_value_secret", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionQueryStringParameter:
    out: ConnectionQueryStringParameter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("IsValueSecret") is not None:
        out["is_value_secret"] = data["IsValueSecret"]
    else:
        out["is_value_secret"] = False
    return out


def redact_sensitive(value: ConnectionQueryStringParameter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
