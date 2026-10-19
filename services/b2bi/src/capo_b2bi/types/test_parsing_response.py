"""Generated from Smithy shape ``com.amazonaws.b2bi#TestParsingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.parsed_split_file_contents_list
    import capo_b2bi.types.validation_messages


class TestParsingResponse(TypedDict, closed=True):
    parsed_file_content: "str"
    """<p>Returns the contents of the input file being tested, parsed according to the specified EDI (electronic data interchange) type.</p>"""
    parsed_split_file_contents: NotRequired[
        "capo_b2bi.types.parsed_split_file_contents_list.ParsedSplitFileContentsList"
    ]
    """<p>Returns an array of parsed file contents when the input file is split according to the specified split options. Each element in the array represents a separate split file's parsed content.</p>"""
    validation_messages: NotRequired[
        "capo_b2bi.types.validation_messages.ValidationMessages"
    ]
    """<p>Returns an array of validation messages generated during EDI validation. These messages provide detailed information about validation errors, warnings, or confirmations based on the configured X12 validation rules such as element length constraints, code list validations, and element requirement checks. This field is populated when the <code>TestParsing</code> API validates EDI documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestParsingResponse) -> dict:
    out: dict = {}
    out["parsedFileContent"] = value["parsed_file_content"]
    if "parsed_split_file_contents" in value:
        import capo_b2bi.types.parsed_split_file_contents_list

        out["parsedSplitFileContents"] = (
            capo_b2bi.types.parsed_split_file_contents_list.serialize_aws_json_1_0(
                value["parsed_split_file_contents"]
            )
        )
    if "validation_messages" in value:
        import capo_b2bi.types.validation_messages

        out["validationMessages"] = (
            capo_b2bi.types.validation_messages.serialize_aws_json_1_0(
                value["validation_messages"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestParsingResponse:
    out: TestParsingResponse = {}  # type: ignore[typeddict-item]
    if data.get("parsedFileContent") is not None:
        out["parsed_file_content"] = data["parsedFileContent"]
    else:
        out["parsed_file_content"] = ""
    if data.get("parsedSplitFileContents") is not None:
        import capo_b2bi.types.parsed_split_file_contents_list

        out["parsed_split_file_contents"] = (
            capo_b2bi.types.parsed_split_file_contents_list.deserialize_aws_json_1_0(
                data["parsedSplitFileContents"]
            )
        )
    if data.get("validationMessages") is not None:
        import capo_b2bi.types.validation_messages

        out["validation_messages"] = (
            capo_b2bi.types.validation_messages.deserialize_aws_json_1_0(
                data["validationMessages"]
            )
        )
    return out
