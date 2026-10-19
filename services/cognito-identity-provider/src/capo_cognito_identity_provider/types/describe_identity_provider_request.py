"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeIdentityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.provider_name_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DescribeIdentityProviderRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that has the IdP that you want to describe..</p>"""
    provider_name: (
        "capo_cognito_identity_provider.types.provider_name_type.ProviderNameType"
    )
    """<p>The name of the IdP that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIdentityProviderRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ProviderName"] = value["provider_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIdentityProviderRequest:
    out: DescribeIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("ProviderName") is not None:
        out["provider_name"] = data["ProviderName"]
    else:
        out["provider_name"] = ""
    return out
