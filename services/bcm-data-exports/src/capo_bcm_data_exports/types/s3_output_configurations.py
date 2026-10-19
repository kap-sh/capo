"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#S3OutputConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.compression_option
    import capo_bcm_data_exports.types.format_option
    import capo_bcm_data_exports.types.overwrite_option
    import capo_bcm_data_exports.types.s3_output_type


class S3OutputConfigurations(TypedDict, closed=True):
    output_type: "capo_bcm_data_exports.types.s3_output_type.S3OutputType"
    """<p>The output type for the data export.</p>"""
    format: "capo_bcm_data_exports.types.format_option.FormatOption"
    """<p>The file format for the data export.</p>"""
    compression: "capo_bcm_data_exports.types.compression_option.CompressionOption"
    """<p>The compression type for the data export.</p>"""
    overwrite: "capo_bcm_data_exports.types.overwrite_option.OverwriteOption"
    """<p>The rule to follow when generating a version of the data export file. You have the choice to overwrite the previous version or to be delivered in addition to the previous versions. Overwriting exports can save on Amazon S3 storage costs. Creating new export versions allows you to track the changes in cost and usage data over time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3OutputConfigurations) -> dict:
    out: dict = {}
    import capo_bcm_data_exports.types.s3_output_type

    out["OutputType"] = (
        capo_bcm_data_exports.types.s3_output_type.serialize_aws_json_1_1(
            value["output_type"]
        )
    )
    import capo_bcm_data_exports.types.format_option

    out["Format"] = capo_bcm_data_exports.types.format_option.serialize_aws_json_1_1(
        value["format"]
    )
    import capo_bcm_data_exports.types.compression_option

    out["Compression"] = (
        capo_bcm_data_exports.types.compression_option.serialize_aws_json_1_1(
            value["compression"]
        )
    )
    import capo_bcm_data_exports.types.overwrite_option

    out["Overwrite"] = (
        capo_bcm_data_exports.types.overwrite_option.serialize_aws_json_1_1(
            value["overwrite"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3OutputConfigurations:
    out: S3OutputConfigurations = {}  # type: ignore[typeddict-item]
    if data.get("OutputType") is not None:
        import capo_bcm_data_exports.types.s3_output_type

        out["output_type"] = (
            capo_bcm_data_exports.types.s3_output_type.deserialize_aws_json_1_1(
                data["OutputType"]
            )
        )
    else:
        import typing

        out["output_type"] = typing.cast(
            "capo_bcm_data_exports.types.s3_output_type.S3OutputType", ""
        )
    if data.get("Format") is not None:
        import capo_bcm_data_exports.types.format_option

        out["format"] = (
            capo_bcm_data_exports.types.format_option.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_bcm_data_exports.types.format_option.FormatOption", ""
        )
    if data.get("Compression") is not None:
        import capo_bcm_data_exports.types.compression_option

        out["compression"] = (
            capo_bcm_data_exports.types.compression_option.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    else:
        import typing

        out["compression"] = typing.cast(
            "capo_bcm_data_exports.types.compression_option.CompressionOption", ""
        )
    if data.get("Overwrite") is not None:
        import capo_bcm_data_exports.types.overwrite_option

        out["overwrite"] = (
            capo_bcm_data_exports.types.overwrite_option.deserialize_aws_json_1_1(
                data["Overwrite"]
            )
        )
    else:
        import typing

        out["overwrite"] = typing.cast(
            "capo_bcm_data_exports.types.overwrite_option.OverwriteOption", ""
        )
    return out
