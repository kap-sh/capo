"""Generated from Smithy shape ``com.amazonaws.wickr#ListNetworksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_list


class ListNetworksResponse(TypedDict, closed=True):
    networks: "capo_wickr.types.network_list.NetworkList"
    """<p>A list of network objects for the Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworksResponse) -> dict:
    out: dict = {}
    import capo_wickr.types.network_list

    out["networks"] = capo_wickr.types.network_list.serialize_json(value["networks"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworksResponse:
    out: ListNetworksResponse = {}  # type: ignore[typeddict-item]
    if data.get("networks") is not None:
        import capo_wickr.types.network_list

        out["networks"] = capo_wickr.types.network_list.deserialize_json(
            data["networks"]
        )
    else:
        out["networks"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
