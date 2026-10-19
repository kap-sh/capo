"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ModelInferenceDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.ml_input_channel_arn


class ModelInferenceDataSource(TypedDict, closed=True):
    ml_input_channel_arn: (
        "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel for this model inference data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelInferenceDataSource) -> dict:
    out: dict = {}
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    return out


def deserialize_json(data: dict) -> ModelInferenceDataSource:
    out: ModelInferenceDataSource = {}  # type: ignore[typeddict-item]
    if data.get("mlInputChannelArn") is not None:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        out["ml_input_channel_arn"] = ""
    return out
