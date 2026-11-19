"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_usage_resource_type_name
    import capo_ec2.types.image_usage_resource_type_option_list


class ImageUsageResourceType(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_ec2.types.image_usage_resource_type_name.ImageUsageResourceTypeName"
    ]
    """<p>The resource type.</p> <p>Valid values: <code>ec2:Instance</code> | <code>ec2:LaunchTemplate</code> | <code>imagebuilder:ImageRecipe</code> | <code>imagebuilder:ContainerRecipe</code> </p>"""
    resource_type_options: NotRequired[
        "capo_ec2.types.image_usage_resource_type_option_list.ImageUsageResourceTypeOptionList"
    ]
    """<p>The options that affect the scope of the report. Valid only when <code>ResourceType</code> is <code>ec2:LaunchTemplate</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))
    if "resource_type_options" in value:
        import capo_ec2.types.image_usage_resource_type_option_list

        capo_ec2.types.image_usage_resource_type_option_list.serialize_ec2_query(
            value["resource_type_options"], pairs, f"{key_prefix}ResourceTypeOptionSet"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageResourceType:
    out: ImageUsageResourceType = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_resource_type_options = el.find("resourceTypeOptionSet")
    if child_resource_type_options is not None:
        import capo_ec2.types.image_usage_resource_type_option_list

        out["resource_type_options"] = (
            capo_ec2.types.image_usage_resource_type_option_list.deserialize_ec2_query(
                child_resource_type_options
            )
        )
    return out
