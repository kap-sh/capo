"""Generated from Smithy shape ``com.amazonaws.osis#VpcAttachmentOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.boolean
    import capo_osis.types.cidr_block


class VpcAttachmentOptions(TypedDict, closed=True):
    attach_to_vpc: "capo_osis.types.boolean.Boolean"
    """<p>Whether a VPC is attached to the pipeline.</p>"""
    cidr_block: NotRequired["capo_osis.types.cidr_block.CidrBlock"]
    """<p>The CIDR block to be reserved for OpenSearch Ingestion to create elastic network interfaces (ENIs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcAttachmentOptions) -> dict:
    out: dict = {}
    out["AttachToVpc"] = value["attach_to_vpc"]
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    return out


def deserialize_json(data: dict) -> VpcAttachmentOptions:
    out: VpcAttachmentOptions = {}  # type: ignore[typeddict-item]
    if data.get("AttachToVpc") is not None:
        out["attach_to_vpc"] = data["AttachToVpc"]
    else:
        out["attach_to_vpc"] = False
    if data.get("CidrBlock") is not None:
        out["cidr_block"] = data["CidrBlock"]
    return out
