"""Generated from Smithy shape ``com.amazonaws.datazone#BatchPutAttributeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.attribute_identifier


class BatchPutAttributeOutput(TypedDict, closed=True):
    attribute_identifier: "capo_datazone.types.attribute_identifier.AttributeIdentifier"
    """<p>The attribute ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAttributeOutput) -> dict:
    out: dict = {}
    out["attributeIdentifier"] = value["attribute_identifier"]
    return out


def deserialize_json(data: dict) -> BatchPutAttributeOutput:
    out: BatchPutAttributeOutput = {}  # type: ignore[typeddict-item]
    if data.get("attributeIdentifier") is not None:
        out["attribute_identifier"] = data["attributeIdentifier"]
    else:
        out["attribute_identifier"] = ""
    return out
