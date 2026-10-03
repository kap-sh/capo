"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.taggable_resource_arn
    import capo_sso_admin.types.token


class ListTagsForResourceRequest(TypedDict, closed=True):
    instance_arn: NotRequired["capo_sso_admin.types.instance_arn.InstanceArn"]
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    resource_arn: "capo_sso_admin.types.taggable_resource_arn.TaggableResourceArn"
    """<p>The ARN of the resource with the tags to be listed.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    out["ResourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
