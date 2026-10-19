"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.service_network_list


class ListServiceNetworksResponse(TypedDict, closed=True):
    items: "capo_vpc_lattice.types.service_network_list.ServiceNetworkList"
    """<p>Information about the service networks.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworksResponse) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.service_network_list

    out["items"] = capo_vpc_lattice.types.service_network_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceNetworksResponse:
    out: ListServiceNetworksResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_vpc_lattice.types.service_network_list

        out["items"] = capo_vpc_lattice.types.service_network_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
