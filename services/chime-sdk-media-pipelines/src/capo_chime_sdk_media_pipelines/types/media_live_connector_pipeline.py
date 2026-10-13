"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaLiveConnectorPipeline``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.amazon_resource_name
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.iso8601_timestamp
    import capo_chime_sdk_media_pipelines.types.live_connector_sink_list
    import capo_chime_sdk_media_pipelines.types.live_connector_source_list
    import capo_chime_sdk_media_pipelines.types.media_pipeline_status


class MediaLiveConnectorPipeline(TypedDict, closed=True):
    sources: NotRequired[
        "capo_chime_sdk_media_pipelines.types.live_connector_source_list.LiveConnectorSourceList"
    ]
    """<p>The connector pipeline's data sources.</p>"""
    sinks: NotRequired[
        "capo_chime_sdk_media_pipelines.types.live_connector_sink_list.LiveConnectorSinkList"
    ]
    """<p>The connector pipeline's data sinks.</p>"""
    media_pipeline_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The connector pipeline's ID.</p>"""
    media_pipeline_arn: NotRequired[
        "capo_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The connector pipeline's ARN.</p>"""
    status: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline_status.MediaPipelineStatus"
    ]
    """<p>The connector pipeline's status.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the connector pipeline was created.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the connector pipeline was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveConnectorPipeline) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_chime_sdk_media_pipelines.types.live_connector_source_list

        out["Sources"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_source_list.serialize_json(
                value["sources"]
            )
        )
    if "sinks" in value:
        import capo_chime_sdk_media_pipelines.types.live_connector_sink_list

        out["Sinks"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_sink_list.serialize_json(
                value["sinks"]
            )
        )
    if "media_pipeline_id" in value:
        out["MediaPipelineId"] = value["media_pipeline_id"]
    if "media_pipeline_arn" in value:
        out["MediaPipelineArn"] = value["media_pipeline_arn"]
    if "status" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_status

        out["Status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_status.serialize_json(
                value["status"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaLiveConnectorPipeline:
    out: MediaLiveConnectorPipeline = {}  # type: ignore[typeddict-item]
    if data.get("Sources") is not None:
        import capo_chime_sdk_media_pipelines.types.live_connector_source_list

        out["sources"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_source_list.deserialize_json(
                data["Sources"]
            )
        )
    if data.get("Sinks") is not None:
        import capo_chime_sdk_media_pipelines.types.live_connector_sink_list

        out["sinks"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_sink_list.deserialize_json(
                data["Sinks"]
            )
        )
    if data.get("MediaPipelineId") is not None:
        out["media_pipeline_id"] = data["MediaPipelineId"]
    if data.get("MediaPipelineArn") is not None:
        out["media_pipeline_arn"] = data["MediaPipelineArn"]
    if data.get("Status") is not None:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_status

        out["status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    return out


def redact_sensitive(value: MediaLiveConnectorPipeline) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sources" in value:
        import capo_chime_sdk_media_pipelines.types.live_connector_source_list

        out["sources"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_source_list.redact_sensitive(
                value["sources"]
            )
        )
    if "sinks" in value:
        import capo_chime_sdk_media_pipelines.types.live_connector_sink_list

        out["sinks"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_sink_list.redact_sensitive(
                value["sinks"]
            )
        )
    return out
