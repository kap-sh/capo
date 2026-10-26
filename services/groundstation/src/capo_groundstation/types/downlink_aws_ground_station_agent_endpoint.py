"""Generated from Smithy shape ``com.amazonaws.groundstation#DownlinkAwsGroundStationAgentEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.downlink_dataflow_details
    import capo_groundstation.types.safe_name


class DownlinkAwsGroundStationAgentEndpoint(TypedDict, closed=True):
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>Downlink dataflow endpoint name</p>"""
    dataflow_details: (
        "capo_groundstation.types.downlink_dataflow_details.DownlinkDataflowDetails"
    )
    """<p>Dataflow details for the downlink endpoint</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkAwsGroundStationAgentEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_groundstation.types.downlink_dataflow_details

    out["dataflowDetails"] = (
        capo_groundstation.types.downlink_dataflow_details.serialize_json(
            value["dataflow_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> DownlinkAwsGroundStationAgentEndpoint:
    out: DownlinkAwsGroundStationAgentEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dataflowDetails") is not None:
        import capo_groundstation.types.downlink_dataflow_details

        out["dataflow_details"] = (
            capo_groundstation.types.downlink_dataflow_details.deserialize_json(
                data["dataflowDetails"]
            )
        )
    else:
        out["dataflow_details"] = {"$unknown": {"name": ""}}
    return out
