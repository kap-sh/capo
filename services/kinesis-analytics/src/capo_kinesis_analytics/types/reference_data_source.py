"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ReferenceDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.in_app_table_name
    import capo_kinesis_analytics.types.s3_reference_data_source
    import capo_kinesis_analytics.types.source_schema


class ReferenceDataSource(TypedDict, closed=True):
    table_name: "capo_kinesis_analytics.types.in_app_table_name.InAppTableName"
    """<p>Name of the in-application table to create.</p>"""
    s3_reference_data_source: NotRequired[
        "capo_kinesis_analytics.types.s3_reference_data_source.S3ReferenceDataSource"
    ]
    """<p>Identifies the S3 bucket and object that contains the reference data. Also identifies the IAM role Amazon Kinesis Analytics can assume to read this object on your behalf. An Amazon Kinesis Analytics application loads reference data only once. If the data changes, you call the <code>UpdateApplication</code> operation to trigger reloading of data into your application. </p>"""
    reference_schema: "capo_kinesis_analytics.types.source_schema.SourceSchema"
    """<p>Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSource) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    if "s3_reference_data_source" in value:
        import capo_kinesis_analytics.types.s3_reference_data_source

        out["S3ReferenceDataSource"] = (
            capo_kinesis_analytics.types.s3_reference_data_source.serialize_aws_json_1_1(
                value["s3_reference_data_source"]
            )
        )
    import capo_kinesis_analytics.types.source_schema

    out["ReferenceSchema"] = (
        capo_kinesis_analytics.types.source_schema.serialize_aws_json_1_1(
            value["reference_schema"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferenceDataSource:
    out: ReferenceDataSource = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("S3ReferenceDataSource") is not None:
        import capo_kinesis_analytics.types.s3_reference_data_source

        out["s3_reference_data_source"] = (
            capo_kinesis_analytics.types.s3_reference_data_source.deserialize_aws_json_1_1(
                data["S3ReferenceDataSource"]
            )
        )
    if data.get("ReferenceSchema") is not None:
        import capo_kinesis_analytics.types.source_schema

        out["reference_schema"] = (
            capo_kinesis_analytics.types.source_schema.deserialize_aws_json_1_1(
                data["ReferenceSchema"]
            )
        )
    else:
        raise DeserializationError("ReferenceDataSource.reference_schema required")
    return out
