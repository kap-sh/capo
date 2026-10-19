"""Generated from Smithy shape ``com.amazonaws.backupgateway#VmwareToAwsTagMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.tag_key
    import capo_backup_gateway.types.tag_value
    import capo_backup_gateway.types.vmware_category
    import capo_backup_gateway.types.vmware_tag_name


class VmwareToAwsTagMapping(TypedDict, closed=True):
    vmware_category: "capo_backup_gateway.types.vmware_category.VmwareCategory"
    """<p>The is the category of VMware.</p>"""
    vmware_tag_name: "capo_backup_gateway.types.vmware_tag_name.VmwareTagName"
    """<p>This is the user-defined name of a VMware tag.</p>"""
    aws_tag_key: "capo_backup_gateway.types.tag_key.TagKey"
    """<p>The key part of the Amazon Web Services tag's key-value pair.</p>"""
    aws_tag_value: "capo_backup_gateway.types.tag_value.TagValue"
    """<p>The value part of the Amazon Web Services tag's key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmwareToAwsTagMapping) -> dict:
    out: dict = {}
    out["VmwareCategory"] = value["vmware_category"]
    out["VmwareTagName"] = value["vmware_tag_name"]
    out["AwsTagKey"] = value["aws_tag_key"]
    out["AwsTagValue"] = value["aws_tag_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VmwareToAwsTagMapping:
    out: VmwareToAwsTagMapping = {}  # type: ignore[typeddict-item]
    if data.get("VmwareCategory") is not None:
        out["vmware_category"] = data["VmwareCategory"]
    else:
        out["vmware_category"] = ""
    if data.get("VmwareTagName") is not None:
        out["vmware_tag_name"] = data["VmwareTagName"]
    else:
        out["vmware_tag_name"] = ""
    if data.get("AwsTagKey") is not None:
        out["aws_tag_key"] = data["AwsTagKey"]
    else:
        out["aws_tag_key"] = ""
    if data.get("AwsTagValue") is not None:
        out["aws_tag_value"] = data["AwsTagValue"]
    else:
        out["aws_tag_value"] = ""
    return out
