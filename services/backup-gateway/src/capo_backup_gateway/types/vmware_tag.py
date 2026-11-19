"""Generated from Smithy shape ``com.amazonaws.backupgateway#VmwareTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.string
    import capo_backup_gateway.types.vmware_category
    import capo_backup_gateway.types.vmware_tag_name


class VmwareTag(TypedDict, closed=True):
    vmware_category: NotRequired[
        "capo_backup_gateway.types.vmware_category.VmwareCategory"
    ]
    """<p>The is the category of VMware.</p>"""
    vmware_tag_name: NotRequired[
        "capo_backup_gateway.types.vmware_tag_name.VmwareTagName"
    ]
    """<p>This is the user-defined name of a VMware tag.</p>"""
    vmware_tag_description: NotRequired["capo_backup_gateway.types.string.string"]
    """<p>This is a user-defined description of a VMware tag.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmwareTag) -> dict:
    out: dict = {}
    if "vmware_category" in value:
        out["VmwareCategory"] = value["vmware_category"]
    if "vmware_tag_name" in value:
        out["VmwareTagName"] = value["vmware_tag_name"]
    if "vmware_tag_description" in value:
        out["VmwareTagDescription"] = value["vmware_tag_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VmwareTag:
    out: VmwareTag = {}  # type: ignore[typeddict-item]
    if data.get("VmwareCategory") is not None:
        out["vmware_category"] = data["VmwareCategory"]
    if data.get("VmwareTagName") is not None:
        out["vmware_tag_name"] = data["VmwareTagName"]
    if data.get("VmwareTagDescription") is not None:
        out["vmware_tag_description"] = data["VmwareTagDescription"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VmwareTag) -> dict:
    out: dict = {}
    if "vmware_category" in value:
        out["VmwareCategory"] = value["vmware_category"]
    if "vmware_tag_name" in value:
        out["VmwareTagName"] = value["vmware_tag_name"]
    if "vmware_tag_description" in value:
        out["VmwareTagDescription"] = value["vmware_tag_description"]
    return out


def deserialize_cbor(data: dict) -> VmwareTag:
    out: VmwareTag = {}  # type: ignore[typeddict-item]
    if data.get("VmwareCategory") is not None:
        out["vmware_category"] = data["VmwareCategory"]
    if data.get("VmwareTagName") is not None:
        out["vmware_tag_name"] = data["VmwareTagName"]
    if data.get("VmwareTagDescription") is not None:
        out["vmware_tag_description"] = data["VmwareTagDescription"]
    return out
