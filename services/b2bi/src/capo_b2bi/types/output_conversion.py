"""Generated from Smithy shape ``com.amazonaws.b2bi#OutputConversion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.advanced_options
    import capo_b2bi.types.format_options
    import capo_b2bi.types.to_format


class OutputConversion(TypedDict, closed=True):
    to_format: "capo_b2bi.types.to_format.ToFormat"
    """<p>The format for the output from an outbound transformer: only X12 is currently supported.</p>"""
    format_options: NotRequired["capo_b2bi.types.format_options.FormatOptions"]
    """<p>A structure that contains the X12 transaction set and version for the transformer output.</p>"""
    advanced_options: NotRequired["capo_b2bi.types.advanced_options.AdvancedOptions"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputConversion) -> dict:
    out: dict = {}
    import capo_b2bi.types.to_format

    out["toFormat"] = capo_b2bi.types.to_format.serialize_aws_json_1_0(
        value["to_format"]
    )
    if "format_options" in value:
        import capo_b2bi.types.format_options

        out["formatOptions"] = capo_b2bi.types.format_options.serialize_aws_json_1_0(
            value["format_options"]
        )
    if "advanced_options" in value:
        import capo_b2bi.types.advanced_options

        out["advancedOptions"] = (
            capo_b2bi.types.advanced_options.serialize_aws_json_1_0(
                value["advanced_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OutputConversion:
    out: OutputConversion = {}  # type: ignore[typeddict-item]
    if data.get("toFormat") is not None:
        import capo_b2bi.types.to_format

        out["to_format"] = capo_b2bi.types.to_format.deserialize_aws_json_1_0(
            data["toFormat"]
        )
    else:
        import typing

        out["to_format"] = typing.cast("capo_b2bi.types.to_format.ToFormat", "")
    if data.get("formatOptions") is not None:
        import capo_b2bi.types.format_options

        out["format_options"] = capo_b2bi.types.format_options.deserialize_aws_json_1_0(
            data["formatOptions"]
        )
    if data.get("advancedOptions") is not None:
        import capo_b2bi.types.advanced_options

        out["advanced_options"] = (
            capo_b2bi.types.advanced_options.deserialize_aws_json_1_0(
                data["advancedOptions"]
            )
        )
    return out
