"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListWebAuthnCredentialsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key
    import capo_cognito_identity_provider.types.web_authn_credential_description_list_type


class ListWebAuthnCredentialsResponse(TypedDict, closed=True):
    credentials: "capo_cognito_identity_provider.types.web_authn_credential_description_list_type.WebAuthnCredentialDescriptionListType"
    """<p>A list of registered passkeys for a user.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWebAuthnCredentialsResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.web_authn_credential_description_list_type

    out["Credentials"] = (
        capo_cognito_identity_provider.types.web_authn_credential_description_list_type.serialize_aws_json_1_1(
            value["credentials"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWebAuthnCredentialsResponse:
    out: ListWebAuthnCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Credentials") is not None:
        import capo_cognito_identity_provider.types.web_authn_credential_description_list_type

        out["credentials"] = (
            capo_cognito_identity_provider.types.web_authn_credential_description_list_type.deserialize_aws_json_1_1(
                data["Credentials"]
            )
        )
    else:
        out["credentials"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
