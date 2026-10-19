"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageStandardGenerativeField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.image_standard_generative_field_types
    import capo_bedrock_data_automation.types.state


class ImageStandardGenerativeField(TypedDict, closed=True):
    state: "capo_bedrock_data_automation.types.state.State"
    types: NotRequired[
        "capo_bedrock_data_automation.types.image_standard_generative_field_types.ImageStandardGenerativeFieldTypes"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ImageStandardGenerativeField) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.state

    out["state"] = capo_bedrock_data_automation.types.state.serialize_json(
        value["state"]
    )
    if "types" in value:
        import capo_bedrock_data_automation.types.image_standard_generative_field_types

        out["types"] = (
            capo_bedrock_data_automation.types.image_standard_generative_field_types.serialize_json(
                value["types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageStandardGenerativeField:
    out: ImageStandardGenerativeField = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_bedrock_data_automation.types.state

        out["state"] = capo_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast("capo_bedrock_data_automation.types.state.State", "")
    if data.get("types") is not None:
        import capo_bedrock_data_automation.types.image_standard_generative_field_types

        out["types"] = (
            capo_bedrock_data_automation.types.image_standard_generative_field_types.deserialize_json(
                data["types"]
            )
        )
    return out
