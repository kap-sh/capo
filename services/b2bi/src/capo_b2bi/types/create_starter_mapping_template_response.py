"""Generated from Smithy shape ``com.amazonaws.b2bi#CreateStarterMappingTemplateResponse``."""

from typing_extensions import TypedDict


class CreateStarterMappingTemplateResponse(TypedDict, closed=True):
    mapping_template: "str"
    """<p>Returns a string that represents the mapping template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStarterMappingTemplateResponse) -> dict:
    out: dict = {}
    out["mappingTemplate"] = value["mapping_template"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStarterMappingTemplateResponse:
    out: CreateStarterMappingTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("mappingTemplate") is not None:
        out["mapping_template"] = data["mappingTemplate"]
    else:
        out["mapping_template"] = ""
    return out
