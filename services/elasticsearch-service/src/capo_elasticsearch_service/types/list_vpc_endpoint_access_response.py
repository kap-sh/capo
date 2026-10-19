"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListVpcEndpointAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.authorized_principal_list
    import capo_elasticsearch_service.types.next_token


class ListVpcEndpointAccessResponse(TypedDict, closed=True):
    authorized_principal_list: "capo_elasticsearch_service.types.authorized_principal_list.AuthorizedPrincipalList"
    """<p>List of <code>AuthorizedPrincipal</code> describing the details of the permissions to manage VPC endpoints against the specified domain.</p>"""
    next_token: "capo_elasticsearch_service.types.next_token.NextToken"
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcEndpointAccessResponse) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.authorized_principal_list

    out["AuthorizedPrincipalList"] = (
        capo_elasticsearch_service.types.authorized_principal_list.serialize_json(
            value["authorized_principal_list"]
        )
    )
    out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVpcEndpointAccessResponse:
    out: ListVpcEndpointAccessResponse = {}  # type: ignore[typeddict-item]
    if data.get("AuthorizedPrincipalList") is not None:
        import capo_elasticsearch_service.types.authorized_principal_list

        out["authorized_principal_list"] = (
            capo_elasticsearch_service.types.authorized_principal_list.deserialize_json(
                data["AuthorizedPrincipalList"]
            )
        )
    else:
        out["authorized_principal_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    else:
        out["next_token"] = ""
    return out
