"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#IncrementalTrainingDataChannelOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.model_training_data_channel_name
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.uuid


class IncrementalTrainingDataChannelOutput(TypedDict, closed=True):
    channel_name: "capo_cleanroomsml.types.model_training_data_channel_name.ModelTrainingDataChannelName"
    """<p>The name of the incremental training data channel that was used.</p>"""
    version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model that was used for incremental training.</p>"""
    model_name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the base trained model that was used for incremental training.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalTrainingDataChannelOutput) -> dict:
    out: dict = {}
    out["channelName"] = value["channel_name"]
    if "version_identifier" in value:
        out["versionIdentifier"] = value["version_identifier"]
    out["modelName"] = value["model_name"]
    return out


def deserialize_json(data: dict) -> IncrementalTrainingDataChannelOutput:
    out: IncrementalTrainingDataChannelOutput = {}  # type: ignore[typeddict-item]
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    else:
        out["channel_name"] = ""
    if data.get("versionIdentifier") is not None:
        out["version_identifier"] = data["versionIdentifier"]
    if data.get("modelName") is not None:
        out["model_name"] = data["modelName"]
    else:
        out["model_name"] = ""
    return out
