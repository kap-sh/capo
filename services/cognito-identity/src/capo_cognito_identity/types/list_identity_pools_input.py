"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ListIdentityPoolsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.pagination_key
    import capo_cognito_identity.types.query_limit


class ListIdentityPoolsInput(TypedDict, closed=True):
    max_results: "capo_cognito_identity.types.query_limit.QueryLimit"
    """<p>The maximum number of identities to return.</p>"""
    next_token: NotRequired["capo_cognito_identity.types.pagination_key.PaginationKey"]
    """<p>A pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIdentityPoolsInput) -> dict:
    out: dict = {}
    out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIdentityPoolsInput:
    out: ListIdentityPoolsInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
