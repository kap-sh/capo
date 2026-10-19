"""Generated from Smithy shape ``com.amazonaws.glue#S3IcebergDirectTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.additional_options
    import capo_glue.types.auto_data_quality
    import capo_glue.types.direct_schema_change_policy
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.glue_studio_path_list
    import capo_glue.types.iceberg_target_compression_type
    import capo_glue.types.node_name
    import capo_glue.types.number_target_partitions_string
    import capo_glue.types.one_input
    import capo_glue.types.target_format


class S3IcebergDirectTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>Specifies the unique identifier for the Iceberg target node in your data pipeline.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>Defines the single input source that provides data to this Iceberg target.</p>"""
    partition_keys: NotRequired[
        "capo_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Specifies the columns used to partition the Iceberg table data in S3.</p>"""
    path: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>Defines the S3 location where the Iceberg table data will be stored.</p>"""
    format: "capo_glue.types.target_format.TargetFormat"
    """<p>Specifies the file format used for storing Iceberg table data (e.g., Parquet, ORC).</p>"""
    additional_options: NotRequired[
        "capo_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Provides additional configuration options for customizing the Iceberg table behavior.</p>"""
    schema_change_policy: NotRequired[
        "capo_glue.types.direct_schema_change_policy.DirectSchemaChangePolicy"
    ]
    """<p>Defines how schema changes are handled when writing data to the Iceberg table.</p>"""
    auto_data_quality: NotRequired["capo_glue.types.auto_data_quality.AutoDataQuality"]
    compression: (
        "capo_glue.types.iceberg_target_compression_type.IcebergTargetCompressionType"
    )
    """<p>Specifies the compression codec used for Iceberg table files in S3.</p>"""
    number_target_partitions: NotRequired[
        "capo_glue.types.number_target_partitions_string.NumberTargetPartitionsString"
    ]
    """<p>Sets the number of target partitions for distributing Iceberg table files across S3.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 Iceberg direct target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3IcebergDirectTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "partition_keys" in value:
        import capo_glue.types.glue_studio_path_list

        out["PartitionKeys"] = (
            capo_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
                value["partition_keys"]
            )
        )
    out["Path"] = value["path"]
    import capo_glue.types.target_format

    out["Format"] = capo_glue.types.target_format.serialize_aws_json_1_1(
        value["format"]
    )
    if "additional_options" in value:
        import capo_glue.types.additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "schema_change_policy" in value:
        import capo_glue.types.direct_schema_change_policy

        out["SchemaChangePolicy"] = (
            capo_glue.types.direct_schema_change_policy.serialize_aws_json_1_1(
                value["schema_change_policy"]
            )
        )
    if "auto_data_quality" in value:
        import capo_glue.types.auto_data_quality

        out["AutoDataQuality"] = (
            capo_glue.types.auto_data_quality.serialize_aws_json_1_1(
                value["auto_data_quality"]
            )
        )
    import capo_glue.types.iceberg_target_compression_type

    out["Compression"] = (
        capo_glue.types.iceberg_target_compression_type.serialize_aws_json_1_1(
            value["compression"]
        )
    )
    if "number_target_partitions" in value:
        out["NumberTargetPartitions"] = value["number_target_partitions"]
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3IcebergDirectTarget:
    out: S3IcebergDirectTarget = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("PartitionKeys") is not None:
        import capo_glue.types.glue_studio_path_list

        out["partition_keys"] = (
            capo_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["PartitionKeys"]
            )
        )
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    else:
        out["path"] = ""
    if data.get("Format") is not None:
        import capo_glue.types.target_format

        out["format"] = capo_glue.types.target_format.deserialize_aws_json_1_1(
            data["Format"]
        )
    else:
        import typing

        out["format"] = typing.cast("capo_glue.types.target_format.TargetFormat", "")
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.additional_options

        out["additional_options"] = (
            capo_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if data.get("SchemaChangePolicy") is not None:
        import capo_glue.types.direct_schema_change_policy

        out["schema_change_policy"] = (
            capo_glue.types.direct_schema_change_policy.deserialize_aws_json_1_1(
                data["SchemaChangePolicy"]
            )
        )
    if data.get("AutoDataQuality") is not None:
        import capo_glue.types.auto_data_quality

        out["auto_data_quality"] = (
            capo_glue.types.auto_data_quality.deserialize_aws_json_1_1(
                data["AutoDataQuality"]
            )
        )
    if data.get("Compression") is not None:
        import capo_glue.types.iceberg_target_compression_type

        out["compression"] = (
            capo_glue.types.iceberg_target_compression_type.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    else:
        import typing

        out["compression"] = typing.cast(
            "capo_glue.types.iceberg_target_compression_type.IcebergTargetCompressionType",
            "",
        )
    if data.get("NumberTargetPartitions") is not None:
        out["number_target_partitions"] = data["NumberTargetPartitions"]
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
