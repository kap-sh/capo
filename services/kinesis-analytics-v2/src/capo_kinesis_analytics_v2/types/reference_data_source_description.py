"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ReferenceDataSourceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.id
    import capo_kinesis_analytics_v2.types.in_app_table_name
    import capo_kinesis_analytics_v2.types.s3_reference_data_source_description
    import capo_kinesis_analytics_v2.types.source_schema


class ReferenceDataSourceDescription(TypedDict, closed=True):
    reference_id: "capo_kinesis_analytics_v2.types.id.Id"
    """<p>The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the <a>CreateApplication</a> or <a>UpdateApplication</a> operation.</p>"""
    table_name: "capo_kinesis_analytics_v2.types.in_app_table_name.InAppTableName"
    """<p>The in-application table name created by the specific reference data source configuration.</p>"""
    s3_reference_data_source_description: "capo_kinesis_analytics_v2.types.s3_reference_data_source_description.S3ReferenceDataSourceDescription"
    """<p>Provides the Amazon S3 bucket name, the object key name that contains the reference data. </p>"""
    reference_schema: NotRequired[
        "capo_kinesis_analytics_v2.types.source_schema.SourceSchema"
    ]
    """<p>Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSourceDescription) -> dict:
    out: dict = {}
    out["ReferenceId"] = value["reference_id"]
    out["TableName"] = value["table_name"]
    import capo_kinesis_analytics_v2.types.s3_reference_data_source_description

    out["S3ReferenceDataSourceDescription"] = (
        capo_kinesis_analytics_v2.types.s3_reference_data_source_description.serialize_aws_json_1_1(
            value["s3_reference_data_source_description"]
        )
    )
    if "reference_schema" in value:
        import capo_kinesis_analytics_v2.types.source_schema

        out["ReferenceSchema"] = (
            capo_kinesis_analytics_v2.types.source_schema.serialize_aws_json_1_1(
                value["reference_schema"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferenceDataSourceDescription:
    out: ReferenceDataSourceDescription = {}  # type: ignore[typeddict-item]
    if data.get("ReferenceId") is not None:
        out["reference_id"] = data["ReferenceId"]
    else:
        out["reference_id"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("S3ReferenceDataSourceDescription") is not None:
        import capo_kinesis_analytics_v2.types.s3_reference_data_source_description

        out["s3_reference_data_source_description"] = (
            capo_kinesis_analytics_v2.types.s3_reference_data_source_description.deserialize_aws_json_1_1(
                data["S3ReferenceDataSourceDescription"]
            )
        )
    else:
        raise DeserializationError(
            "ReferenceDataSourceDescription.s3_reference_data_source_description required"
        )
    if data.get("ReferenceSchema") is not None:
        import capo_kinesis_analytics_v2.types.source_schema

        out["reference_schema"] = (
            capo_kinesis_analytics_v2.types.source_schema.deserialize_aws_json_1_1(
                data["ReferenceSchema"]
            )
        )
    return out
