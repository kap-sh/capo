"""Generated from Smithy shape ``com.amazonaws.b2bi#TestMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.file_format
    import capo_b2bi.types.mapping_template
    import capo_b2bi.types.test_mapping_input_file_content


class TestMappingRequest(TypedDict, closed=True):
    input_file_content: (
        "capo_b2bi.types.test_mapping_input_file_content.TestMappingInputFileContent"
    )
    """<p>Specify the contents of the EDI (electronic data interchange) XML or JSON file that is used as input for the transform.</p>"""
    mapping_template: "capo_b2bi.types.mapping_template.MappingTemplate"
    """<p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html">Mapping</a> data type instead.</p> </note>"""
    file_format: "capo_b2bi.types.file_format.FileFormat"
    """<p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestMappingRequest) -> dict:
    out: dict = {}
    out["inputFileContent"] = value["input_file_content"]
    out["mappingTemplate"] = value["mapping_template"]
    import capo_b2bi.types.file_format

    out["fileFormat"] = capo_b2bi.types.file_format.serialize_aws_json_1_0(
        value["file_format"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestMappingRequest:
    out: TestMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("inputFileContent") is not None:
        out["input_file_content"] = data["inputFileContent"]
    else:
        raise DeserializationError("TestMappingRequest.input_file_content required")
    if data.get("mappingTemplate") is not None:
        out["mapping_template"] = data["mappingTemplate"]
    else:
        raise DeserializationError("TestMappingRequest.mapping_template required")
    if data.get("fileFormat") is not None:
        import capo_b2bi.types.file_format

        out["file_format"] = capo_b2bi.types.file_format.deserialize_aws_json_1_0(
            data["fileFormat"]
        )
    else:
        raise DeserializationError("TestMappingRequest.file_format required")
    return out
