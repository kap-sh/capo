"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeTermsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.terms_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DescribeTermsRequest(TypedDict, closed=True):
    terms_id: "capo_cognito_identity_provider.types.terms_id_type.TermsIdType"
    """<p>The ID of the terms documents that you want to describe.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the terms documents that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTermsRequest) -> dict:
    out: dict = {}
    out["TermsId"] = value["terms_id"]
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTermsRequest:
    out: DescribeTermsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TermsId") is not None:
        out["terms_id"] = data["TermsId"]
    else:
        out["terms_id"] = ""
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    return out
