"""Generated from Smithy shape ``com.amazonaws.glue#S3DeltaDirectTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.additional_options
    import capo_glue.types.auto_data_quality
    import capo_glue.types.delta_target_compression_type
    import capo_glue.types.direct_schema_change_policy
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_studio_path_list
    import capo_glue.types.node_name
    import capo_glue.types.number_target_partitions_string
    import capo_glue.types.one_input
    import capo_glue.types.target_format


class S3DeltaDirectTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    partition_keys: NotRequired[
        "capo_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Specifies native partitioning using a sequence of keys.</p>"""
    path: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The Amazon S3 path of your Delta Lake data source to write to.</p>"""
    compression: (
        "capo_glue.types.delta_target_compression_type.DeltaTargetCompressionType"
    )
    """<p>Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are <code>"gzip"</code> and <code>"bzip"</code>).</p>"""
    number_target_partitions: NotRequired[
        "capo_glue.types.number_target_partitions_string.NumberTargetPartitionsString"
    ]
    """<p>Specifies the number of target partitions for distributing Delta Lake dataset files across Amazon S3.</p>"""
    format: "capo_glue.types.target_format.TargetFormat"
    """<p>Specifies the data output format for the target.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Specifies additional connection options for the connector.</p>"""
    schema_change_policy: NotRequired[
        "capo_glue.types.direct_schema_change_policy.DirectSchemaChangePolicy"
    ]
    """<p>A policy that specifies update behavior for the crawler.</p>"""
    auto_data_quality: NotRequired["capo_glue.types.auto_data_quality.AutoDataQuality"]
    """<p>Specifies whether to automatically enable data quality evaluation for the S3 Delta direct target. When set to <code>true</code>, data quality checks are performed automatically during the write operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DeltaDirectTarget) -> dict:
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
    import capo_glue.types.delta_target_compression_type

    out["Compression"] = (
        capo_glue.types.delta_target_compression_type.serialize_aws_json_1_1(
            value["compression"]
        )
    )
    if "number_target_partitions" in value:
        out["NumberTargetPartitions"] = value["number_target_partitions"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DeltaDirectTarget:
    out: S3DeltaDirectTarget = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3DeltaDirectTarget.name required")
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("S3DeltaDirectTarget.inputs required")
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
        raise DeserializationError("S3DeltaDirectTarget.path required")
    if data.get("Compression") is not None:
        import capo_glue.types.delta_target_compression_type

        out["compression"] = (
            capo_glue.types.delta_target_compression_type.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    else:
        raise DeserializationError("S3DeltaDirectTarget.compression required")
    if data.get("NumberTargetPartitions") is not None:
        out["number_target_partitions"] = data["NumberTargetPartitions"]
    if data.get("Format") is not None:
        import capo_glue.types.target_format

        out["format"] = capo_glue.types.target_format.deserialize_aws_json_1_1(
            data["Format"]
        )
    else:
        raise DeserializationError("S3DeltaDirectTarget.format required")
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
    return out
