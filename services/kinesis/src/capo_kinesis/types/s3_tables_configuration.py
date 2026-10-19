"""Generated from Smithy shape ``com.amazonaws.kinesis#S3TablesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.partition_spec
    import capo_kinesis.types.s3_tables_compression_type
    import capo_kinesis.types.s3_tables_namespace
    import capo_kinesis.types.s3_tables_table_name
    import capo_kinesis.types.table_bucket_arn


class S3TablesConfiguration(TypedDict, closed=True):
    table_bucket_arn: "capo_kinesis.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 table bucket.</p>"""
    namespace: "capo_kinesis.types.s3_tables_namespace.S3TablesNamespace"
    """<p>The namespace (database) of the destination table.</p>"""
    table_name: "capo_kinesis.types.s3_tables_table_name.S3TablesTableName"
    """<p>The name of the destination table. Amazon Kinesis Data Streams creates this table in the specified table bucket.</p>"""
    compression_type: (
        "capo_kinesis.types.s3_tables_compression_type.S3TablesCompressionType"
    )
    """<p>The compression applied to Parquet data files. Valid values:</p> <ul> <li> <p> <code>NONE</code> - No compression.</p> </li> <li> <p> <code>ZSTD</code> - Zstandard compression.</p> </li> <li> <p> <code>SNAPPY</code> - Snappy compression.</p> </li> </ul>"""
    partition_spec: NotRequired["capo_kinesis.types.partition_spec.PartitionSpec"]
    """<p>The partitioning specification for the destination table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TablesConfiguration) -> dict:
    out: dict = {}
    out["TableBucketARN"] = value["table_bucket_arn"]
    out["Namespace"] = value["namespace"]
    out["TableName"] = value["table_name"]
    import capo_kinesis.types.s3_tables_compression_type

    out["CompressionType"] = (
        capo_kinesis.types.s3_tables_compression_type.serialize_aws_json_1_1(
            value["compression_type"]
        )
    )
    if "partition_spec" in value:
        import capo_kinesis.types.partition_spec

        out["PartitionSpec"] = capo_kinesis.types.partition_spec.serialize_aws_json_1_1(
            value["partition_spec"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3TablesConfiguration:
    out: S3TablesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TableBucketARN") is not None:
        out["table_bucket_arn"] = data["TableBucketARN"]
    else:
        out["table_bucket_arn"] = ""
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    else:
        out["namespace"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("CompressionType") is not None:
        import capo_kinesis.types.s3_tables_compression_type

        out["compression_type"] = (
            capo_kinesis.types.s3_tables_compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    else:
        import typing

        out["compression_type"] = typing.cast(
            "capo_kinesis.types.s3_tables_compression_type.S3TablesCompressionType", ""
        )
    if data.get("PartitionSpec") is not None:
        import capo_kinesis.types.partition_spec

        out["partition_spec"] = (
            capo_kinesis.types.partition_spec.deserialize_aws_json_1_1(
                data["PartitionSpec"]
            )
        )
    return out
