"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.external_region_code


class ContextEntry(TypedDict, closed=True):
    context_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the context entry.</p>"""
    context_type: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The type of the context entry, for example <code>SegmentId</code>, <code>Subnet</code>, or <code>Attachment</code>.</p>"""
    segment_type: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The type of the segment, for example <code>SecurityGroup</code>. Network Manager returns this value only when the context type is <code>SegmentId</code>.</p>"""
    public_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the resource, for example a security group ID, subnet ID, or transit gateway attachment ID.</p>"""
    region: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    availability_zone: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the Availability Zone of the resource, for example <code>use1-az2</code>. Network Manager returns this value only when the context type is <code>Subnet</code>.</p>"""
    attachment_type: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The type of the attachment, for example <code>VPC</code>. Network Manager returns this value only when the context type is <code>Attachment</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextEntry) -> dict:
    out: dict = {}
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    if "context_type" in value:
        out["ContextType"] = value["context_type"]
    if "segment_type" in value:
        out["SegmentType"] = value["segment_type"]
    if "public_id" in value:
        out["PublicId"] = value["public_id"]
    if "region" in value:
        out["Region"] = value["region"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "attachment_type" in value:
        out["AttachmentType"] = value["attachment_type"]
    return out


def deserialize_json(data: dict) -> ContextEntry:
    out: ContextEntry = {}  # type: ignore[typeddict-item]
    if data.get("ContextId") is not None:
        out["context_id"] = data["ContextId"]
    if data.get("ContextType") is not None:
        out["context_type"] = data["ContextType"]
    if data.get("SegmentType") is not None:
        out["segment_type"] = data["SegmentType"]
    if data.get("PublicId") is not None:
        out["public_id"] = data["PublicId"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("AttachmentType") is not None:
        out["attachment_type"] = data["AttachmentType"]
    return out
