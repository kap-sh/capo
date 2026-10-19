"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateIamIdentityCenterConfigOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.iam_identity_center_group_attribute
    import capo_opensearchserverless.types.iam_identity_center_instance_arn
    import capo_opensearchserverless.types.iam_identity_center_user_attribute


class CreateIamIdentityCenterConfigOptions(TypedDict, closed=True):
    instance_arn: "capo_opensearchserverless.types.iam_identity_center_instance_arn.IamIdentityCenterInstanceArn"
    """<p>The ARN of the IAM Identity Center instance used to integrate with OpenSearch Serverless.</p>"""
    user_attribute: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_user_attribute.IamIdentityCenterUserAttribute"
    ]
    """<p>The user attribute for this IAM Identity Center integration. Defaults to <code>UserId</code>.</p>"""
    group_attribute: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_group_attribute.IamIdentityCenterGroupAttribute"
    ]
    """<p>The group attribute for this IAM Identity Center integration. Defaults to <code>GroupId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIamIdentityCenterConfigOptions) -> dict:
    out: dict = {}
    out["instanceArn"] = value["instance_arn"]
    if "user_attribute" in value:
        out["userAttribute"] = value["user_attribute"]
    if "group_attribute" in value:
        out["groupAttribute"] = value["group_attribute"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIamIdentityCenterConfigOptions:
    out: CreateIamIdentityCenterConfigOptions = {}  # type: ignore[typeddict-item]
    if data.get("instanceArn") is not None:
        out["instance_arn"] = data["instanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("userAttribute") is not None:
        out["user_attribute"] = data["userAttribute"]
    if data.get("groupAttribute") is not None:
        out["group_attribute"] = data["groupAttribute"]
    return out
