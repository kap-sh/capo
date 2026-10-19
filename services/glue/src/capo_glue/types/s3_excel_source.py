"""Generated from Smithy shape ``com.amazonaws.glue#S3ExcelSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.boxed_long
    import capo_glue.types.boxed_non_negative_int
    import capo_glue.types.enclosed_in_string_properties
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name
    import capo_glue.types.parquet_compression_type
    import capo_glue.types.s3_direct_source_additional_options


class S3ExcelSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the S3 Excel data source.</p>"""
    paths: "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    """<p>The S3 paths where the Excel files are located.</p>"""
    compression_type: NotRequired[
        "capo_glue.types.parquet_compression_type.ParquetCompressionType"
    ]
    """<p>The compression format used for the Excel files.</p>"""
    exclusions: NotRequired[
        "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    ]
    """<p>Patterns to exclude specific files or paths from processing.</p>"""
    group_size: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Defines the size of file groups for batch processing.</p>"""
    group_files: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies how files should be grouped for processing.</p>"""
    recurse: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether to recursively process subdirectories.</p>"""
    max_band: NotRequired["capo_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"]
    """<p>The maximum number of processing bands to use.</p>"""
    max_files_in_band: NotRequired[
        "capo_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>The maximum number of files to process in each band.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.s3_direct_source_additional_options.S3DirectSourceAdditionalOptions"
    ]
    """<p>Additional configuration options for S3 direct source processing.</p>"""
    number_rows: NotRequired["capo_glue.types.boxed_long.BoxedLong"]
    """<p>The number of rows to process from each Excel file.</p>"""
    skip_footer: NotRequired[
        "capo_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>The number of rows to skip at the end of each Excel file.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>The Glue schemas to apply to the processed data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ExcelSource) -> dict:
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
    if "number_rows" in value:
        out["NumberRows"] = value["number_rows"]
    if "skip_footer" in value:
        out["SkipFooter"] = value["skip_footer"]
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ExcelSource:
    out: S3ExcelSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Paths") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["paths"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    else:
        out["paths"] = []
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
    if data.get("NumberRows") is not None:
        out["number_rows"] = data["NumberRows"]
    if data.get("SkipFooter") is not None:
        out["skip_footer"] = data["SkipFooter"]
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
