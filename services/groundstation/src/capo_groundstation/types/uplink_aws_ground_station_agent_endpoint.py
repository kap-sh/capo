"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkAwsGroundStationAgentEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.uplink_dataflow_details


class UplinkAwsGroundStationAgentEndpoint(TypedDict, closed=True):
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>Uplink dataflow endpoint name</p>"""
    dataflow_details: (
        "capo_groundstation.types.uplink_dataflow_details.UplinkDataflowDetails"
    )
    """<p>Dataflow details for the uplink endpoint</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UplinkAwsGroundStationAgentEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_groundstation.types.uplink_dataflow_details

    out["dataflowDetails"] = (
        capo_groundstation.types.uplink_dataflow_details.serialize_json(
            value["dataflow_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> UplinkAwsGroundStationAgentEndpoint:
    out: UplinkAwsGroundStationAgentEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dataflowDetails") is not None:
        import capo_groundstation.types.uplink_dataflow_details

        out["dataflow_details"] = (
            capo_groundstation.types.uplink_dataflow_details.deserialize_json(
                data["dataflowDetails"]
            )
        )
    else:
        import capo_groundstation.types._unknown

        out["dataflow_details"] = capo_groundstation.types._unknown.UnknownUnionMember(
            ""
        )
    return out
