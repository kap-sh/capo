"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#UpdateConfiguredAudienceModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_arn


class UpdateConfiguredAudienceModelResponse(TypedDict, closed=True):
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredAudienceModelResponse) -> dict:
    out: dict = {}
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    return out


def deserialize_json(data: dict) -> UpdateConfiguredAudienceModelResponse:
    out: UpdateConfiguredAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuredAudienceModelArn") is not None:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        out["configured_audience_model_arn"] = ""
    return out
