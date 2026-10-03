"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#UntagResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resource_groups_tagging_api.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag
    import capo_resource_groups_tagging_api.types.tag_key_list_for_untag


class UntagResourcesInput(TypedDict, closed=True):
    resource_arn_list: "capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag.ResourceARNListForTagUntag"
    """<p>Specifies a list of ARNs of the resources that you want to remove tags from.</p> <p>An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tag_keys: "capo_resource_groups_tagging_api.types.tag_key_list_for_untag.TagKeyListForUntag"
    """<p>Specifies a list of tag keys that you want to remove from the specified resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourcesInput) -> dict:
    out: dict = {}
    import capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag

    out["ResourceARNList"] = (
        capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag.serialize_aws_json_1_1(
            value["resource_arn_list"]
        )
    )
    import capo_resource_groups_tagging_api.types.tag_key_list_for_untag

    out["TagKeys"] = (
        capo_resource_groups_tagging_api.types.tag_key_list_for_untag.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourcesInput:
    out: UntagResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARNList") is not None:
        import capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag

        out["resource_arn_list"] = (
            capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag.deserialize_aws_json_1_1(
                data["ResourceARNList"]
            )
        )
    else:
        raise DeserializationError("UntagResourcesInput.resource_arn_list required")
    if data.get("TagKeys") is not None:
        import capo_resource_groups_tagging_api.types.tag_key_list_for_untag

        out["tag_keys"] = (
            capo_resource_groups_tagging_api.types.tag_key_list_for_untag.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourcesInput.tag_keys required")
    return out
