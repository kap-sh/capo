"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListTermsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.list_terms_request_max_results_integer
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class ListTermsRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to list terms documents.</p>"""
    max_results: NotRequired[
        "capo_cognito_identity_provider.types.list_terms_request_max_results_integer.ListTermsRequestMaxResultsInteger"
    ]
    """<p>The maximum number of terms documents that you want Amazon Cognito to return in the response.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTermsRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTermsRequest:
    out: ListTermsRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
