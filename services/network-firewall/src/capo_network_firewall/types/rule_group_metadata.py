"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroupMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.vendor_name


class RuleGroupMetadata(TypedDict, closed=True):
    name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p>"""
    arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the rule group.</p>"""
    vendor_name: NotRequired["capo_network_firewall.types.vendor_name.VendorName"]
    """<p>The name of the Amazon Web Services Marketplace seller that provides this rule group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleGroupMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleGroupMetadata:
    out: RuleGroupMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("VendorName") is not None:
        out["vendor_name"] = data["VendorName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleGroupMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    return out


def deserialize_cbor(data: dict) -> RuleGroupMetadata:
    out: RuleGroupMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("VendorName") is not None:
        out["vendor_name"] = data["VendorName"]
    return out
