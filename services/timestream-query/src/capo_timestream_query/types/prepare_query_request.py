"""Generated from Smithy shape ``com.amazonaws.timestreamquery#PrepareQueryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.nullable_boolean
    import capo_timestream_query.types.query_string


class PrepareQueryRequest(TypedDict, closed=True):
    query_string: "capo_timestream_query.types.query_string.QueryString"
    """<p>The Timestream query string that you want to use as a prepared statement. Parameter names can be specified in the query string <code>@</code> character followed by an identifier. </p>"""
    validate_only: NotRequired[
        "capo_timestream_query.types.nullable_boolean.NullableBoolean"
    ]
    """<p>By setting this value to <code>true</code>, Timestream will only validate that the query string is a valid Timestream query, and not store the prepared query for later use.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrepareQueryRequest) -> dict:
    out: dict = {}
    out["QueryString"] = value["query_string"]
    if "validate_only" in value:
        out["ValidateOnly"] = value["validate_only"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PrepareQueryRequest:
    out: PrepareQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        out["query_string"] = ""
    if data.get("ValidateOnly") is not None:
        out["validate_only"] = data["ValidateOnly"]
    return out


def redact_sensitive(value: PrepareQueryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_string" in value:
        out["query_string"] = "*** Sensitive Data Redacted ***"
    return out
