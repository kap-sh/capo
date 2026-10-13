"""Generated from Smithy shape ``com.amazonaws.drs#SourceServer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.agent_version
    import capo_drs.types.arn
    import capo_drs.types.data_replication_info
    import capo_drs.types.last_launch_result
    import capo_drs.types.life_cycle
    import capo_drs.types.recovery_instance_id
    import capo_drs.types.replication_direction
    import capo_drs.types.source_cloud_properties
    import capo_drs.types.source_network_id
    import capo_drs.types.source_properties
    import capo_drs.types.source_server_arn
    import capo_drs.types.source_server_id
    import capo_drs.types.staging_area
    import capo_drs.types.tags_map


class SourceServer(TypedDict, closed=True):
    source_server_id: NotRequired["capo_drs.types.source_server_id.SourceServerID"]
    """<p>The ID of the Source Server.</p>"""
    arn: NotRequired["capo_drs.types.arn.ARN"]
    """<p>The ARN of the Source Server.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>The tags associated with the Source Server.</p>"""
    recovery_instance_id: NotRequired[
        "capo_drs.types.recovery_instance_id.RecoveryInstanceID"
    ]
    """<p>The ID of the Recovery Instance associated with this Source Server.</p>"""
    last_launch_result: NotRequired[
        "capo_drs.types.last_launch_result.LastLaunchResult"
    ]
    """<p>The status of the last recovery launch of this Source Server.</p>"""
    data_replication_info: NotRequired[
        "capo_drs.types.data_replication_info.DataReplicationInfo"
    ]
    """<p>The Data Replication Info of the Source Server.</p>"""
    life_cycle: NotRequired["capo_drs.types.life_cycle.LifeCycle"]
    """<p>The lifecycle information of this Source Server.</p>"""
    source_properties: NotRequired["capo_drs.types.source_properties.SourceProperties"]
    """<p>The source properties of the Source Server.</p>"""
    staging_area: NotRequired["capo_drs.types.staging_area.StagingArea"]
    """<p>The staging area of the source server.</p>"""
    source_cloud_properties: NotRequired[
        "capo_drs.types.source_cloud_properties.SourceCloudProperties"
    ]
    """<p>Source cloud properties of the Source Server.</p>"""
    replication_direction: NotRequired[
        "capo_drs.types.replication_direction.ReplicationDirection"
    ]
    """<p>Replication direction of the Source Server.</p>"""
    reversed_direction_source_server_arn: NotRequired[
        "capo_drs.types.source_server_arn.SourceServerARN"
    ]
    """<p>For EC2-originated Source Servers which have been failed over and then failed back, this value will mean the ARN of the Source Server on the opposite replication direction.</p>"""
    source_network_id: NotRequired["capo_drs.types.source_network_id.SourceNetworkID"]
    """<p>ID of the Source Network which is protecting this Source Server's network.</p>"""
    agent_version: NotRequired["capo_drs.types.agent_version.AgentVersion"]
    """<p>The version of the DRS agent installed on the source server</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceServer) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    if "recovery_instance_id" in value:
        out["recoveryInstanceId"] = value["recovery_instance_id"]
    if "last_launch_result" in value:
        out["lastLaunchResult"] = value["last_launch_result"]
    if "data_replication_info" in value:
        import capo_drs.types.data_replication_info

        out["dataReplicationInfo"] = (
            capo_drs.types.data_replication_info.serialize_json(
                value["data_replication_info"]
            )
        )
    if "life_cycle" in value:
        import capo_drs.types.life_cycle

        out["lifeCycle"] = capo_drs.types.life_cycle.serialize_json(value["life_cycle"])
    if "source_properties" in value:
        import capo_drs.types.source_properties

        out["sourceProperties"] = capo_drs.types.source_properties.serialize_json(
            value["source_properties"]
        )
    if "staging_area" in value:
        import capo_drs.types.staging_area

        out["stagingArea"] = capo_drs.types.staging_area.serialize_json(
            value["staging_area"]
        )
    if "source_cloud_properties" in value:
        import capo_drs.types.source_cloud_properties

        out["sourceCloudProperties"] = (
            capo_drs.types.source_cloud_properties.serialize_json(
                value["source_cloud_properties"]
            )
        )
    if "replication_direction" in value:
        out["replicationDirection"] = value["replication_direction"]
    if "reversed_direction_source_server_arn" in value:
        out["reversedDirectionSourceServerArn"] = value[
            "reversed_direction_source_server_arn"
        ]
    if "source_network_id" in value:
        out["sourceNetworkID"] = value["source_network_id"]
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    return out


def deserialize_json(data: dict) -> SourceServer:
    out: SourceServer = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    if data.get("recoveryInstanceId") is not None:
        out["recovery_instance_id"] = data["recoveryInstanceId"]
    if data.get("lastLaunchResult") is not None:
        out["last_launch_result"] = data["lastLaunchResult"]
    if data.get("dataReplicationInfo") is not None:
        import capo_drs.types.data_replication_info

        out["data_replication_info"] = (
            capo_drs.types.data_replication_info.deserialize_json(
                data["dataReplicationInfo"]
            )
        )
    if data.get("lifeCycle") is not None:
        import capo_drs.types.life_cycle

        out["life_cycle"] = capo_drs.types.life_cycle.deserialize_json(
            data["lifeCycle"]
        )
    if data.get("sourceProperties") is not None:
        import capo_drs.types.source_properties

        out["source_properties"] = capo_drs.types.source_properties.deserialize_json(
            data["sourceProperties"]
        )
    if data.get("stagingArea") is not None:
        import capo_drs.types.staging_area

        out["staging_area"] = capo_drs.types.staging_area.deserialize_json(
            data["stagingArea"]
        )
    if data.get("sourceCloudProperties") is not None:
        import capo_drs.types.source_cloud_properties

        out["source_cloud_properties"] = (
            capo_drs.types.source_cloud_properties.deserialize_json(
                data["sourceCloudProperties"]
            )
        )
    if data.get("replicationDirection") is not None:
        out["replication_direction"] = data["replicationDirection"]
    if data.get("reversedDirectionSourceServerArn") is not None:
        out["reversed_direction_source_server_arn"] = data[
            "reversedDirectionSourceServerArn"
        ]
    if data.get("sourceNetworkID") is not None:
        out["source_network_id"] = data["sourceNetworkID"]
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    return out


def redact_sensitive(value: SourceServer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
