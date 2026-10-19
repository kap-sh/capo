"""Generated from Smithy shape ``com.amazonaws.b2bi#TestParsingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.advanced_options
    import capo_b2bi.types.edi_type
    import capo_b2bi.types.file_format
    import capo_b2bi.types.s3_location


class TestParsingRequest(TypedDict, closed=True):
    input_file: "capo_b2bi.types.s3_location.S3Location"
    """<p>Specifies an <code>S3Location</code> object, which contains the Amazon S3 bucket and prefix for the location of the input file.</p>"""
    file_format: "capo_b2bi.types.file_format.FileFormat"
    """<p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>"""
    edi_type: "capo_b2bi.types.edi_type.EdiType"
    """<p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>"""
    advanced_options: NotRequired["capo_b2bi.types.advanced_options.AdvancedOptions"]
    """<p>Specifies advanced options for parsing the input EDI file. These options allow for more granular control over the parsing process, including split options for X12 files.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestParsingRequest) -> dict:
    out: dict = {}
    import capo_b2bi.types.s3_location

    out["inputFile"] = capo_b2bi.types.s3_location.serialize_aws_json_1_0(
        value["input_file"]
    )
    import capo_b2bi.types.file_format

    out["fileFormat"] = capo_b2bi.types.file_format.serialize_aws_json_1_0(
        value["file_format"]
    )
    import capo_b2bi.types.edi_type

    out["ediType"] = capo_b2bi.types.edi_type.serialize_aws_json_1_0(value["edi_type"])
    if "advanced_options" in value:
        import capo_b2bi.types.advanced_options

        out["advancedOptions"] = (
            capo_b2bi.types.advanced_options.serialize_aws_json_1_0(
                value["advanced_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestParsingRequest:
    out: TestParsingRequest = {}  # type: ignore[typeddict-item]
    if data.get("inputFile") is not None:
        import capo_b2bi.types.s3_location

        out["input_file"] = capo_b2bi.types.s3_location.deserialize_aws_json_1_0(
            data["inputFile"]
        )
    else:
        raise DeserializationError("TestParsingRequest.input_file required")
    if data.get("fileFormat") is not None:
        import capo_b2bi.types.file_format

        out["file_format"] = capo_b2bi.types.file_format.deserialize_aws_json_1_0(
            data["fileFormat"]
        )
    else:
        import typing

        out["file_format"] = typing.cast("capo_b2bi.types.file_format.FileFormat", "")
    if data.get("ediType") is not None:
        import capo_b2bi.types.edi_type

        out["edi_type"] = capo_b2bi.types.edi_type.deserialize_aws_json_1_0(
            data["ediType"]
        )
    else:
        import capo_b2bi.types._unknown

        out["edi_type"] = capo_b2bi.types._unknown.UnknownUnionMember("")
    if data.get("advancedOptions") is not None:
        import capo_b2bi.types.advanced_options

        out["advanced_options"] = (
            capo_b2bi.types.advanced_options.deserialize_aws_json_1_0(
                data["advancedOptions"]
            )
        )
    return out
