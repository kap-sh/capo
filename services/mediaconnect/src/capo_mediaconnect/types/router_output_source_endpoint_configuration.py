"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputSourceEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_arn


class RouterOutputSourceEndpointConfiguration(TypedDict, closed=True):
    router_output_arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that the source endpoint represents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputSourceEndpointConfiguration) -> dict:
    out: dict = {}
    out["routerOutputArn"] = value["router_output_arn"]
    return out


def deserialize_json(data: dict) -> RouterOutputSourceEndpointConfiguration:
    out: RouterOutputSourceEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("routerOutputArn") is not None:
        out["router_output_arn"] = data["routerOutputArn"]
    else:
        out["router_output_arn"] = ""
    return out
