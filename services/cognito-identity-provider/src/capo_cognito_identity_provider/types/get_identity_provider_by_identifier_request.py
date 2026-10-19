"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetIdentityProviderByIdentifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.idp_identifier_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class GetIdentityProviderByIdentifierRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to get information about the IdP.</p>"""
    idp_identifier: (
        "capo_cognito_identity_provider.types.idp_identifier_type.IdpIdentifierType"
    )
    """<p>The identifier that you assigned to your user pool. The identifier is an alternative name for an IdP that is distinct from the IdP name. For example, an IdP with a name of <code>MyIdP</code> might have an identifier of the email domain <code>example.com</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdentityProviderByIdentifierRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["IdpIdentifier"] = value["idp_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdentityProviderByIdentifierRequest:
    out: GetIdentityProviderByIdentifierRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("IdpIdentifier") is not None:
        out["idp_identifier"] = data["IdpIdentifier"]
    else:
        out["idp_identifier"] = ""
    return out
