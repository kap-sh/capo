"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.amazon_machine_image_security_group_list


class AmazonMachineImageRecommendation(TypedDict, closed=True):
    instance_type: "str"
    """<p>The recommended EC2 instance type for this AMI.</p>"""
    security_groups: NotRequired[
        "capo_marketplace_discovery.types.amazon_machine_image_security_group_list.AmazonMachineImageSecurityGroupList"
    ]
    """<p>The recommended security group configurations for this AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageRecommendation) -> dict:
    out: dict = {}
    out["instanceType"] = value["instance_type"]
    if "security_groups" in value:
        import capo_marketplace_discovery.types.amazon_machine_image_security_group_list

        out["securityGroups"] = (
            capo_marketplace_discovery.types.amazon_machine_image_security_group_list.serialize_json(
                value["security_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmazonMachineImageRecommendation:
    out: AmazonMachineImageRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        out["instance_type"] = ""
    if data.get("securityGroups") is not None:
        import capo_marketplace_discovery.types.amazon_machine_image_security_group_list

        out["security_groups"] = (
            capo_marketplace_discovery.types.amazon_machine_image_security_group_list.deserialize_json(
                data["securityGroups"]
            )
        )
    return out
