"""Generated from Smithy shape ``com.amazonaws.b2bi#GenerateMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.generate_mapping_input_file_content
    import capo_b2bi.types.generate_mapping_output_file_content
    import capo_b2bi.types.mapping_type


class GenerateMappingRequest(TypedDict, closed=True):
    input_file_content: "capo_b2bi.types.generate_mapping_input_file_content.GenerateMappingInputFileContent"
    """<p>Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a starting point for the mapping.</p>"""
    output_file_content: "capo_b2bi.types.generate_mapping_output_file_content.GenerateMappingOutputFileContent"
    """<p>Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a target for the mapping.</p>"""
    mapping_type: "capo_b2bi.types.mapping_type.MappingType"
    """<p>Specify the mapping type: either <code>JSONATA</code> or <code>XSLT.</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GenerateMappingRequest) -> dict:
    out: dict = {}
    out["inputFileContent"] = value["input_file_content"]
    out["outputFileContent"] = value["output_file_content"]
    import capo_b2bi.types.mapping_type

    out["mappingType"] = capo_b2bi.types.mapping_type.serialize_aws_json_1_0(
        value["mapping_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GenerateMappingRequest:
    out: GenerateMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("inputFileContent") is not None:
        out["input_file_content"] = data["inputFileContent"]
    else:
        out["input_file_content"] = ""
    if data.get("outputFileContent") is not None:
        out["output_file_content"] = data["outputFileContent"]
    else:
        out["output_file_content"] = ""
    if data.get("mappingType") is not None:
        import capo_b2bi.types.mapping_type

        out["mapping_type"] = capo_b2bi.types.mapping_type.deserialize_aws_json_1_0(
            data["mappingType"]
        )
    else:
        import typing

        out["mapping_type"] = typing.cast(
            "capo_b2bi.types.mapping_type.MappingType", ""
        )
    return out
