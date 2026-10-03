"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateSlotTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.composite_slot_type_setting
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.external_source_setting
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.slot_type_signature
    import capo_lex_models_v2.types.slot_type_values
    import capo_lex_models_v2.types.slot_value_selection_setting


class UpdateSlotTypeRequest(TypedDict, closed=True):
    slot_type_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the slot type to update.</p>"""
    slot_type_name: "capo_lex_models_v2.types.name.Name"
    """<p>The new name of the slot type.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The new description of the slot type.</p>"""
    slot_type_values: NotRequired[
        "capo_lex_models_v2.types.slot_type_values.SlotTypeValues"
    ]
    """<p>A new list of values and their optional synonyms that define the values that the slot type can take.</p>"""
    value_selection_setting: NotRequired[
        "capo_lex_models_v2.types.slot_value_selection_setting.SlotValueSelectionSetting"
    ]
    """<p>The strategy that Amazon Lex should use when deciding on a value from the list of slot type values.</p>"""
    parent_slot_type_signature: NotRequired[
        "capo_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
    ]
    """<p>The new built-in slot type that should be used as the parent of this slot type.</p>"""
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot that contains the slot type.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot that contains the slot type. Must be <code>DRAFT</code>.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale that contains the slot type. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    external_source_setting: NotRequired[
        "capo_lex_models_v2.types.external_source_setting.ExternalSourceSetting"
    ]
    composite_slot_type_setting: NotRequired[
        "capo_lex_models_v2.types.composite_slot_type_setting.CompositeSlotTypeSetting"
    ]
    """<p>Specifications for a composite slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSlotTypeRequest) -> dict:
    out: dict = {}
    out["slotTypeName"] = value["slot_type_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slot_type_values" in value:
        import capo_lex_models_v2.types.slot_type_values

        out["slotTypeValues"] = (
            capo_lex_models_v2.types.slot_type_values.serialize_json(
                value["slot_type_values"]
            )
        )
    if "value_selection_setting" in value:
        import capo_lex_models_v2.types.slot_value_selection_setting

        out["valueSelectionSetting"] = (
            capo_lex_models_v2.types.slot_value_selection_setting.serialize_json(
                value["value_selection_setting"]
            )
        )
    if "parent_slot_type_signature" in value:
        out["parentSlotTypeSignature"] = value["parent_slot_type_signature"]
    if "external_source_setting" in value:
        import capo_lex_models_v2.types.external_source_setting

        out["externalSourceSetting"] = (
            capo_lex_models_v2.types.external_source_setting.serialize_json(
                value["external_source_setting"]
            )
        )
    if "composite_slot_type_setting" in value:
        import capo_lex_models_v2.types.composite_slot_type_setting

        out["compositeSlotTypeSetting"] = (
            capo_lex_models_v2.types.composite_slot_type_setting.serialize_json(
                value["composite_slot_type_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSlotTypeRequest:
    out: UpdateSlotTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("slotTypeName") is not None:
        out["slot_type_name"] = data["slotTypeName"]
    else:
        raise DeserializationError("UpdateSlotTypeRequest.slot_type_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("slotTypeValues") is not None:
        import capo_lex_models_v2.types.slot_type_values

        out["slot_type_values"] = (
            capo_lex_models_v2.types.slot_type_values.deserialize_json(
                data["slotTypeValues"]
            )
        )
    if data.get("valueSelectionSetting") is not None:
        import capo_lex_models_v2.types.slot_value_selection_setting

        out["value_selection_setting"] = (
            capo_lex_models_v2.types.slot_value_selection_setting.deserialize_json(
                data["valueSelectionSetting"]
            )
        )
    if data.get("parentSlotTypeSignature") is not None:
        out["parent_slot_type_signature"] = data["parentSlotTypeSignature"]
    if data.get("externalSourceSetting") is not None:
        import capo_lex_models_v2.types.external_source_setting

        out["external_source_setting"] = (
            capo_lex_models_v2.types.external_source_setting.deserialize_json(
                data["externalSourceSetting"]
            )
        )
    if data.get("compositeSlotTypeSetting") is not None:
        import capo_lex_models_v2.types.composite_slot_type_setting

        out["composite_slot_type_setting"] = (
            capo_lex_models_v2.types.composite_slot_type_setting.deserialize_json(
                data["compositeSlotTypeSetting"]
            )
        )
    return out
