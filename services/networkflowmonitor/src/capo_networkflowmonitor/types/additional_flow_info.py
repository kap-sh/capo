"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#AdditionalFlowInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.client_location
    import capo_networkflowmonitor.types.network


class AdditionalFlowInfo(TypedDict, closed=True):
    network: NotRequired["capo_networkflowmonitor.types.network.Network"]
    """<p>The network that the remote address of the network flow belongs to.</p>"""
    client_location: NotRequired[
        "capo_networkflowmonitor.types.client_location.ClientLocation"
    ]
    """<p>The location of the client for the network flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalFlowInfo) -> dict:
    out: dict = {}
    if "network" in value:
        import capo_networkflowmonitor.types.network

        out["network"] = capo_networkflowmonitor.types.network.serialize_json(
            value["network"]
        )
    if "client_location" in value:
        import capo_networkflowmonitor.types.client_location

        out["clientLocation"] = (
            capo_networkflowmonitor.types.client_location.serialize_json(
                value["client_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdditionalFlowInfo:
    out: AdditionalFlowInfo = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        import capo_networkflowmonitor.types.network

        out["network"] = capo_networkflowmonitor.types.network.deserialize_json(
            data["network"]
        )
    if data.get("clientLocation") is not None:
        import capo_networkflowmonitor.types.client_location

        out["client_location"] = (
            capo_networkflowmonitor.types.client_location.deserialize_json(
                data["clientLocation"]
            )
        )
    return out
