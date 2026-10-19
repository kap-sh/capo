"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#LookupDeveloperIdentityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.developer_user_identifier
    import capo_cognito_identity.types.identity_id
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.pagination_key
    import capo_cognito_identity.types.query_limit


class LookupDeveloperIdentityInput(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    identity_id: NotRequired["capo_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    developer_user_identifier: NotRequired[
        "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier"
    ]
    """<p>A unique ID used by your backend authentication process to identify a user. Typically, a developer identity provider would issue many developer user identifiers, in keeping with the number of users.</p>"""
    max_results: NotRequired["capo_cognito_identity.types.query_limit.QueryLimit"]
    """<p>The maximum number of identities to return.</p>"""
    next_token: NotRequired["capo_cognito_identity.types.pagination_key.PaginationKey"]
    """<p>A pagination token. The first call you make will have <code>NextToken</code> set to null. After that the service will return <code>NextToken</code> values as needed. For example, let's say you make a request with <code>MaxResults</code> set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupDeveloperIdentityInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "developer_user_identifier" in value:
        out["DeveloperUserIdentifier"] = value["developer_user_identifier"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LookupDeveloperIdentityInput:
    out: LookupDeveloperIdentityInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        out["identity_pool_id"] = ""
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    if data.get("DeveloperUserIdentifier") is not None:
        out["developer_user_identifier"] = data["DeveloperUserIdentifier"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
