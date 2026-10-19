"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.description_type
    import capo_cognito_identity_provider.types.group_name_type
    import capo_cognito_identity_provider.types.precedence_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class CreateGroupRequest(TypedDict, closed=True):
    group_name: "capo_cognito_identity_provider.types.group_name_type.GroupNameType"
    """<p>A name for the group. This name must be unique in your user pool.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to create a user group.</p>"""
    description: NotRequired[
        "capo_cognito_identity_provider.types.description_type.DescriptionType"
    ]
    """<p>A description of the group that you're creating.</p>"""
    role_arn: NotRequired["capo_cognito_identity_provider.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (ARN) for the IAM role that you want to associate with the group. A group role primarily declares a preferred role for the credentials that you get from an identity pool. Amazon Cognito ID tokens have a <code>cognito:preferred_role</code> claim that presents the highest-precedence group that a user belongs to. Both ID and access tokens also contain a <code>cognito:groups</code> claim that list all the groups that a user is a member of.</p>"""
    precedence: NotRequired[
        "capo_cognito_identity_provider.types.precedence_type.PrecedenceType"
    ]
    """<p>A non-negative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. Zero is the highest precedence value. Groups with lower <code>Precedence</code> values take precedence over groups with higher or null <code>Precedence</code> values. If a user belongs to two or more groups, it is the group with the lowest precedence value whose role ARN is given in the user's tokens for the <code>cognito:roles</code> and <code>cognito:preferred_role</code> claims.</p> <p>Two groups can have the same <code>Precedence</code> value. If this happens, neither group takes precedence over the other. If two groups with the same <code>Precedence</code> have the same role ARN, that role is used in the <code>cognito:preferred_role</code> claim in tokens for users in each group. If the two groups have different role ARNs, the <code>cognito:preferred_role</code> claim isn't set in users' tokens.</p> <p>The default <code>Precedence</code> value is null. The maximum <code>Precedence</code> value is <code>2^31-1</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGroupRequest) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    out["UserPoolId"] = value["user_pool_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "precedence" in value:
        out["Precedence"] = value["precedence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGroupRequest:
    out: CreateGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Precedence") is not None:
        out["precedence"] = data["Precedence"]
    return out
