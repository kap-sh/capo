"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListResourceEndpointAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.resource_endpoint_association_list


class ListResourceEndpointAssociationsResponse(TypedDict, closed=True):
    items: "capo_vpc_lattice.types.resource_endpoint_association_list.ResourceEndpointAssociationList"
    """<p>Information about the VPC endpoint associations.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceEndpointAssociationsResponse) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.resource_endpoint_association_list

    out["items"] = (
        capo_vpc_lattice.types.resource_endpoint_association_list.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceEndpointAssociationsResponse:
    out: ListResourceEndpointAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_vpc_lattice.types.resource_endpoint_association_list

        out["items"] = (
            capo_vpc_lattice.types.resource_endpoint_association_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
