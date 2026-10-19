"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateAudienceModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_model_arn


class CreateAudienceModelResponse(TypedDict, closed=True):
    audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAudienceModelResponse) -> dict:
    out: dict = {}
    out["audienceModelArn"] = value["audience_model_arn"]
    return out


def deserialize_json(data: dict) -> CreateAudienceModelResponse:
    out: CreateAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("audienceModelArn") is not None:
        out["audience_model_arn"] = data["audienceModelArn"]
    else:
        out["audience_model_arn"] = ""
    return out
