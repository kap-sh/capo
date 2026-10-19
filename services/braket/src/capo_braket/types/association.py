"""Generated from Smithy shape ``com.amazonaws.braket#Association``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.association_type
    import capo_braket.types.braket_resource_arn


class Association(TypedDict, closed=True):
    arn: "capo_braket.types.braket_resource_arn.BraketResourceArn"
    """<p>The Amazon Braket resource arn.</p>"""
    type: "capo_braket.types.association_type.AssociationType"
    """<p>The association type for the specified Amazon Braket resource arn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Association) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Association:
    out: Association = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
