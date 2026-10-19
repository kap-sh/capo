"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValueSelectionSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.advanced_recognition_setting
    import capo_lex_models_v2.types.slot_value_regex_filter
    import capo_lex_models_v2.types.slot_value_resolution_strategy


class SlotValueSelectionSetting(TypedDict, closed=True):
    resolution_strategy: "capo_lex_models_v2.types.slot_value_resolution_strategy.SlotValueResolutionStrategy"
    """<p>Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:</p> <ul> <li> <p> <code>ORIGINAL_VALUE</code> - Returns the value entered by the user, if the user value is similar to the slot value.</p> </li> <li> <p> <code>TOP_RESOLUTION</code> - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.</p> </li> </ul> <p>If you don't specify the <code>valueSelectionStrategy</code>, the default is <code>ORIGINAL_VALUE</code>.</p>"""
    regex_filter: NotRequired[
        "capo_lex_models_v2.types.slot_value_regex_filter.SlotValueRegexFilter"
    ]
    """<p>A regular expression used to validate the value of a slot.</p>"""
    advanced_recognition_setting: NotRequired[
        "capo_lex_models_v2.types.advanced_recognition_setting.AdvancedRecognitionSetting"
    ]
    """<p>Provides settings that enable advanced recognition settings for slot values. You can use this to enable using slot values as a custom vocabulary for recognizing user utterances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotValueSelectionSetting) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.slot_value_resolution_strategy

    out["resolutionStrategy"] = (
        capo_lex_models_v2.types.slot_value_resolution_strategy.serialize_json(
            value["resolution_strategy"]
        )
    )
    if "regex_filter" in value:
        import capo_lex_models_v2.types.slot_value_regex_filter

        out["regexFilter"] = (
            capo_lex_models_v2.types.slot_value_regex_filter.serialize_json(
                value["regex_filter"]
            )
        )
    if "advanced_recognition_setting" in value:
        import capo_lex_models_v2.types.advanced_recognition_setting

        out["advancedRecognitionSetting"] = (
            capo_lex_models_v2.types.advanced_recognition_setting.serialize_json(
                value["advanced_recognition_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlotValueSelectionSetting:
    out: SlotValueSelectionSetting = {}  # type: ignore[typeddict-item]
    if data.get("resolutionStrategy") is not None:
        import capo_lex_models_v2.types.slot_value_resolution_strategy

        out["resolution_strategy"] = (
            capo_lex_models_v2.types.slot_value_resolution_strategy.deserialize_json(
                data["resolutionStrategy"]
            )
        )
    else:
        import typing

        out["resolution_strategy"] = typing.cast(
            "capo_lex_models_v2.types.slot_value_resolution_strategy.SlotValueResolutionStrategy",
            "",
        )
    if data.get("regexFilter") is not None:
        import capo_lex_models_v2.types.slot_value_regex_filter

        out["regex_filter"] = (
            capo_lex_models_v2.types.slot_value_regex_filter.deserialize_json(
                data["regexFilter"]
            )
        )
    if data.get("advancedRecognitionSetting") is not None:
        import capo_lex_models_v2.types.advanced_recognition_setting

        out["advanced_recognition_setting"] = (
            capo_lex_models_v2.types.advanced_recognition_setting.deserialize_json(
                data["advancedRecognitionSetting"]
            )
        )
    return out
