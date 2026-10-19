"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_router_output_error_list
    import capo_mediaconnect.types.router_output_list


class BatchGetRouterOutputResponse(TypedDict, closed=True):
    router_outputs: "capo_mediaconnect.types.router_output_list.RouterOutputList"
    """<p>An array of router outputs that were successfully retrieved.</p>"""
    errors: "capo_mediaconnect.types.batch_get_router_output_error_list.BatchGetRouterOutputErrorList"
    """<p>An array of errors that occurred when retrieving the requested router outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterOutputResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_output_list

    out["routerOutputs"] = capo_mediaconnect.types.router_output_list.serialize_json(
        value["router_outputs"]
    )
    import capo_mediaconnect.types.batch_get_router_output_error_list

    out["errors"] = (
        capo_mediaconnect.types.batch_get_router_output_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetRouterOutputResponse:
    out: BatchGetRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if data.get("routerOutputs") is not None:
        import capo_mediaconnect.types.router_output_list

        out["router_outputs"] = (
            capo_mediaconnect.types.router_output_list.deserialize_json(
                data["routerOutputs"]
            )
        )
    else:
        out["router_outputs"] = []
    if data.get("errors") is not None:
        import capo_mediaconnect.types.batch_get_router_output_error_list

        out["errors"] = (
            capo_mediaconnect.types.batch_get_router_output_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
