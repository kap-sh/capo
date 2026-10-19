"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteFoundationModelAgreementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_model_id


class DeleteFoundationModelAgreementRequest(TypedDict, closed=True):
    model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>Model Id of the model access to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFoundationModelAgreementRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> DeleteFoundationModelAgreementRequest:
    out: DeleteFoundationModelAgreementRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    return out
