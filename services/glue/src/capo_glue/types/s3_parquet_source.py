"""Generated from Smithy shape ``com.amazonaws.glue#S3ParquetSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.boxed_non_negative_int
    import capo_glue.types.enclosed_in_string_properties
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name
    import capo_glue.types.parquet_compression_type
    import capo_glue.types.s3_direct_source_additional_options


class S3ParquetSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data store.</p>"""
    paths: "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    """<p>A list of the Amazon S3 paths to read from.</p>"""
    compression_type: NotRequired[
        "capo_glue.types.parquet_compression_type.ParquetCompressionType"
    ]
    """<p>Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are <code>"gzip"</code> and <code>"bzip"</code>).</p>"""
    exclusions: NotRequired[
        "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    ]
    r"""<p>A string containing a JSON list of Unix-style glob patterns to exclude. For example, "[\"**.pdf\"]" excludes all PDF files. </p>"""
    group_size: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The target group size in bytes. The default is computed based on the input data size and the size of your cluster. When there are fewer than 50,000 input files, <code>"groupFiles"</code> must be set to <code>"inPartition"</code> for this to take effect.</p>"""
    group_files: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Grouping files is turned on by default when the input contains more than 50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter to "inPartition". To disable grouping when there are more than 50,000 files, set this parameter to <code>"none"</code>.</p>"""
    recurse: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>If set to true, recursively reads files in all subdirectories under the specified paths.</p>"""
    max_band: NotRequired["capo_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"]
    """<p>This option controls the duration in milliseconds after which the s3 listing is likely to be consistent. Files with modification timestamps falling within the last maxBand milliseconds are tracked specially when using JobBookmarks to account for Amazon S3 eventual consistency. Most users don't need to set this option. The default is 900000 milliseconds, or 15 minutes.</p>"""
    max_files_in_band: NotRequired[
        "capo_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>This option specifies the maximum number of files to save from the last maxBand seconds. If this number is exceeded, extra files are skipped and only processed in the next job run.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.s3_direct_source_additional_options.S3DirectSourceAdditionalOptions"
    ]
    """<p>Specifies additional connection options.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the S3 Parquet source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ParquetSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.enclosed_in_string_properties

    out["Paths"] = capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
        value["paths"]
    )
    if "compression_type" in value:
        import capo_glue.types.parquet_compression_type

        out["CompressionType"] = (
            capo_glue.types.parquet_compression_type.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    if "exclusions" in value:
        import capo_glue.types.enclosed_in_string_properties

        out["Exclusions"] = (
            capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
                value["exclusions"]
            )
        )
    if "group_size" in value:
        out["GroupSize"] = value["group_size"]
    if "group_files" in value:
        out["GroupFiles"] = value["group_files"]
    if "recurse" in value:
        out["Recurse"] = value["recurse"]
    if "max_band" in value:
        out["MaxBand"] = value["max_band"]
    if "max_files_in_band" in value:
        out["MaxFilesInBand"] = value["max_files_in_band"]
    if "additional_options" in value:
        import capo_glue.types.s3_direct_source_additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.s3_direct_source_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ParquetSource:
    out: S3ParquetSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3ParquetSource.name required")
    if data.get("Paths") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["paths"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    else:
        raise DeserializationError("S3ParquetSource.paths required")
    if data.get("CompressionType") is not None:
        import capo_glue.types.parquet_compression_type

        out["compression_type"] = (
            capo_glue.types.parquet_compression_type.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    if data.get("Exclusions") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["exclusions"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Exclusions"]
            )
        )
    if data.get("GroupSize") is not None:
        out["group_size"] = data["GroupSize"]
    if data.get("GroupFiles") is not None:
        out["group_files"] = data["GroupFiles"]
    if data.get("Recurse") is not None:
        out["recurse"] = data["Recurse"]
    if data.get("MaxBand") is not None:
        out["max_band"] = data["MaxBand"]
    if data.get("MaxFilesInBand") is not None:
        out["max_files_in_band"] = data["MaxFilesInBand"]
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.s3_direct_source_additional_options

        out["additional_options"] = (
            capo_glue.types.s3_direct_source_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
