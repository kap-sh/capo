"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetTagSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.resource_type
    import capo_ec2.types.tag_list


class SpotFleetTagSpecification(TypedDict, closed=True):
    resource_type: NotRequired["capo_ec2.types.resource_type.ResourceType"]
    """<p>The type of resource. Currently, the only resource type that is supported is <code>instance</code>. To tag the Spot Fleet request on creation, use the <code>TagSpecifications</code> parameter in <code> <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetRequestConfigData.html">SpotFleetRequestConfigData</a> </code>.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetTagSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_type" in value:
        import capo_ec2.types.resource_type

        capo_ec2.types.resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}Tag"
        )


def deserialize_ec2_query(el: Element) -> SpotFleetTagSpecification:
    out: SpotFleetTagSpecification = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        import capo_ec2.types.resource_type

        out["resource_type"] = capo_ec2.types.resource_type.deserialize_ec2_query(
            child_resource_type
        )
    child_tags = el.find("tag")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
