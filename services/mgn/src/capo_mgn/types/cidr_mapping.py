"""Generated from Smithy shape ``com.amazonaws.mgn#CidrMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.cidr


class CidrMapping(TypedDict, closed=True):
    original_cidr: "capo_mgn.types.cidr.Cidr"
    """<p>The original CIDR range in the source network.</p>"""
    updated_cidr: "capo_mgn.types.cidr.Cidr"
    """<p>The updated CIDR range to use in the target network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CidrMapping) -> dict:
    out: dict = {}
    out["originalCidr"] = value["original_cidr"]
    out["updatedCidr"] = value["updated_cidr"]
    return out


def deserialize_json(data: dict) -> CidrMapping:
    out: CidrMapping = {}  # type: ignore[typeddict-item]
    if data.get("originalCidr") is not None:
        out["original_cidr"] = data["originalCidr"]
    else:
        out["original_cidr"] = ""
    if data.get("updatedCidr") is not None:
        out["updated_cidr"] = data["updatedCidr"]
    else:
        out["updated_cidr"] = ""
    return out
