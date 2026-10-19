"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateConfiguredAudienceModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_arn


class CreateConfiguredAudienceModelResponse(TypedDict, closed=True):
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredAudienceModelResponse) -> dict:
    out: dict = {}
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    return out


def deserialize_json(data: dict) -> CreateConfiguredAudienceModelResponse:
    out: CreateConfiguredAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuredAudienceModelArn") is not None:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        out["configured_audience_model_arn"] = ""
    return out
