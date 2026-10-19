"""Generated from Smithy shape ``com.amazonaws.datazone#IsNullExpression``."""

from typing_extensions import TypedDict


class IsNullExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsNullExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    return out


def deserialize_json(data: dict) -> IsNullExpression:
    out: IsNullExpression = {}  # type: ignore[typeddict-item]
    if data.get("columnName") is not None:
        out["column_name"] = data["columnName"]
    else:
        out["column_name"] = ""
    return out
