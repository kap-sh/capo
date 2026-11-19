"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeContainerGroupPortMappingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_name_or_arn
    import capo_gamelift.types.container_group_type
    import capo_gamelift.types.container_name_query_filter
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.instance_id


class DescribeContainerGroupPortMappingsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the container fleet. You can use either the fleet ID or ARN value.</p>"""
    container_group_type: NotRequired[
        "capo_gamelift.types.container_group_type.ContainerGroupType"
    ]
    """<p>The type of container group to retrieve port mappings for.</p> <ul> <li> <p> <code>GAME_SERVER</code> -- Get port mappings for a game server container group.</p> </li> <li> <p> <code>PER_INSTANCE</code> -- Get port mappings for a per-instance container group.</p> </li> </ul>"""
    compute_name: NotRequired[
        "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
    ]
    """<p>A unique identifier for the compute resource for which to retrieve port mappings. For a container fleet, a compute represents a game server container group running on a fleet instance. You can use either the compute name or ARN value.</p> <p>When <code>ContainerGroupType</code> is <code>GAME_SERVER</code>, this parameter is required.</p> <p>When <code>ContainerGroupType</code> is <code>PER_INSTANCE</code>, do not provide this parameter. If you provide a compute name with <code>PER_INSTANCE</code>, the request fails with an <code>InvalidRequestException</code>.</p>"""
    instance_id: NotRequired["capo_gamelift.types.instance_id.InstanceId"]
    """<p>A unique identifier for the fleet instance to retrieve port mappings for.</p> <p>When <code>ContainerGroupType</code> is <code>PER_INSTANCE</code>, this parameter is required.</p> <p>When <code>ContainerGroupType</code> is <code>GAME_SERVER</code>, this parameter is optional. If you provide an instance ID, it must match the instance that's running the specified compute. If the instance ID doesn't match, the request fails with an <code>InvalidRequestException</code>.</p>"""
    container_name: NotRequired[
        "capo_gamelift.types.container_name_query_filter.ContainerNameQueryFilter"
    ]
    """<p>A container name to filter the results. When provided, the operation returns port mappings for the specified container only. If no container with the specified name exists in the container group, the request fails with a <code>NotFoundException</code>.</p> <p>If not provided, the operation returns port mappings for all containers in the container group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerGroupPortMappingsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "container_group_type" in value:
        import capo_gamelift.types.container_group_type

        out["ContainerGroupType"] = (
            capo_gamelift.types.container_group_type.serialize_aws_json_1_1(
                value["container_group_type"]
            )
        )
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerGroupPortMappingsInput:
    out: DescribeContainerGroupPortMappingsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ContainerGroupType") is not None:
        import capo_gamelift.types.container_group_type

        out["container_group_type"] = (
            capo_gamelift.types.container_group_type.deserialize_aws_json_1_1(
                data["ContainerGroupType"]
            )
        )
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ContainerName") is not None:
        out["container_name"] = data["ContainerName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeContainerGroupPortMappingsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "container_group_type" in value:
        import capo_gamelift.types.container_group_type

        out["ContainerGroupType"] = (
            capo_gamelift.types.container_group_type.serialize_cbor(
                value["container_group_type"]
            )
        )
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    return out


def deserialize_cbor(data: dict) -> DescribeContainerGroupPortMappingsInput:
    out: DescribeContainerGroupPortMappingsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ContainerGroupType") is not None:
        import capo_gamelift.types.container_group_type

        out["container_group_type"] = (
            capo_gamelift.types.container_group_type.deserialize_cbor(
                data["ContainerGroupType"]
            )
        )
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ContainerName") is not None:
        out["container_name"] = data["ContainerName"]
    return out
