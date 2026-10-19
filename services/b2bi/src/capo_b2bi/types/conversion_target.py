"""Generated from Smithy shape ``com.amazonaws.b2bi#ConversionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.advanced_options
    import capo_b2bi.types.conversion_target_format
    import capo_b2bi.types.conversion_target_format_details
    import capo_b2bi.types.output_sample_file_source


class ConversionTarget(TypedDict, closed=True):
    file_format: "capo_b2bi.types.conversion_target_format.ConversionTargetFormat"
    """<p>Currently, only X12 format is supported.</p>"""
    format_details: NotRequired[
        "capo_b2bi.types.conversion_target_format_details.ConversionTargetFormatDetails"
    ]
    """<p>A structure that contains the formatting details for the conversion target.</p>"""
    output_sample_file: NotRequired[
        "capo_b2bi.types.output_sample_file_source.OutputSampleFileSource"
    ]
    """Customer uses this to provide a sample on what should file look like after conversion X12 EDI use case around this would be discovering the file syntax"""
    advanced_options: NotRequired["capo_b2bi.types.advanced_options.AdvancedOptions"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConversionTarget) -> dict:
    out: dict = {}
    import capo_b2bi.types.conversion_target_format

    out["fileFormat"] = capo_b2bi.types.conversion_target_format.serialize_aws_json_1_0(
        value["file_format"]
    )
    if "format_details" in value:
        import capo_b2bi.types.conversion_target_format_details

        out["formatDetails"] = (
            capo_b2bi.types.conversion_target_format_details.serialize_aws_json_1_0(
                value["format_details"]
            )
        )
    if "output_sample_file" in value:
        import capo_b2bi.types.output_sample_file_source

        out["outputSampleFile"] = (
            capo_b2bi.types.output_sample_file_source.serialize_aws_json_1_0(
                value["output_sample_file"]
            )
        )
    if "advanced_options" in value:
        import capo_b2bi.types.advanced_options

        out["advancedOptions"] = (
            capo_b2bi.types.advanced_options.serialize_aws_json_1_0(
                value["advanced_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConversionTarget:
    out: ConversionTarget = {}  # type: ignore[typeddict-item]
    if data.get("fileFormat") is not None:
        import capo_b2bi.types.conversion_target_format

        out["file_format"] = (
            capo_b2bi.types.conversion_target_format.deserialize_aws_json_1_0(
                data["fileFormat"]
            )
        )
    else:
        import typing

        out["file_format"] = typing.cast(
            "capo_b2bi.types.conversion_target_format.ConversionTargetFormat", ""
        )
    if data.get("formatDetails") is not None:
        import capo_b2bi.types.conversion_target_format_details

        out["format_details"] = (
            capo_b2bi.types.conversion_target_format_details.deserialize_aws_json_1_0(
                data["formatDetails"]
            )
        )
    if data.get("outputSampleFile") is not None:
        import capo_b2bi.types.output_sample_file_source

        out["output_sample_file"] = (
            capo_b2bi.types.output_sample_file_source.deserialize_aws_json_1_0(
                data["outputSampleFile"]
            )
        )
    if data.get("advancedOptions") is not None:
        import capo_b2bi.types.advanced_options

        out["advanced_options"] = (
            capo_b2bi.types.advanced_options.deserialize_aws_json_1_0(
                data["advancedOptions"]
            )
        )
    return out
