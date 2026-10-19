"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListResourceServersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key_type
    import capo_cognito_identity_provider.types.resource_servers_list_type


class ListResourceServersResponse(TypedDict, closed=True):
    resource_servers: "capo_cognito_identity_provider.types.resource_servers_list_type.ResourceServersListType"
    """<p>An array of resource servers and the details of their configuration. For each, the response includes names, identifiers, and custom scopes.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceServersResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.resource_servers_list_type

    out["ResourceServers"] = (
        capo_cognito_identity_provider.types.resource_servers_list_type.serialize_aws_json_1_1(
            value["resource_servers"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceServersResponse:
    out: ListResourceServersResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceServers") is not None:
        import capo_cognito_identity_provider.types.resource_servers_list_type

        out["resource_servers"] = (
            capo_cognito_identity_provider.types.resource_servers_list_type.deserialize_aws_json_1_1(
                data["ResourceServers"]
            )
        )
    else:
        out["resource_servers"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
