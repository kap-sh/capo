"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListIdentityProvidersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key_type
    import capo_cognito_identity_provider.types.providers_list_type


class ListIdentityProvidersResponse(TypedDict, closed=True):
    providers: (
        "capo_cognito_identity_provider.types.providers_list_type.ProvidersListType"
    )
    """<p>An array of the IdPs in your user pool. For each, the response includes identifiers, the IdP name and type, and trust-relationship details like the issuer URL.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIdentityProvidersResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.providers_list_type

    out["Providers"] = (
        capo_cognito_identity_provider.types.providers_list_type.serialize_aws_json_1_1(
            value["providers"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIdentityProvidersResponse:
    out: ListIdentityProvidersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Providers") is not None:
        import capo_cognito_identity_provider.types.providers_list_type

        out["providers"] = (
            capo_cognito_identity_provider.types.providers_list_type.deserialize_aws_json_1_1(
                data["Providers"]
            )
        )
    else:
        out["providers"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
