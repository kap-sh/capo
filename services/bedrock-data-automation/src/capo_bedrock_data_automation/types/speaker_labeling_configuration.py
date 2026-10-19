"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#SpeakerLabelingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.state


class SpeakerLabelingConfiguration(TypedDict, closed=True):
    state: "capo_bedrock_data_automation.types.state.State"


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerLabelingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.state

    out["state"] = capo_bedrock_data_automation.types.state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> SpeakerLabelingConfiguration:
    out: SpeakerLabelingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_bedrock_data_automation.types.state

        out["state"] = capo_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast("capo_bedrock_data_automation.types.state.State", "")
    return out
