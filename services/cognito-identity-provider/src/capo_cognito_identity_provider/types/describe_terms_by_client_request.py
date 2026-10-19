"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeTermsByClientRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.terms_name_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DescribeTermsByClientRequest(TypedDict, closed=True):
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that the terms documents are associated with.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the terms documents that you want to describe.</p>"""
    terms_name: "capo_cognito_identity_provider.types.terms_name_type.TermsNameType"
    """<p>The name of the terms documents that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTermsByClientRequest) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["UserPoolId"] = value["user_pool_id"]
    out["TermsName"] = value["terms_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTermsByClientRequest:
    out: DescribeTermsByClientRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("TermsName") is not None:
        out["terms_name"] = data["TermsName"]
    else:
        out["terms_name"] = ""
    return out


def redact_sensitive(value: DescribeTermsByClientRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
