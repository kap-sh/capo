"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputDestinationEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn


class RouterInputDestinationEndpointConfiguration(TypedDict, closed=True):
    router_input_arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input that the destination endpoint represents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputDestinationEndpointConfiguration) -> dict:
    out: dict = {}
    out["routerInputArn"] = value["router_input_arn"]
    return out


def deserialize_json(data: dict) -> RouterInputDestinationEndpointConfiguration:
    out: RouterInputDestinationEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("routerInputArn") is not None:
        out["router_input_arn"] = data["routerInputArn"]
    else:
        out["router_input_arn"] = ""
    return out
