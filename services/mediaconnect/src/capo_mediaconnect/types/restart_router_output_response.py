"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RestartRouterOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_arn
    import capo_mediaconnect.types.router_output_state


class RestartRouterOutputResponse(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The ARN of the router output that was restarted.</p>"""
    name: "str"
    """<p>The name of the router output that was restarted.</p>"""
    state: "capo_mediaconnect.types.router_output_state.RouterOutputState"
    """<p>The current state of the router output after the restart operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestartRouterOutputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_output_state

    out["state"] = capo_mediaconnect.types.router_output_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> RestartRouterOutputResponse:
    out: RestartRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("state") is not None:
        import capo_mediaconnect.types.router_output_state

        out["state"] = capo_mediaconnect.types.router_output_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_mediaconnect.types.router_output_state.RouterOutputState", ""
        )
    return out
