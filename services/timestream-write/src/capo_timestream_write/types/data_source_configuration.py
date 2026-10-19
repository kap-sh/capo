"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_write.types.batch_load_data_format
    import capo_timestream_write.types.csv_configuration
    import capo_timestream_write.types.data_source_s3_configuration


class DataSourceConfiguration(TypedDict, closed=True):
    data_source_s3_configuration: "capo_timestream_write.types.data_source_s3_configuration.DataSourceS3Configuration"
    """<p>Configuration of an S3 location for a file which contains data to load.</p>"""
    csv_configuration: NotRequired[
        "capo_timestream_write.types.csv_configuration.CsvConfiguration"
    ]
    data_format: (
        "capo_timestream_write.types.batch_load_data_format.BatchLoadDataFormat"
    )
    """<p>This is currently CSV.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataSourceConfiguration) -> dict:
    out: dict = {}
    import capo_timestream_write.types.data_source_s3_configuration

    out["DataSourceS3Configuration"] = (
        capo_timestream_write.types.data_source_s3_configuration.serialize_aws_json_1_0(
            value["data_source_s3_configuration"]
        )
    )
    if "csv_configuration" in value:
        import capo_timestream_write.types.csv_configuration

        out["CsvConfiguration"] = (
            capo_timestream_write.types.csv_configuration.serialize_aws_json_1_0(
                value["csv_configuration"]
            )
        )
    import capo_timestream_write.types.batch_load_data_format

    out["DataFormat"] = (
        capo_timestream_write.types.batch_load_data_format.serialize_aws_json_1_0(
            value["data_format"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DataSourceConfiguration:
    out: DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceS3Configuration") is not None:
        import capo_timestream_write.types.data_source_s3_configuration

        out["data_source_s3_configuration"] = (
            capo_timestream_write.types.data_source_s3_configuration.deserialize_aws_json_1_0(
                data["DataSourceS3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "DataSourceConfiguration.data_source_s3_configuration required"
        )
    if data.get("CsvConfiguration") is not None:
        import capo_timestream_write.types.csv_configuration

        out["csv_configuration"] = (
            capo_timestream_write.types.csv_configuration.deserialize_aws_json_1_0(
                data["CsvConfiguration"]
            )
        )
    if data.get("DataFormat") is not None:
        import capo_timestream_write.types.batch_load_data_format

        out["data_format"] = (
            capo_timestream_write.types.batch_load_data_format.deserialize_aws_json_1_0(
                data["DataFormat"]
            )
        )
    else:
        import typing

        out["data_format"] = typing.cast(
            "capo_timestream_write.types.batch_load_data_format.BatchLoadDataFormat", ""
        )
    return out
