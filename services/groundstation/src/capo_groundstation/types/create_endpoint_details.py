"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.downlink_aws_ground_station_agent_endpoint
    import capo_groundstation.types.uplink_aws_ground_station_agent_endpoint


class _CreateEndpointDetails_uplinkAwsGroundStationAgentEndpoint(
    TypedDict, closed=True
):
    uplinkAwsGroundStationAgentEndpoint: "capo_groundstation.types.uplink_aws_ground_station_agent_endpoint.UplinkAwsGroundStationAgentEndpoint"


class _CreateEndpointDetails_downlinkAwsGroundStationAgentEndpoint(
    TypedDict, closed=True
):
    downlinkAwsGroundStationAgentEndpoint: "capo_groundstation.types.downlink_aws_ground_station_agent_endpoint.DownlinkAwsGroundStationAgentEndpoint"


CreateEndpointDetails: TypeAlias = (
    _CreateEndpointDetails_uplinkAwsGroundStationAgentEndpoint
    | _CreateEndpointDetails_downlinkAwsGroundStationAgentEndpoint
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CreateEndpointDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CreateEndpointDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "uplinkAwsGroundStationAgentEndpoint" in value:
        import capo_groundstation.types.uplink_aws_ground_station_agent_endpoint

        return {
            "uplinkAwsGroundStationAgentEndpoint": capo_groundstation.types.uplink_aws_ground_station_agent_endpoint.serialize_json(
                value["uplinkAwsGroundStationAgentEndpoint"]
            )
        }
    elif "downlinkAwsGroundStationAgentEndpoint" in value:
        import capo_groundstation.types.downlink_aws_ground_station_agent_endpoint

        return {
            "downlinkAwsGroundStationAgentEndpoint": capo_groundstation.types.downlink_aws_ground_station_agent_endpoint.serialize_json(
                value["downlinkAwsGroundStationAgentEndpoint"]
            )
        }
    else:
        raise SerializationError("CreateEndpointDetails: no variant present")


def deserialize_json(data: dict) -> CreateEndpointDetails:
    if data.get("uplinkAwsGroundStationAgentEndpoint") is not None:
        import capo_groundstation.types.uplink_aws_ground_station_agent_endpoint

        return {
            "uplinkAwsGroundStationAgentEndpoint": capo_groundstation.types.uplink_aws_ground_station_agent_endpoint.deserialize_json(
                data["uplinkAwsGroundStationAgentEndpoint"]
            )
        }
    elif data.get("downlinkAwsGroundStationAgentEndpoint") is not None:
        import capo_groundstation.types.downlink_aws_ground_station_agent_endpoint

        return {
            "downlinkAwsGroundStationAgentEndpoint": capo_groundstation.types.downlink_aws_ground_station_agent_endpoint.deserialize_json(
                data["downlinkAwsGroundStationAgentEndpoint"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CreateEndpointDetails: no recognized variant key")
