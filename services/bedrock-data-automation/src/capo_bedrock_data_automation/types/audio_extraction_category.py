"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioExtractionCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.audio_extraction_category_type_configuration
    import capo_bedrock_data_automation.types.audio_extraction_category_types
    import capo_bedrock_data_automation.types.state


class AudioExtractionCategory(TypedDict, closed=True):
    state: "capo_bedrock_data_automation.types.state.State"
    types: NotRequired[
        "capo_bedrock_data_automation.types.audio_extraction_category_types.AudioExtractionCategoryTypes"
    ]
    type_configuration: NotRequired[
        "capo_bedrock_data_automation.types.audio_extraction_category_type_configuration.AudioExtractionCategoryTypeConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionCategory) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.state

    out["state"] = capo_bedrock_data_automation.types.state.serialize_json(
        value["state"]
    )
    if "types" in value:
        import capo_bedrock_data_automation.types.audio_extraction_category_types

        out["types"] = (
            capo_bedrock_data_automation.types.audio_extraction_category_types.serialize_json(
                value["types"]
            )
        )
    if "type_configuration" in value:
        import capo_bedrock_data_automation.types.audio_extraction_category_type_configuration

        out["typeConfiguration"] = (
            capo_bedrock_data_automation.types.audio_extraction_category_type_configuration.serialize_json(
                value["type_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioExtractionCategory:
    out: AudioExtractionCategory = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_bedrock_data_automation.types.state

        out["state"] = capo_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast("capo_bedrock_data_automation.types.state.State", "")
    if data.get("types") is not None:
        import capo_bedrock_data_automation.types.audio_extraction_category_types

        out["types"] = (
            capo_bedrock_data_automation.types.audio_extraction_category_types.deserialize_json(
                data["types"]
            )
        )
    if data.get("typeConfiguration") is not None:
        import capo_bedrock_data_automation.types.audio_extraction_category_type_configuration

        out["type_configuration"] = (
            capo_bedrock_data_automation.types.audio_extraction_category_type_configuration.deserialize_json(
                data["typeConfiguration"]
            )
        )
    return out
