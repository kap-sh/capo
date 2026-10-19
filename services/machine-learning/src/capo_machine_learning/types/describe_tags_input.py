"""Generated from Smithy shape ``com.amazonaws.machinelearning#DescribeTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.taggable_resource_type


class DescribeTagsInput(TypedDict, closed=True):
    resource_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the ML object. For example, <code>exampleModelId</code>. </p>"""
    resource_type: (
        "capo_machine_learning.types.taggable_resource_type.TaggableResourceType"
    )
    """<p>The type of the ML object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsInput) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_machine_learning.types.taggable_resource_type

    out["ResourceType"] = (
        capo_machine_learning.types.taggable_resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsInput:
    out: DescribeTagsInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        import capo_machine_learning.types.taggable_resource_type

        out["resource_type"] = (
            capo_machine_learning.types.taggable_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_machine_learning.types.taggable_resource_type.TaggableResourceType",
            "",
        )
    return out
