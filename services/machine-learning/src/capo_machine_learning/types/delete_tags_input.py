"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.tag_key_list
    import capo_machine_learning.types.taggable_resource_type


class DeleteTagsInput(TypedDict, closed=True):
    tag_keys: "capo_machine_learning.types.tag_key_list.TagKeyList"
    """<p>One or more tags to delete.</p>"""
    resource_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID of the tagged ML object. For example, <code>exampleModelId</code>.</p>"""
    resource_type: (
        "capo_machine_learning.types.taggable_resource_type.TaggableResourceType"
    )
    """<p>The type of the tagged ML object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsInput) -> dict:
    out: dict = {}
    import capo_machine_learning.types.tag_key_list

    out["TagKeys"] = capo_machine_learning.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    out["ResourceId"] = value["resource_id"]
    import capo_machine_learning.types.taggable_resource_type

    out["ResourceType"] = (
        capo_machine_learning.types.taggable_resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsInput:
    out: DeleteTagsInput = {}  # type: ignore[typeddict-item]
    if data.get("TagKeys") is not None:
        import capo_machine_learning.types.tag_key_list

        out["tag_keys"] = (
            capo_machine_learning.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
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
