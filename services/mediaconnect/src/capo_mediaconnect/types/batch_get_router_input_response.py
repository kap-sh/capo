"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_router_input_error_list
    import capo_mediaconnect.types.router_input_list


class BatchGetRouterInputResponse(TypedDict, closed=True):
    router_inputs: "capo_mediaconnect.types.router_input_list.RouterInputList"
    """<p>An array of router inputs that were successfully retrieved.</p>"""
    errors: "capo_mediaconnect.types.batch_get_router_input_error_list.BatchGetRouterInputErrorList"
    """<p>An array of errors that occurred when retrieving the requested router inputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterInputResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_input_list

    out["routerInputs"] = capo_mediaconnect.types.router_input_list.serialize_json(
        value["router_inputs"]
    )
    import capo_mediaconnect.types.batch_get_router_input_error_list

    out["errors"] = (
        capo_mediaconnect.types.batch_get_router_input_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetRouterInputResponse:
    out: BatchGetRouterInputResponse = {}  # type: ignore[typeddict-item]
    if data.get("routerInputs") is not None:
        import capo_mediaconnect.types.router_input_list

        out["router_inputs"] = (
            capo_mediaconnect.types.router_input_list.deserialize_json(
                data["routerInputs"]
            )
        )
    else:
        out["router_inputs"] = []
    if data.get("errors") is not None:
        import capo_mediaconnect.types.batch_get_router_input_error_list

        out["errors"] = (
            capo_mediaconnect.types.batch_get_router_input_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
