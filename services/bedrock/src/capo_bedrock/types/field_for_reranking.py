"""Generated from Smithy shape ``com.amazonaws.bedrock#FieldForReranking``."""

from typing_extensions import TypedDict


class FieldForReranking(TypedDict, closed=True):
    field_name: "str"
    """<p>The name of the metadata field to be used during the reranking process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldForReranking) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    return out


def deserialize_json(data: dict) -> FieldForReranking:
    out: FieldForReranking = {}  # type: ignore[typeddict-item]
    if data.get("fieldName") is not None:
        out["field_name"] = data["fieldName"]
    else:
        out["field_name"] = ""
    return out
