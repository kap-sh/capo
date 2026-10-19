"""Generated from Smithy shape ``com.amazonaws.rtbfabric#QueryStringKeyValuePair``."""

from typing_extensions import TypedDict


class QueryStringKeyValuePair(TypedDict, closed=True):
    key: "str"
    """<p>The key of the query string parameter to match. Must contain only RFC 3986 unreserved characters.</p>"""
    value: "str"
    """<p>The value of the query string parameter to match. Must contain only RFC 3986 unreserved characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryStringKeyValuePair) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> QueryStringKeyValuePair:
    out: QueryStringKeyValuePair = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
