"""Generated from Smithy shape ``com.amazonaws.inspector#CreateResourceGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.resource_group_tags


class CreateResourceGroupRequest(TypedDict, closed=True):
    resource_group_tags: "capo_inspector.types.resource_group_tags.ResourceGroupTags"
    """<p>A collection of keys and an array of possible values, '[{"key":"key1","values":["Value1","Value2"]},{"key":"Key2","values":["Value3"]}]'.</p> <p>For example,'[{"key":"Name","values":["TestEC2Instance"]}]'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResourceGroupRequest) -> dict:
    out: dict = {}
    import capo_inspector.types.resource_group_tags

    out["resourceGroupTags"] = (
        capo_inspector.types.resource_group_tags.serialize_aws_json_1_1(
            value["resource_group_tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResourceGroupRequest:
    out: CreateResourceGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceGroupTags") is not None:
        import capo_inspector.types.resource_group_tags

        out["resource_group_tags"] = (
            capo_inspector.types.resource_group_tags.deserialize_aws_json_1_1(
                data["resourceGroupTags"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResourceGroupRequest.resource_group_tags required"
        )
    return out
