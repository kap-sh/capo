"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.tag_key_list
    import capo_sso_admin.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    instance_arn: NotRequired["capo_sso_admin.types.instance_arn.InstanceArn"]
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    resource_arn: "capo_sso_admin.types.taggable_resource_arn.TaggableResourceArn"
    """<p>The ARN of the resource with the tags to be listed.</p>"""
    tag_keys: "capo_sso_admin.types.tag_key_list.TagKeyList"
    """<p>The keys of tags that are attached to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    out["ResourceArn"] = value["resource_arn"]
    import capo_sso_admin.types.tag_key_list

    out["TagKeys"] = capo_sso_admin.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if data.get("TagKeys") is not None:
        import capo_sso_admin.types.tag_key_list

        out["tag_keys"] = capo_sso_admin.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
