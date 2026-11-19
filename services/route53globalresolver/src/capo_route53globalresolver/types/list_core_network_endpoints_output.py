"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListCoreNetworkEndpointsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.core_network_endpoints


class ListCoreNetworkEndpointsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    core_network_endpoints: (
        "capo_route53globalresolver.types.core_network_endpoints.CoreNetworkEndpoints"
    )
    """<p>An array of information about the core network endpoints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkEndpointsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_route53globalresolver.types.core_network_endpoints

    out["coreNetworkEndpoints"] = (
        capo_route53globalresolver.types.core_network_endpoints.serialize_json(
            value["core_network_endpoints"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCoreNetworkEndpointsOutput:
    out: ListCoreNetworkEndpointsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("coreNetworkEndpoints") is not None:
        import capo_route53globalresolver.types.core_network_endpoints

        out["core_network_endpoints"] = (
            capo_route53globalresolver.types.core_network_endpoints.deserialize_json(
                data["coreNetworkEndpoints"]
            )
        )
    else:
        out["core_network_endpoints"] = []
    return out
