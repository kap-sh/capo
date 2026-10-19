"""Generated from Smithy shape ``com.amazonaws.ssm#AddTagsToResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.resource_id
    import capo_ssm.types.resource_type_for_tagging
    import capo_ssm.types.tag_list


class AddTagsToResourceRequest(TypedDict, closed=True):
    resource_type: "capo_ssm.types.resource_type_for_tagging.ResourceTypeForTagging"
    """<p>Specifies the type of resource you are tagging.</p> <note> <p>The <code>ManagedInstance</code> type for this API operation is for on-premises managed nodes. You must specify the name of the managed node in the following format: <code>mi-<i>ID_number</i> </code>. For example, <code>mi-1a2b3c4d5e6f</code>.</p> </note>"""
    resource_id: "capo_ssm.types.resource_id.ResourceId"
    """<p>The resource ID you want to tag.</p> <p>Use the ID of the resource. Here are some examples:</p> <p> <code>MaintenanceWindow</code>: <code>mw-012345abcde</code> </p> <p> <code>PatchBaseline</code>: <code>pb-012345abcde</code> </p> <p> <code>Automation</code>: <code>example-c160-4567-8519-012345abcde</code> </p> <p> <code>OpsMetadata</code> object: <code>ResourceID</code> for tagging is created from the Amazon Resource Name (ARN) for the object. Specifically, <code>ResourceID</code> is created from the strings that come after the word <code>opsmetadata</code> in the ARN. For example, an OpsMetadata object with an ARN of <code>arn:aws:ssm:us-east-2:1234567890:opsmetadata/aws/ssm/MyGroup/appmanager</code> has a <code>ResourceID</code> of either <code>aws/ssm/MyGroup/appmanager</code> or <code>/aws/ssm/MyGroup/appmanager</code>.</p> <p>For the <code>Document</code> and <code>Parameter</code> values, use the name of the resource. If you're tagging a shared document, you must use the full ARN of the document.</p> <p> <code>ManagedInstance</code>: <code>mi-012345abcde</code> </p> <note> <p>The <code>ManagedInstance</code> type for this API operation is only for on-premises managed nodes. You must specify the name of the managed node in the following format: <code>mi-<i>ID_number</i> </code>. For example, <code>mi-1a2b3c4d5e6f</code>.</p> </note>"""
    tags: "capo_ssm.types.tag_list.TagList"
    """<p>One or more tags. The value parameter is required.</p> <important> <p>Don't enter personally identifiable information in this field.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.resource_type_for_tagging

    out["ResourceType"] = (
        capo_ssm.types.resource_type_for_tagging.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import capo_ssm.types.tag_list

    out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceRequest:
    out: AddTagsToResourceRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = []
    return out
