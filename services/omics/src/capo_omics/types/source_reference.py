"""Generated from Smithy shape ``com.amazonaws.omics#SourceReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.source_reference_type
    import capo_omics.types.source_reference_value


class SourceReference(TypedDict, closed=True):
    type: "capo_omics.types.source_reference_type.SourceReferenceType"
    """<p>The type of source reference, such as branch, tag, or commit.</p>"""
    value: "capo_omics.types.source_reference_value.SourceReferenceValue"
    """<p>The value of the source reference, such as the branch name, tag name, or commit ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceReference) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SourceReference:
    out: SourceReference = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
