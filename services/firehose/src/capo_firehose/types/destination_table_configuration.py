"""Generated from Smithy shape ``com.amazonaws.firehose#DestinationTableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.error_output_prefix
    import capo_firehose.types.list_of_non_empty_strings_without_whitespace
    import capo_firehose.types.partition_spec
    import capo_firehose.types.string_with_letters_digits_underscores_dots


class DestinationTableConfiguration(TypedDict, closed=True):
    destination_table_name: "capo_firehose.types.string_with_letters_digits_underscores_dots.StringWithLettersDigitsUnderscoresDots"
    """<p> Specifies the name of the Apache Iceberg Table. </p>"""
    destination_database_name: "capo_firehose.types.string_with_letters_digits_underscores_dots.StringWithLettersDigitsUnderscoresDots"
    """<p> The name of the Apache Iceberg database. </p>"""
    unique_keys: NotRequired[
        "capo_firehose.types.list_of_non_empty_strings_without_whitespace.ListOfNonEmptyStringsWithoutWhitespace"
    ]
    """<p> A list of unique keys for a given Apache Iceberg table. Firehose will use these for running Create, Update, or Delete operations on the given Iceberg table. </p>"""
    partition_spec: NotRequired["capo_firehose.types.partition_spec.PartitionSpec"]
    """<p>The partition spec configuration for a table that is used by automatic table creation.</p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    s3_error_output_prefix: NotRequired[
        "capo_firehose.types.error_output_prefix.ErrorOutputPrefix"
    ]
    """<p> The table specific S3 error output prefix. All the errors that occurred while delivering to this table will be prefixed with this value in S3 destination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationTableConfiguration) -> dict:
    out: dict = {}
    out["DestinationTableName"] = value["destination_table_name"]
    out["DestinationDatabaseName"] = value["destination_database_name"]
    if "unique_keys" in value:
        import capo_firehose.types.list_of_non_empty_strings_without_whitespace

        out["UniqueKeys"] = (
            capo_firehose.types.list_of_non_empty_strings_without_whitespace.serialize_aws_json_1_1(
                value["unique_keys"]
            )
        )
    if "partition_spec" in value:
        import capo_firehose.types.partition_spec

        out["PartitionSpec"] = (
            capo_firehose.types.partition_spec.serialize_aws_json_1_1(
                value["partition_spec"]
            )
        )
    if "s3_error_output_prefix" in value:
        out["S3ErrorOutputPrefix"] = value["s3_error_output_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationTableConfiguration:
    out: DestinationTableConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DestinationTableName") is not None:
        out["destination_table_name"] = data["DestinationTableName"]
    else:
        out["destination_table_name"] = ""
    if data.get("DestinationDatabaseName") is not None:
        out["destination_database_name"] = data["DestinationDatabaseName"]
    else:
        out["destination_database_name"] = ""
    if data.get("UniqueKeys") is not None:
        import capo_firehose.types.list_of_non_empty_strings_without_whitespace

        out["unique_keys"] = (
            capo_firehose.types.list_of_non_empty_strings_without_whitespace.deserialize_aws_json_1_1(
                data["UniqueKeys"]
            )
        )
    if data.get("PartitionSpec") is not None:
        import capo_firehose.types.partition_spec

        out["partition_spec"] = (
            capo_firehose.types.partition_spec.deserialize_aws_json_1_1(
                data["PartitionSpec"]
            )
        )
    if data.get("S3ErrorOutputPrefix") is not None:
        out["s3_error_output_prefix"] = data["S3ErrorOutputPrefix"]
    return out
