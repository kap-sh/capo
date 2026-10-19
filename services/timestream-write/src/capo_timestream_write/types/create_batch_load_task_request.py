"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#CreateBatchLoadTaskRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_write.types.client_request_token
    import capo_timestream_write.types.data_model_configuration
    import capo_timestream_write.types.data_source_configuration
    import capo_timestream_write.types.record_version
    import capo_timestream_write.types.report_configuration
    import capo_timestream_write.types.resource_create_api_name


class CreateBatchLoadTaskRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_timestream_write.types.client_request_token.ClientRequestToken"
    ]
    """<p></p>"""
    data_model_configuration: NotRequired[
        "capo_timestream_write.types.data_model_configuration.DataModelConfiguration"
    ]
    data_source_configuration: (
        "capo_timestream_write.types.data_source_configuration.DataSourceConfiguration"
    )
    """<p>Defines configuration details about the data source for a batch load task.</p>"""
    report_configuration: (
        "capo_timestream_write.types.report_configuration.ReportConfiguration"
    )
    target_database_name: (
        "capo_timestream_write.types.resource_create_api_name.ResourceCreateAPIName"
    )
    """<p>Target Timestream database for a batch load task.</p>"""
    target_table_name: (
        "capo_timestream_write.types.resource_create_api_name.ResourceCreateAPIName"
    )
    """<p>Target Timestream table for a batch load task.</p>"""
    record_version: NotRequired[
        "capo_timestream_write.types.record_version.RecordVersion"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBatchLoadTaskRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "data_model_configuration" in value:
        import capo_timestream_write.types.data_model_configuration

        out["DataModelConfiguration"] = (
            capo_timestream_write.types.data_model_configuration.serialize_aws_json_1_0(
                value["data_model_configuration"]
            )
        )
    import capo_timestream_write.types.data_source_configuration

    out["DataSourceConfiguration"] = (
        capo_timestream_write.types.data_source_configuration.serialize_aws_json_1_0(
            value["data_source_configuration"]
        )
    )
    import capo_timestream_write.types.report_configuration

    out["ReportConfiguration"] = (
        capo_timestream_write.types.report_configuration.serialize_aws_json_1_0(
            value["report_configuration"]
        )
    )
    out["TargetDatabaseName"] = value["target_database_name"]
    out["TargetTableName"] = value["target_table_name"]
    if "record_version" in value:
        out["RecordVersion"] = value["record_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBatchLoadTaskRequest:
    out: CreateBatchLoadTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("DataModelConfiguration") is not None:
        import capo_timestream_write.types.data_model_configuration

        out["data_model_configuration"] = (
            capo_timestream_write.types.data_model_configuration.deserialize_aws_json_1_0(
                data["DataModelConfiguration"]
            )
        )
    if data.get("DataSourceConfiguration") is not None:
        import capo_timestream_write.types.data_source_configuration

        out["data_source_configuration"] = (
            capo_timestream_write.types.data_source_configuration.deserialize_aws_json_1_0(
                data["DataSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBatchLoadTaskRequest.data_source_configuration required"
        )
    if data.get("ReportConfiguration") is not None:
        import capo_timestream_write.types.report_configuration

        out["report_configuration"] = (
            capo_timestream_write.types.report_configuration.deserialize_aws_json_1_0(
                data["ReportConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBatchLoadTaskRequest.report_configuration required"
        )
    if data.get("TargetDatabaseName") is not None:
        out["target_database_name"] = data["TargetDatabaseName"]
    else:
        out["target_database_name"] = ""
    if data.get("TargetTableName") is not None:
        out["target_table_name"] = data["TargetTableName"]
    else:
        out["target_table_name"] = ""
    if data.get("RecordVersion") is not None:
        out["record_version"] = data["RecordVersion"]
    return out


def redact_sensitive(value: CreateBatchLoadTaskRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    return out
