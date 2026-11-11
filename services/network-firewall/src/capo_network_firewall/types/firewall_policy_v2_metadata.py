"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicyV2Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class FirewallPolicyV2Metadata(TypedDict, closed=True):
    name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.</p>"""
    arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the Next Generation policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicyV2Metadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallPolicyV2Metadata:
    out: FirewallPolicyV2Metadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
