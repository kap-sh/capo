"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeEdgeConfigurationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.edge_agent_status
    import capo_kinesis_video.types.edge_config
    import capo_kinesis_video.types.failed_status_details
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name
    import capo_kinesis_video.types.sync_status
    import capo_kinesis_video.types.timestamp


class DescribeEdgeConfigurationOutput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream from which the edge configuration was updated.</p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""
    creation_time: NotRequired["capo_kinesis_video.types.timestamp.Timestamp"]
    """<p>The timestamp at which a stream’s edge configuration was first created.</p>"""
    last_updated_time: NotRequired["capo_kinesis_video.types.timestamp.Timestamp"]
    """<p>The timestamp at which a stream’s edge configuration was last updated.</p>"""
    sync_status: NotRequired["capo_kinesis_video.types.sync_status.SyncStatus"]
    """<p>The latest status of the edge configuration update.</p>"""
    failed_status_details: NotRequired[
        "capo_kinesis_video.types.failed_status_details.FailedStatusDetails"
    ]
    """<p>A description of the generated failure status.</p>"""
    edge_config: NotRequired["capo_kinesis_video.types.edge_config.EdgeConfig"]
    """<p>A description of the stream's edge configuration that will be used to sync with the Edge Agent IoT Greengrass component. The Edge Agent component will run on an IoT Hub Device setup at your premise.</p>"""
    edge_agent_status: NotRequired[
        "capo_kinesis_video.types.edge_agent_status.EdgeAgentStatus"
    ]
    """<p>An object that contains the latest status details for an edge agent's recorder and uploader jobs. Use this information to determine the current health of an edge agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEdgeConfigurationOutput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "creation_time" in value:
        import capo_kinesis_video.types.timestamp

        out["CreationTime"] = capo_kinesis_video.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_kinesis_video.types.timestamp

        out["LastUpdatedTime"] = capo_kinesis_video.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "sync_status" in value:
        import capo_kinesis_video.types.sync_status

        out["SyncStatus"] = capo_kinesis_video.types.sync_status.serialize_json(
            value["sync_status"]
        )
    if "failed_status_details" in value:
        out["FailedStatusDetails"] = value["failed_status_details"]
    if "edge_config" in value:
        import capo_kinesis_video.types.edge_config

        out["EdgeConfig"] = capo_kinesis_video.types.edge_config.serialize_json(
            value["edge_config"]
        )
    if "edge_agent_status" in value:
        import capo_kinesis_video.types.edge_agent_status

        out["EdgeAgentStatus"] = (
            capo_kinesis_video.types.edge_agent_status.serialize_json(
                value["edge_agent_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeEdgeConfigurationOutput:
    out: DescribeEdgeConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("CreationTime") is not None:
        import capo_kinesis_video.types.timestamp

        out["creation_time"] = capo_kinesis_video.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_kinesis_video.types.timestamp

        out["last_updated_time"] = capo_kinesis_video.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("SyncStatus") is not None:
        import capo_kinesis_video.types.sync_status

        out["sync_status"] = capo_kinesis_video.types.sync_status.deserialize_json(
            data["SyncStatus"]
        )
    if data.get("FailedStatusDetails") is not None:
        out["failed_status_details"] = data["FailedStatusDetails"]
    if data.get("EdgeConfig") is not None:
        import capo_kinesis_video.types.edge_config

        out["edge_config"] = capo_kinesis_video.types.edge_config.deserialize_json(
            data["EdgeConfig"]
        )
    if data.get("EdgeAgentStatus") is not None:
        import capo_kinesis_video.types.edge_agent_status

        out["edge_agent_status"] = (
            capo_kinesis_video.types.edge_agent_status.deserialize_json(
                data["EdgeAgentStatus"]
            )
        )
    return out


def redact_sensitive(value: DescribeEdgeConfigurationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "edge_config" in value:
        import capo_kinesis_video.types.edge_config

        out["edge_config"] = capo_kinesis_video.types.edge_config.redact_sensitive(
            value["edge_config"]
        )
    return out
