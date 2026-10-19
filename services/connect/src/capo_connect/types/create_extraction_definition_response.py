"""Generated from Smithy shape ``com.amazonaws.connect#CreateExtractionDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.extraction_definition_id


class CreateExtractionDefinitionResponse(TypedDict, closed=True):
    extraction_definition_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the extraction definition.</p>"""
    extraction_definition_id: (
        "capo_connect.types.extraction_definition_id.ExtractionDefinitionId"
    )
    """<p>The identifier of the extraction definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExtractionDefinitionResponse) -> dict:
    out: dict = {}
    out["ExtractionDefinitionArn"] = value["extraction_definition_arn"]
    out["ExtractionDefinitionId"] = value["extraction_definition_id"]
    return out


def deserialize_json(data: dict) -> CreateExtractionDefinitionResponse:
    out: CreateExtractionDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExtractionDefinitionArn") is not None:
        out["extraction_definition_arn"] = data["ExtractionDefinitionArn"]
    else:
        out["extraction_definition_arn"] = ""
    if data.get("ExtractionDefinitionId") is not None:
        out["extraction_definition_id"] = data["ExtractionDefinitionId"]
    else:
        out["extraction_definition_id"] = ""
    return out
