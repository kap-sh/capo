"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValueElicitationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.prompt_specification
    import capo_lex_models_v2.types.sample_utterances_list
    import capo_lex_models_v2.types.slot_capture_setting
    import capo_lex_models_v2.types.slot_constraint
    import capo_lex_models_v2.types.slot_default_value_specification
    import capo_lex_models_v2.types.slot_resolution_setting
    import capo_lex_models_v2.types.wait_and_continue_specification


class SlotValueElicitationSetting(TypedDict, closed=True):
    default_value_specification: NotRequired[
        "capo_lex_models_v2.types.slot_default_value_specification.SlotDefaultValueSpecification"
    ]
    """<p>A list of default values for a slot. Default values are used when Amazon Lex hasn't determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.</p>"""
    slot_constraint: "capo_lex_models_v2.types.slot_constraint.SlotConstraint"
    """<p>Specifies whether the slot is required or optional.</p>"""
    prompt_specification: NotRequired[
        "capo_lex_models_v2.types.prompt_specification.PromptSpecification"
    ]
    """<p>The prompt that Amazon Lex uses to elicit the slot value from the user.</p>"""
    sample_utterances: NotRequired[
        "capo_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
    ]
    """<p>If you know a specific pattern that users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.</p>"""
    wait_and_continue_specification: NotRequired[
        "capo_lex_models_v2.types.wait_and_continue_specification.WaitAndContinueSpecification"
    ]
    slot_capture_setting: NotRequired[
        "capo_lex_models_v2.types.slot_capture_setting.SlotCaptureSetting"
    ]
    """<p>Specifies the settings that Amazon Lex uses when a slot value is successfully entered by a user.</p>"""
    slot_resolution_setting: NotRequired[
        "capo_lex_models_v2.types.slot_resolution_setting.SlotResolutionSetting"
    ]
    """<p>An object containing information about whether assisted slot resolution is turned on for the slot or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotValueElicitationSetting) -> dict:
    out: dict = {}
    if "default_value_specification" in value:
        import capo_lex_models_v2.types.slot_default_value_specification

        out["defaultValueSpecification"] = (
            capo_lex_models_v2.types.slot_default_value_specification.serialize_json(
                value["default_value_specification"]
            )
        )
    import capo_lex_models_v2.types.slot_constraint

    out["slotConstraint"] = capo_lex_models_v2.types.slot_constraint.serialize_json(
        value["slot_constraint"]
    )
    if "prompt_specification" in value:
        import capo_lex_models_v2.types.prompt_specification

        out["promptSpecification"] = (
            capo_lex_models_v2.types.prompt_specification.serialize_json(
                value["prompt_specification"]
            )
        )
    if "sample_utterances" in value:
        import capo_lex_models_v2.types.sample_utterances_list

        out["sampleUtterances"] = (
            capo_lex_models_v2.types.sample_utterances_list.serialize_json(
                value["sample_utterances"]
            )
        )
    if "wait_and_continue_specification" in value:
        import capo_lex_models_v2.types.wait_and_continue_specification

        out["waitAndContinueSpecification"] = (
            capo_lex_models_v2.types.wait_and_continue_specification.serialize_json(
                value["wait_and_continue_specification"]
            )
        )
    if "slot_capture_setting" in value:
        import capo_lex_models_v2.types.slot_capture_setting

        out["slotCaptureSetting"] = (
            capo_lex_models_v2.types.slot_capture_setting.serialize_json(
                value["slot_capture_setting"]
            )
        )
    if "slot_resolution_setting" in value:
        import capo_lex_models_v2.types.slot_resolution_setting

        out["slotResolutionSetting"] = (
            capo_lex_models_v2.types.slot_resolution_setting.serialize_json(
                value["slot_resolution_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlotValueElicitationSetting:
    out: SlotValueElicitationSetting = {}  # type: ignore[typeddict-item]
    if data.get("defaultValueSpecification") is not None:
        import capo_lex_models_v2.types.slot_default_value_specification

        out["default_value_specification"] = (
            capo_lex_models_v2.types.slot_default_value_specification.deserialize_json(
                data["defaultValueSpecification"]
            )
        )
    if data.get("slotConstraint") is not None:
        import capo_lex_models_v2.types.slot_constraint

        out["slot_constraint"] = (
            capo_lex_models_v2.types.slot_constraint.deserialize_json(
                data["slotConstraint"]
            )
        )
    else:
        import typing

        out["slot_constraint"] = typing.cast(
            "capo_lex_models_v2.types.slot_constraint.SlotConstraint", ""
        )
    if data.get("promptSpecification") is not None:
        import capo_lex_models_v2.types.prompt_specification

        out["prompt_specification"] = (
            capo_lex_models_v2.types.prompt_specification.deserialize_json(
                data["promptSpecification"]
            )
        )
    if data.get("sampleUtterances") is not None:
        import capo_lex_models_v2.types.sample_utterances_list

        out["sample_utterances"] = (
            capo_lex_models_v2.types.sample_utterances_list.deserialize_json(
                data["sampleUtterances"]
            )
        )
    if data.get("waitAndContinueSpecification") is not None:
        import capo_lex_models_v2.types.wait_and_continue_specification

        out["wait_and_continue_specification"] = (
            capo_lex_models_v2.types.wait_and_continue_specification.deserialize_json(
                data["waitAndContinueSpecification"]
            )
        )
    if data.get("slotCaptureSetting") is not None:
        import capo_lex_models_v2.types.slot_capture_setting

        out["slot_capture_setting"] = (
            capo_lex_models_v2.types.slot_capture_setting.deserialize_json(
                data["slotCaptureSetting"]
            )
        )
    if data.get("slotResolutionSetting") is not None:
        import capo_lex_models_v2.types.slot_resolution_setting

        out["slot_resolution_setting"] = (
            capo_lex_models_v2.types.slot_resolution_setting.deserialize_json(
                data["slotResolutionSetting"]
            )
        )
    return out
