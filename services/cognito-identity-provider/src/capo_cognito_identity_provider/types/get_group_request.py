"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.group_name_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class GetGroupRequest(TypedDict, closed=True):
    group_name: "capo_cognito_identity_provider.types.group_name_type.GroupNameType"
    """<p>The name of the group that you want to get information about.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the group that you want to query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGroupRequest) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGroupRequest:
    out: GetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    return out
