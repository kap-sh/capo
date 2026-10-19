"""Generated from Smithy shape ``com.amazonaws.internetmonitor#NetworkImpairment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.network_list
    import capo_internetmonitor.types.triangulation_event_type


class NetworkImpairment(TypedDict, closed=True):
    networks: "capo_internetmonitor.types.network_list.NetworkList"
    """<p>The networks that could be impacted by a network impairment event.</p>"""
    as_path: "capo_internetmonitor.types.network_list.NetworkList"
    """<p>The combination of the Autonomous System Number (ASN) of the network and the name of the network.</p>"""
    network_event_type: (
        "capo_internetmonitor.types.triangulation_event_type.TriangulationEventType"
    )
    """<p>The type of network impairment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkImpairment) -> dict:
    out: dict = {}
    import capo_internetmonitor.types.network_list

    out["Networks"] = capo_internetmonitor.types.network_list.serialize_json(
        value["networks"]
    )
    import capo_internetmonitor.types.network_list

    out["AsPath"] = capo_internetmonitor.types.network_list.serialize_json(
        value["as_path"]
    )
    out["NetworkEventType"] = value["network_event_type"]
    return out


def deserialize_json(data: dict) -> NetworkImpairment:
    out: NetworkImpairment = {}  # type: ignore[typeddict-item]
    if data.get("Networks") is not None:
        import capo_internetmonitor.types.network_list

        out["networks"] = capo_internetmonitor.types.network_list.deserialize_json(
            data["Networks"]
        )
    else:
        out["networks"] = []
    if data.get("AsPath") is not None:
        import capo_internetmonitor.types.network_list

        out["as_path"] = capo_internetmonitor.types.network_list.deserialize_json(
            data["AsPath"]
        )
    else:
        out["as_path"] = []
    if data.get("NetworkEventType") is not None:
        out["network_event_type"] = data["NetworkEventType"]
    else:
        out["network_event_type"] = ""
    return out
