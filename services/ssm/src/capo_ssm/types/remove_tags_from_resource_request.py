"""Generated from Smithy shape ``com.amazonaws.ssm#RemoveTagsFromResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.key_list
    import capo_ssm.types.resource_id
    import capo_ssm.types.resource_type_for_tagging


class RemoveTagsFromResourceRequest(TypedDict, closed=True):
    resource_type: "capo_ssm.types.resource_type_for_tagging.ResourceTypeForTagging"
    """<p>The type of resource from which you want to remove a tag.</p> <note> <p>The <code>ManagedInstance</code> type for this API operation is only for on-premises managed nodes. Specify the name of the managed node in the following format: <code>mi-<i>ID_number</i> </code>. For example, <code>mi-1a2b3c4d5e6f</code>.</p> </note>"""
    resource_id: "capo_ssm.types.resource_id.ResourceId"
    """<p>The ID of the resource from which you want to remove tags. For example:</p> <p>ManagedInstance: mi-012345abcde</p> <p>MaintenanceWindow: mw-012345abcde</p> <p> <code>Automation</code>: <code>example-c160-4567-8519-012345abcde</code> </p> <p>PatchBaseline: pb-012345abcde</p> <p>OpsMetadata object: <code>ResourceID</code> for tagging is created from the Amazon Resource Name (ARN) for the object. Specifically, <code>ResourceID</code> is created from the strings that come after the word <code>opsmetadata</code> in the ARN. For example, an OpsMetadata object with an ARN of <code>arn:aws:ssm:us-east-2:1234567890:opsmetadata/aws/ssm/MyGroup/appmanager</code> has a <code>ResourceID</code> of either <code>aws/ssm/MyGroup/appmanager</code> or <code>/aws/ssm/MyGroup/appmanager</code>.</p> <p>For the Document and Parameter values, use the name of the resource.</p> <note> <p>The <code>ManagedInstance</code> type for this API operation is only for on-premises managed nodes. Specify the name of the managed node in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.</p> </note>"""
    tag_keys: "capo_ssm.types.key_list.KeyList"
    """<p>Tag keys that you want to remove from the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.resource_type_for_tagging

    out["ResourceType"] = (
        capo_ssm.types.resource_type_for_tagging.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import capo_ssm.types.key_list

    out["TagKeys"] = capo_ssm.types.key_list.serialize_aws_json_1_1(value["tag_keys"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceRequest:
    out: RemoveTagsFromResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        import capo_ssm.types.resource_type_for_tagging

        out["resource_type"] = (
            capo_ssm.types.resource_type_for_tagging.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_ssm.types.resource_type_for_tagging.ResourceTypeForTagging", ""
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("TagKeys") is not None:
        import capo_ssm.types.key_list

        out["tag_keys"] = capo_ssm.types.key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
