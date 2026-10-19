"""Generated from Smithy shape ``com.amazonaws.b2bi#ConversionSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.conversion_source_format
    import capo_b2bi.types.input_file_source


class ConversionSource(TypedDict, closed=True):
    file_format: "capo_b2bi.types.conversion_source_format.ConversionSourceFormat"
    """<p>The format for the input file: either JSON or XML.</p>"""
    input_file: "capo_b2bi.types.input_file_source.InputFileSource"
    """File to be converted"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConversionSource) -> dict:
    out: dict = {}
    import capo_b2bi.types.conversion_source_format

    out["fileFormat"] = capo_b2bi.types.conversion_source_format.serialize_aws_json_1_0(
        value["file_format"]
    )
    import capo_b2bi.types.input_file_source

    out["inputFile"] = capo_b2bi.types.input_file_source.serialize_aws_json_1_0(
        value["input_file"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConversionSource:
    out: ConversionSource = {}  # type: ignore[typeddict-item]
    if data.get("fileFormat") is not None:
        import capo_b2bi.types.conversion_source_format

        out["file_format"] = (
            capo_b2bi.types.conversion_source_format.deserialize_aws_json_1_0(
                data["fileFormat"]
            )
        )
    else:
        import typing

        out["file_format"] = typing.cast(
            "capo_b2bi.types.conversion_source_format.ConversionSourceFormat", ""
        )
    if data.get("inputFile") is not None:
        import capo_b2bi.types.input_file_source

        out["input_file"] = capo_b2bi.types.input_file_source.deserialize_aws_json_1_0(
            data["inputFile"]
        )
    else:
        import capo_b2bi.types._unknown

        out["input_file"] = capo_b2bi.types._unknown.UnknownUnionMember("")
    return out
