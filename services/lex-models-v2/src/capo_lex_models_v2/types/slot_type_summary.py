"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.slot_type_category
    import capo_lex_models_v2.types.slot_type_signature
    import capo_lex_models_v2.types.timestamp


class SlotTypeSummary(TypedDict, closed=True):
    slot_type_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier assigned to the slot type.</p>"""
    slot_type_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of the slot type.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the slot type.</p>"""
    parent_slot_type_signature: NotRequired[
        "capo_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
    ]
    """<p>If the slot type is derived from a built-on slot type, the name of the parent slot type.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the slot type was last updated.</p>"""
    slot_type_category: NotRequired[
        "capo_lex_models_v2.types.slot_type_category.SlotTypeCategory"
    ]
    """<p>Indicates the type of the slot type.</p> <ul> <li> <p> <code>Custom</code> - A slot type that you created using custom values. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/custom-slot-types.html">Creating custom slot types</a>.</p> </li> <li> <p> <code>Extended</code> - A slot type created by extending the <code>AMAZON.AlphaNumeric</code> built-in slot type. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-alphanumerice.html"> <code>AMAZON.AlphaNumeric</code> </a>.</p> </li> <li> <p> <code>ExternalGrammar</code> - A slot type using a custom GRXML grammar to define values. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/building-grxml.html">Using a custom grammar slot type</a>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeSummary) -> dict:
    out: dict = {}
    if "slot_type_id" in value:
        out["slotTypeId"] = value["slot_type_id"]
    if "slot_type_name" in value:
        out["slotTypeName"] = value["slot_type_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parent_slot_type_signature" in value:
        out["parentSlotTypeSignature"] = value["parent_slot_type_signature"]
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    if "slot_type_category" in value:
        import capo_lex_models_v2.types.slot_type_category

        out["slotTypeCategory"] = (
            capo_lex_models_v2.types.slot_type_category.serialize_json(
                value["slot_type_category"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlotTypeSummary:
    out: SlotTypeSummary = {}  # type: ignore[typeddict-item]
    if data.get("slotTypeId") is not None:
        out["slot_type_id"] = data["slotTypeId"]
    if data.get("slotTypeName") is not None:
        out["slot_type_name"] = data["slotTypeName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("parentSlotTypeSignature") is not None:
        out["parent_slot_type_signature"] = data["parentSlotTypeSignature"]
    if data.get("lastUpdatedDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if data.get("slotTypeCategory") is not None:
        import capo_lex_models_v2.types.slot_type_category

        out["slot_type_category"] = (
            capo_lex_models_v2.types.slot_type_category.deserialize_json(
                data["slotTypeCategory"]
            )
        )
    return out
