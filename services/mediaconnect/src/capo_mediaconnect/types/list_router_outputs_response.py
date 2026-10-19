"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListRouterOutputsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_router_output_list


class ListRouterOutputsResponse(TypedDict, closed=True):
    router_outputs: (
        "capo_mediaconnect.types.listed_router_output_list.ListedRouterOutputList"
    )
    """<p>The summary information for the retrieved router outputs.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRouterOutputsResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.listed_router_output_list

    out["routerOutputs"] = (
        capo_mediaconnect.types.listed_router_output_list.serialize_json(
            value["router_outputs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRouterOutputsResponse:
    out: ListRouterOutputsResponse = {}  # type: ignore[typeddict-item]
    if data.get("routerOutputs") is not None:
        import capo_mediaconnect.types.listed_router_output_list

        out["router_outputs"] = (
            capo_mediaconnect.types.listed_router_output_list.deserialize_json(
                data["routerOutputs"]
            )
        )
    else:
        out["router_outputs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
