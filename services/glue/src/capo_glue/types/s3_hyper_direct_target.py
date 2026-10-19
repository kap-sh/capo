"""Generated from Smithy shape ``com.amazonaws.glue#S3HyperDirectTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.auto_data_quality
    import capo_glue.types.direct_schema_change_policy
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.glue_studio_path_list
    import capo_glue.types.hyper_target_compression_type
    import capo_glue.types.node_name
    import capo_glue.types.one_input
    import capo_glue.types.target_format


class S3HyperDirectTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The unique identifier for the HyperDirect target node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>Specifies the input source for the HyperDirect target.</p>"""
    format: NotRequired["capo_glue.types.target_format.TargetFormat"]
    """<p>Specifies the data output format for the HyperDirect target.</p>"""
    partition_keys: NotRequired[
        "capo_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Defines the partitioning strategy for the output data.</p>"""
    path: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The S3 location where the output data will be written.</p>"""
    compression: NotRequired[
        "capo_glue.types.hyper_target_compression_type.HyperTargetCompressionType"
    ]
    """<p>The compression type to apply to the output data.</p>"""
    schema_change_policy: NotRequired[
        "capo_glue.types.direct_schema_change_policy.DirectSchemaChangePolicy"
    ]
    """<p>Defines how schema changes are handled during write operations.</p>"""
    auto_data_quality: NotRequired["capo_glue.types.auto_data_quality.AutoDataQuality"]
    """<p>Specifies whether to automatically enable data quality evaluation for the S3 Hyper direct target. When set to <code>true</code>, data quality checks are performed automatically during the write operation.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 Hyper direct target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3HyperDirectTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "format" in value:
        import capo_glue.types.target_format

        out["Format"] = capo_glue.types.target_format.serialize_aws_json_1_1(
            value["format"]
        )
    if "partition_keys" in value:
        import capo_glue.types.glue_studio_path_list

        out["PartitionKeys"] = (
            capo_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
                value["partition_keys"]
            )
        )
    out["Path"] = value["path"]
    if "compression" in value:
        import capo_glue.types.hyper_target_compression_type

        out["Compression"] = (
            capo_glue.types.hyper_target_compression_type.serialize_aws_json_1_1(
                value["compression"]
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
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3HyperDirectTarget:
    out: S3HyperDirectTarget = {}  # type: ignore[typeddict-item]
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
    if data.get("Format") is not None:
        import capo_glue.types.target_format

        out["format"] = capo_glue.types.target_format.deserialize_aws_json_1_1(
            data["Format"]
        )
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
    if data.get("Compression") is not None:
        import capo_glue.types.hyper_target_compression_type

        out["compression"] = (
            capo_glue.types.hyper_target_compression_type.deserialize_aws_json_1_1(
                data["Compression"]
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
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
