"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListRouterInputsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_router_input_list


class ListRouterInputsResponse(TypedDict, closed=True):
    router_inputs: (
        "capo_mediaconnect.types.listed_router_input_list.ListedRouterInputList"
    )
    """<p>The summary information for the retrieved router inputs.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRouterInputsResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.listed_router_input_list

    out["routerInputs"] = (
        capo_mediaconnect.types.listed_router_input_list.serialize_json(
            value["router_inputs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRouterInputsResponse:
    out: ListRouterInputsResponse = {}  # type: ignore[typeddict-item]
    if data.get("routerInputs") is not None:
        import capo_mediaconnect.types.listed_router_input_list

        out["router_inputs"] = (
            capo_mediaconnect.types.listed_router_input_list.deserialize_json(
                data["routerInputs"]
            )
        )
    else:
        out["router_inputs"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
