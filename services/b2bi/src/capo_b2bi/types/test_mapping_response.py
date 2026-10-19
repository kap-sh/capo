"""Generated from Smithy shape ``com.amazonaws.b2bi#TestMappingResponse``."""

from typing_extensions import TypedDict


class TestMappingResponse(TypedDict, closed=True):
    mapped_file_content: "str"
    """<p>Returns a string for the mapping that can be used to identify the mapping. Similar to a fingerprint</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestMappingResponse) -> dict:
    out: dict = {}
    out["mappedFileContent"] = value["mapped_file_content"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TestMappingResponse:
    out: TestMappingResponse = {}  # type: ignore[typeddict-item]
    if data.get("mappedFileContent") is not None:
        out["mapped_file_content"] = data["mappedFileContent"]
    else:
        out["mapped_file_content"] = ""
    return out
