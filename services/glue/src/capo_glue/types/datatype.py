"""Generated from Smithy shape ``com.amazonaws.glue#Datatype``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_limited_string


class Datatype(TypedDict, closed=True):
    id: "capo_glue.types.generic_limited_string.GenericLimitedString"
    """<p>The datatype of the value.</p>"""
    label: "capo_glue.types.generic_limited_string.GenericLimitedString"
    """<p>A label assigned to the datatype.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Datatype) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Label"] = value["label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Datatype:
    out: Datatype = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    else:
        out["label"] = ""
    return out
