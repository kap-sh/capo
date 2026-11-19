"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.configuration_summary
    import capo_observabilityadmin.types.resource_arn
    import capo_observabilityadmin.types.source_progress
    import capo_observabilityadmin.types.tag_map_output
    import capo_observabilityadmin.types.telemetry_pipeline_configuration
    import capo_observabilityadmin.types.telemetry_pipeline_name
    import capo_observabilityadmin.types.telemetry_pipeline_status
    import capo_observabilityadmin.types.telemetry_pipeline_status_reason


class TelemetryPipeline(TypedDict, closed=True):
    created_time_stamp: NotRequired["int"]
    """<p>The timestamp when the telemetry pipeline was created.</p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p>The timestamp when the telemetry pipeline was last updated.</p>"""
    arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the telemetry pipeline.</p>"""
    name: NotRequired[
        "capo_observabilityadmin.types.telemetry_pipeline_name.TelemetryPipelineName"
    ]
    """<p>The name of the telemetry pipeline.</p>"""
    configuration: NotRequired[
        "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration"
    ]
    """<p>The configuration that defines how the telemetry pipeline processes data.</p>"""
    status: NotRequired[
        "capo_observabilityadmin.types.telemetry_pipeline_status.TelemetryPipelineStatus"
    ]
    """<p>The current status of the telemetry pipeline.</p>"""
    status_reason: NotRequired[
        "capo_observabilityadmin.types.telemetry_pipeline_status_reason.TelemetryPipelineStatusReason"
    ]
    """<p>Additional information about the pipeline status, including reasons for failure states.</p>"""
    tags: NotRequired["capo_observabilityadmin.types.tag_map_output.TagMapOutput"]
    """<p>The key-value pairs associated with the telemetry pipeline resource.</p>"""
    last_refresh_time_stamp: NotRequired["int"]
    """<p>The timestamp when the most recent refresh of the telemetry pipeline started. This field is only present for external-cloud pipelines that you have refreshed.</p>"""
    source_progress: NotRequired[
        "capo_observabilityadmin.types.source_progress.SourceProgress"
    ]
    """<p>The progress of source activation for the telemetry pipeline. This field is only present for external-cloud pipelines.</p>"""
    configuration_summary: NotRequired[
        "capo_observabilityadmin.types.configuration_summary.ConfigurationSummary"
    ]
    """<p>A summary of the pipeline configuration components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryPipeline) -> dict:
    out: dict = {}
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "configuration" in value:
        import capo_observabilityadmin.types.telemetry_pipeline_configuration

        out["Configuration"] = (
            capo_observabilityadmin.types.telemetry_pipeline_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "status" in value:
        import capo_observabilityadmin.types.telemetry_pipeline_status

        out["Status"] = (
            capo_observabilityadmin.types.telemetry_pipeline_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import capo_observabilityadmin.types.telemetry_pipeline_status_reason

        out["StatusReason"] = (
            capo_observabilityadmin.types.telemetry_pipeline_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "tags" in value:
        import capo_observabilityadmin.types.tag_map_output

        out["Tags"] = capo_observabilityadmin.types.tag_map_output.serialize_json(
            value["tags"]
        )
    if "last_refresh_time_stamp" in value:
        out["LastRefreshTimeStamp"] = value["last_refresh_time_stamp"]
    if "source_progress" in value:
        import capo_observabilityadmin.types.source_progress

        out["SourceProgress"] = (
            capo_observabilityadmin.types.source_progress.serialize_json(
                value["source_progress"]
            )
        )
    if "configuration_summary" in value:
        import capo_observabilityadmin.types.configuration_summary

        out["ConfigurationSummary"] = (
            capo_observabilityadmin.types.configuration_summary.serialize_json(
                value["configuration_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryPipeline:
    out: TelemetryPipeline = {}  # type: ignore[typeddict-item]
    if data.get("CreatedTimeStamp") is not None:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    if data.get("LastUpdateTimeStamp") is not None:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Configuration") is not None:
        import capo_observabilityadmin.types.telemetry_pipeline_configuration

        out["configuration"] = (
            capo_observabilityadmin.types.telemetry_pipeline_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("Status") is not None:
        import capo_observabilityadmin.types.telemetry_pipeline_status

        out["status"] = (
            capo_observabilityadmin.types.telemetry_pipeline_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        import capo_observabilityadmin.types.telemetry_pipeline_status_reason

        out["status_reason"] = (
            capo_observabilityadmin.types.telemetry_pipeline_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.tag_map_output

        out["tags"] = capo_observabilityadmin.types.tag_map_output.deserialize_json(
            data["Tags"]
        )
    if data.get("LastRefreshTimeStamp") is not None:
        out["last_refresh_time_stamp"] = data["LastRefreshTimeStamp"]
    if data.get("SourceProgress") is not None:
        import capo_observabilityadmin.types.source_progress

        out["source_progress"] = (
            capo_observabilityadmin.types.source_progress.deserialize_json(
                data["SourceProgress"]
            )
        )
    if data.get("ConfigurationSummary") is not None:
        import capo_observabilityadmin.types.configuration_summary

        out["configuration_summary"] = (
            capo_observabilityadmin.types.configuration_summary.deserialize_json(
                data["ConfigurationSummary"]
            )
        )
    return out
