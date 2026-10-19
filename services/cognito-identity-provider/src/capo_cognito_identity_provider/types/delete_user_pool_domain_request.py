"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteUserPoolDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.domain_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DeleteUserPoolDomainRequest(TypedDict, closed=True):
    domain: "capo_cognito_identity_provider.types.domain_type.DomainType"
    """<p>The domain that you want to delete. For custom domains, this is the fully-qualified domain name like <code>auth.example.com</code>. For Amazon Cognito prefix domains, this is the prefix alone, like <code>myprefix</code>.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to delete the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserPoolDomainRequest) -> dict:
    out: dict = {}
    out["Domain"] = value["domain"]
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserPoolDomainRequest:
    out: DeleteUserPoolDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        out["domain"] = ""
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    return out
