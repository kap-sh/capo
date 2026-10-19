"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateFoundationModelAgreementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_model_id
    import capo_bedrock.types.offer_token


class CreateFoundationModelAgreementRequest(TypedDict, closed=True):
    offer_token: "capo_bedrock.types.offer_token.OfferToken"
    """<p>An offer token encapsulates the information for an offer.</p>"""
    model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId"
    """<p>Model Id of the model for the access request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFoundationModelAgreementRequest) -> dict:
    out: dict = {}
    out["offerToken"] = value["offer_token"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> CreateFoundationModelAgreementRequest:
    out: CreateFoundationModelAgreementRequest = {}  # type: ignore[typeddict-item]
    if data.get("offerToken") is not None:
        out["offer_token"] = data["offerToken"]
    else:
        out["offer_token"] = ""
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    return out
