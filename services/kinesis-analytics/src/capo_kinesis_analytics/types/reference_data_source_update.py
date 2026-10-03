"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ReferenceDataSourceUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.id
    import capo_kinesis_analytics.types.in_app_table_name
    import capo_kinesis_analytics.types.s3_reference_data_source_update
    import capo_kinesis_analytics.types.source_schema


class ReferenceDataSourceUpdate(TypedDict, closed=True):
    reference_id: "capo_kinesis_analytics.types.id.Id"
    """<p>ID of the reference data source being updated. You can use the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html">DescribeApplication</a> operation to get this value.</p>"""
    table_name_update: NotRequired[
        "capo_kinesis_analytics.types.in_app_table_name.InAppTableName"
    ]
    """<p>In-application table name that is created by this update.</p>"""
    s3_reference_data_source_update: NotRequired[
        "capo_kinesis_analytics.types.s3_reference_data_source_update.S3ReferenceDataSourceUpdate"
    ]
    """<p>Describes the S3 bucket name, object key name, and IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.</p>"""
    reference_schema_update: NotRequired[
        "capo_kinesis_analytics.types.source_schema.SourceSchema"
    ]
    """<p>Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSourceUpdate) -> dict:
    out: dict = {}
    out["ReferenceId"] = value["reference_id"]
    if "table_name_update" in value:
        out["TableNameUpdate"] = value["table_name_update"]
    if "s3_reference_data_source_update" in value:
        import capo_kinesis_analytics.types.s3_reference_data_source_update

        out["S3ReferenceDataSourceUpdate"] = (
            capo_kinesis_analytics.types.s3_reference_data_source_update.serialize_aws_json_1_1(
                value["s3_reference_data_source_update"]
            )
        )
    if "reference_schema_update" in value:
        import capo_kinesis_analytics.types.source_schema

        out["ReferenceSchemaUpdate"] = (
            capo_kinesis_analytics.types.source_schema.serialize_aws_json_1_1(
                value["reference_schema_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferenceDataSourceUpdate:
    out: ReferenceDataSourceUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ReferenceId") is not None:
        out["reference_id"] = data["ReferenceId"]
    else:
        raise DeserializationError("ReferenceDataSourceUpdate.reference_id required")
    if data.get("TableNameUpdate") is not None:
        out["table_name_update"] = data["TableNameUpdate"]
    if data.get("S3ReferenceDataSourceUpdate") is not None:
        import capo_kinesis_analytics.types.s3_reference_data_source_update

        out["s3_reference_data_source_update"] = (
            capo_kinesis_analytics.types.s3_reference_data_source_update.deserialize_aws_json_1_1(
                data["S3ReferenceDataSourceUpdate"]
            )
        )
    if data.get("ReferenceSchemaUpdate") is not None:
        import capo_kinesis_analytics.types.source_schema

        out["reference_schema_update"] = (
            capo_kinesis_analytics.types.source_schema.deserialize_aws_json_1_1(
                data["ReferenceSchemaUpdate"]
            )
        )
    return out
