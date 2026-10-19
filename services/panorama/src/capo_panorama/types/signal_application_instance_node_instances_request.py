"""Generated from Smithy shape ``com.amazonaws.panorama#SignalApplicationInstanceNodeInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.application_instance_id
    import capo_panorama.types.node_signal_list


class SignalApplicationInstanceNodeInstancesRequest(TypedDict, closed=True):
    application_instance_id: (
        "capo_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>An application instance ID.</p>"""
    node_signals: "capo_panorama.types.node_signal_list.NodeSignalList"
    """<p>A list of signals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignalApplicationInstanceNodeInstancesRequest) -> dict:
    out: dict = {}
    import capo_panorama.types.node_signal_list

    out["NodeSignals"] = capo_panorama.types.node_signal_list.serialize_json(
        value["node_signals"]
    )
    return out


def deserialize_json(data: dict) -> SignalApplicationInstanceNodeInstancesRequest:
    out: SignalApplicationInstanceNodeInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NodeSignals") is not None:
        import capo_panorama.types.node_signal_list

        out["node_signals"] = capo_panorama.types.node_signal_list.deserialize_json(
            data["NodeSignals"]
        )
    else:
        out["node_signals"] = []
    return out
