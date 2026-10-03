"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.export_data_formats
    import capo_application_discovery_service.types.export_filters
    import capo_application_discovery_service.types.export_preferences
    import capo_application_discovery_service.types.time_stamp


class StartExportTaskRequest(TypedDict, closed=True):
    export_data_format: NotRequired[
        "capo_application_discovery_service.types.export_data_formats.ExportDataFormats"
    ]
    """<p>The file format for the returned export data. Default value is <code>CSV</code>. <b>Note:</b> <i>The</i> <code>GRAPHML</code> <i>option has been deprecated.</i> </p>"""
    filters: NotRequired[
        "capo_application_discovery_service.types.export_filters.ExportFilters"
    ]
    """<p>If a filter is present, it selects the single <code>agentId</code> of the Application Discovery Agent for which data is exported. The <code>agentId</code> can be found in the results of the <code>DescribeAgents</code> API or CLI. If no filter is present, <code>startTime</code> and <code>endTime</code> are ignored and exported data includes both Amazon Web Services Application Discovery Service Agentless Collector collectors data and summary data from Application Discovery Agent agents. </p>"""
    start_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The start timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, data is exported starting from the first data collected by the agent.</p>"""
    end_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The end timestamp for exported data from the single Application Discovery Agent selected in the filters. If no value is specified, exported data includes the most recent data collected by the agent.</p>"""
    preferences: NotRequired[
        "capo_application_discovery_service.types.export_preferences.ExportPreferences"
    ]
    """<p> Indicates the type of data that needs to be exported. Only one <a href="https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportPreferences.html">ExportPreferences</a> can be enabled at any time. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartExportTaskRequest) -> dict:
    out: dict = {}
    if "export_data_format" in value:
        import capo_application_discovery_service.types.export_data_formats

        out["exportDataFormat"] = (
            capo_application_discovery_service.types.export_data_formats.serialize_aws_json_1_1(
                value["export_data_format"]
            )
        )
    if "filters" in value:
        import capo_application_discovery_service.types.export_filters

        out["filters"] = (
            capo_application_discovery_service.types.export_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "start_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["startTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["endTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "preferences" in value:
        import capo_application_discovery_service.types.export_preferences

        out["preferences"] = (
            capo_application_discovery_service.types.export_preferences.serialize_aws_json_1_1(
                value["preferences"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartExportTaskRequest:
    out: StartExportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("exportDataFormat") is not None:
        import capo_application_discovery_service.types.export_data_formats

        out["export_data_format"] = (
            capo_application_discovery_service.types.export_data_formats.deserialize_aws_json_1_1(
                data["exportDataFormat"]
            )
        )
    if data.get("filters") is not None:
        import capo_application_discovery_service.types.export_filters

        out["filters"] = (
            capo_application_discovery_service.types.export_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if data.get("startTime") is not None:
        import capo_application_discovery_service.types.time_stamp

        out["start_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_application_discovery_service.types.time_stamp

        out["end_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["endTime"]
            )
        )
    if data.get("preferences") is not None:
        import capo_application_discovery_service.types.export_preferences

        out["preferences"] = (
            capo_application_discovery_service.types.export_preferences.deserialize_aws_json_1_1(
                data["preferences"]
            )
        )
    return out
