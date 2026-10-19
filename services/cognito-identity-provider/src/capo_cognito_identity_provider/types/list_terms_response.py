"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListTermsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.terms_description_list_type


class ListTermsResponse(TypedDict, closed=True):
    terms: "capo_cognito_identity_provider.types.terms_description_list_type.TermsDescriptionListType"
    """<p>A summary of the requested terms documents. Includes unique identifiers for later changes to the terms documents.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTermsResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.terms_description_list_type

    out["Terms"] = (
        capo_cognito_identity_provider.types.terms_description_list_type.serialize_aws_json_1_1(
            value["terms"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTermsResponse:
    out: ListTermsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Terms") is not None:
        import capo_cognito_identity_provider.types.terms_description_list_type

        out["terms"] = (
            capo_cognito_identity_provider.types.terms_description_list_type.deserialize_aws_json_1_1(
                data["Terms"]
            )
        )
    else:
        out["terms"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
