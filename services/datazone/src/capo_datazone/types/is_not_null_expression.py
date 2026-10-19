"""Generated from Smithy shape ``com.amazonaws.datazone#IsNotNullExpression``."""

from typing_extensions import TypedDict


class IsNotNullExpression(TypedDict, closed=True):
    column_name: "str"
    """<p>The name of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsNotNullExpression) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    return out


def deserialize_json(data: dict) -> IsNotNullExpression:
    out: IsNotNullExpression = {}  # type: ignore[typeddict-item]
    if data.get("columnName") is not None:
        out["column_name"] = data["columnName"]
    else:
        out["column_name"] = ""
    return out
