"""Generated from Smithy shape ``com.amazonaws.datazone#NotLikeExpression``."""

from typing_extensions import TypedDict


class NotLikeExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""
    value: "str"
    """<p>The value that might not be like the expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotLikeExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> NotLikeExpression:
    out: NotLikeExpression = {}  # type: ignore[typeddict-item]
    if data.get("columnName") is not None:
        out["column_name"] = data["columnName"]
    else:
        out["column_name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
