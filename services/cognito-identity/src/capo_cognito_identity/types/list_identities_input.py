"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ListIdentitiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.hide_disabled
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.pagination_key
    import capo_cognito_identity.types.query_limit


class ListIdentitiesInput(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    max_results: "capo_cognito_identity.types.query_limit.QueryLimit"
    """<p>The maximum number of identities to return.</p>"""
    next_token: NotRequired["capo_cognito_identity.types.pagination_key.PaginationKey"]
    """<p>A pagination token.</p>"""
    hide_disabled: NotRequired["capo_cognito_identity.types.hide_disabled.HideDisabled"]
    """<p>An optional boolean parameter that allows you to hide disabled identities. If omitted, the ListIdentities API will include disabled identities in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIdentitiesInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "hide_disabled" in value:
        out["HideDisabled"] = value["hide_disabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIdentitiesInput:
    out: ListIdentitiesInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError("ListIdentitiesInput.identity_pool_id required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        raise DeserializationError("ListIdentitiesInput.max_results required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("HideDisabled") is not None:
        out["hide_disabled"] = data["HideDisabled"]
    return out
