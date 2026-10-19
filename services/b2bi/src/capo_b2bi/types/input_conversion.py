"""Generated from Smithy shape ``com.amazonaws.b2bi#InputConversion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.advanced_options
    import capo_b2bi.types.format_options
    import capo_b2bi.types.from_format


class InputConversion(TypedDict, closed=True):
    from_format: "capo_b2bi.types.from_format.FromFormat"
    """<p>The format for the transformer input: currently on <code>X12</code> is supported.</p>"""
    format_options: NotRequired["capo_b2bi.types.format_options.FormatOptions"]
    """<p>A structure that contains the formatting options for an inbound transformer.</p>"""
    advanced_options: NotRequired["capo_b2bi.types.advanced_options.AdvancedOptions"]
    """<p>Specifies advanced options for the input conversion process. These options provide additional control over how EDI files are processed during transformation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputConversion) -> dict:
    out: dict = {}
    import capo_b2bi.types.from_format

    out["fromFormat"] = capo_b2bi.types.from_format.serialize_aws_json_1_0(
        value["from_format"]
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


def deserialize_aws_json_1_0(data: dict) -> InputConversion:
    out: InputConversion = {}  # type: ignore[typeddict-item]
    if data.get("fromFormat") is not None:
        import capo_b2bi.types.from_format

        out["from_format"] = capo_b2bi.types.from_format.deserialize_aws_json_1_0(
            data["fromFormat"]
        )
    else:
        import typing

        out["from_format"] = typing.cast("capo_b2bi.types.from_format.FromFormat", "")
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
