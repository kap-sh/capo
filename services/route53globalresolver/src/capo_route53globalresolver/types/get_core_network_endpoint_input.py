"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetCoreNetworkEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id


class GetCoreNetworkEndpointInput(TypedDict, closed=True):
    core_network_endpoint_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the core network endpoint to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreNetworkEndpointInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCoreNetworkEndpointInput:
    out: GetCoreNetworkEndpointInput = {}  # type: ignore[typeddict-item]
    return out
