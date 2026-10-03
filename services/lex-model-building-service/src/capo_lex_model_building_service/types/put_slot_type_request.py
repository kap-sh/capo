"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#PutSlotTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.boolean
    import capo_lex_model_building_service.types.custom_or_builtin_slot_type_name
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.enumeration_values
    import capo_lex_model_building_service.types.slot_type_configurations
    import capo_lex_model_building_service.types.slot_type_name
    import capo_lex_model_building_service.types.slot_value_selection_strategy
    import capo_lex_model_building_service.types.string


class PutSlotTypeRequest(TypedDict, closed=True):
    name: "capo_lex_model_building_service.types.slot_type_name.SlotTypeName"
    """<p>The name of the slot type. The name is <i>not</i> case sensitive. </p> <p>The name can't match a built-in slot type name, or a built-in slot type name with "AMAZON." removed. For example, because there is a built-in slot type called <code>AMAZON.DATE</code>, you can't create a custom slot type called <code>DATE</code>.</p> <p>For a list of built-in slot types, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference">Slot Type Reference</a> in the <i>Alexa Skills Kit</i>.</p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the slot type.</p>"""
    enumeration_values: NotRequired[
        "capo_lex_model_building_service.types.enumeration_values.EnumerationValues"
    ]
    """<p>A list of <code>EnumerationValue</code> objects that defines the values that the slot type can take. Each value can have a list of <code>synonyms</code>, which are additional values that help train the machine learning model about the values that it resolves for a slot. </p> <p>A regular expression slot type doesn't require enumeration values. All other slot types require a list of enumeration values.</p> <p>When Amazon Lex resolves a slot value, it generates a resolution list that contains up to five possible values for the slot. If you are using a Lambda function, this resolution list is passed to the function. If you are not using a Lambda function you can choose to return the value that the user entered or the first value in the resolution list as the slot value. The <code>valueSelectionStrategy</code> field indicates the option to use. </p>"""
    checksum: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>Identifies a specific revision of the <code>$LATEST</code> version.</p> <p>When you create a new slot type, leave the <code>checksum</code> field blank. If you specify a checksum you get a <code>BadRequestException</code> exception.</p> <p>When you want to update a slot type, set the <code>checksum</code> field to the checksum of the most recent revision of the <code>$LATEST</code> version. If you don't specify the <code> checksum</code> field, or if the checksum does not match the <code>$LATEST</code> version, you get a <code>PreconditionFailedException</code> exception.</p>"""
    value_selection_strategy: NotRequired[
        "capo_lex_model_building_service.types.slot_value_selection_strategy.SlotValueSelectionStrategy"
    ]
    """<p>Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:</p> <ul> <li> <p> <code>ORIGINAL_VALUE</code> - Returns the value entered by the user, if the user value is similar to the slot value.</p> </li> <li> <p> <code>TOP_RESOLUTION</code> - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.</p> </li> </ul> <p>If you don't specify the <code>valueSelectionStrategy</code>, the default is <code>ORIGINAL_VALUE</code>.</p>"""
    create_version: NotRequired["capo_lex_model_building_service.types.boolean.Boolean"]
    """<p>When set to <code>true</code> a new numbered version of the slot type is created. This is the same as calling the <code>CreateSlotTypeVersion</code> operation. If you do not specify <code>createVersion</code>, the default is <code>false</code>.</p>"""
    parent_slot_type_signature: NotRequired[
        "capo_lex_model_building_service.types.custom_or_builtin_slot_type_name.CustomOrBuiltinSlotTypeName"
    ]
    """<p>The built-in slot type used as the parent of the slot type. When you define a parent slot type, the new slot type has all of the same configuration as the parent.</p> <p>Only <code>AMAZON.AlphaNumeric</code> is supported.</p>"""
    slot_type_configurations: NotRequired[
        "capo_lex_model_building_service.types.slot_type_configurations.SlotTypeConfigurations"
    ]
    """<p>Configuration information that extends the parent built-in slot type. The configuration is added to the settings for the parent slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSlotTypeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "enumeration_values" in value:
        import capo_lex_model_building_service.types.enumeration_values

        out["enumerationValues"] = (
            capo_lex_model_building_service.types.enumeration_values.serialize_json(
                value["enumeration_values"]
            )
        )
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "value_selection_strategy" in value:
        import capo_lex_model_building_service.types.slot_value_selection_strategy

        out["valueSelectionStrategy"] = (
            capo_lex_model_building_service.types.slot_value_selection_strategy.serialize_json(
                value["value_selection_strategy"]
            )
        )
    if "create_version" in value:
        out["createVersion"] = value["create_version"]
    if "parent_slot_type_signature" in value:
        out["parentSlotTypeSignature"] = value["parent_slot_type_signature"]
    if "slot_type_configurations" in value:
        import capo_lex_model_building_service.types.slot_type_configurations

        out["slotTypeConfigurations"] = (
            capo_lex_model_building_service.types.slot_type_configurations.serialize_json(
                value["slot_type_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutSlotTypeRequest:
    out: PutSlotTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("enumerationValues") is not None:
        import capo_lex_model_building_service.types.enumeration_values

        out["enumeration_values"] = (
            capo_lex_model_building_service.types.enumeration_values.deserialize_json(
                data["enumerationValues"]
            )
        )
    if data.get("checksum") is not None:
        out["checksum"] = data["checksum"]
    if data.get("valueSelectionStrategy") is not None:
        import capo_lex_model_building_service.types.slot_value_selection_strategy

        out["value_selection_strategy"] = (
            capo_lex_model_building_service.types.slot_value_selection_strategy.deserialize_json(
                data["valueSelectionStrategy"]
            )
        )
    if data.get("createVersion") is not None:
        out["create_version"] = data["createVersion"]
    if data.get("parentSlotTypeSignature") is not None:
        out["parent_slot_type_signature"] = data["parentSlotTypeSignature"]
    if data.get("slotTypeConfigurations") is not None:
        import capo_lex_model_building_service.types.slot_type_configurations

        out["slot_type_configurations"] = (
            capo_lex_model_building_service.types.slot_type_configurations.deserialize_json(
                data["slotTypeConfigurations"]
            )
        )
    return out
