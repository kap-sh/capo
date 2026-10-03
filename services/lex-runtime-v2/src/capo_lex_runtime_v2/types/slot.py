"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Slot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.shape
    import capo_lex_runtime_v2.types.slots
    import capo_lex_runtime_v2.types.value
    import capo_lex_runtime_v2.types.values


class Slot(TypedDict, closed=True):
    value: NotRequired["capo_lex_runtime_v2.types.value.Value"]
    """<p>The current value of the slot.</p>"""
    shape: NotRequired["capo_lex_runtime_v2.types.shape.Shape"]
    """<p>When the <code>shape</code> value is <code>List</code>, it indicates that the <code>values</code> field contains a list of slot values. When the value is <code>Scalar</code>, it indicates that the <code>value</code> field contains a single value.</p>"""
    values: NotRequired["capo_lex_runtime_v2.types.values.Values"]
    """<p>A list of one or more values that the user provided for the slot. For example, if a for a slot that elicits pizza toppings, the values might be "pepperoni" and "pineapple." </p>"""
    sub_slots: NotRequired["capo_lex_runtime_v2.types.slots.Slots"]
    """<p>The constituent sub slots of a composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Slot) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_lex_runtime_v2.types.value

        out["value"] = capo_lex_runtime_v2.types.value.serialize_json(value["value"])
    if "shape" in value:
        import capo_lex_runtime_v2.types.shape

        out["shape"] = capo_lex_runtime_v2.types.shape.serialize_json(value["shape"])
    if "values" in value:
        import capo_lex_runtime_v2.types.values

        out["values"] = capo_lex_runtime_v2.types.values.serialize_json(value["values"])
    if "sub_slots" in value:
        import capo_lex_runtime_v2.types.slots

        out["subSlots"] = capo_lex_runtime_v2.types.slots.serialize_json(
            value["sub_slots"]
        )
    return out


def deserialize_json(data: dict) -> Slot:
    out: Slot = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_lex_runtime_v2.types.value

        out["value"] = capo_lex_runtime_v2.types.value.deserialize_json(data["value"])
    if data.get("shape") is not None:
        import capo_lex_runtime_v2.types.shape

        out["shape"] = capo_lex_runtime_v2.types.shape.deserialize_json(data["shape"])
    if data.get("values") is not None:
        import capo_lex_runtime_v2.types.values

        out["values"] = capo_lex_runtime_v2.types.values.deserialize_json(
            data["values"]
        )
    if data.get("subSlots") is not None:
        import capo_lex_runtime_v2.types.slots

        out["sub_slots"] = capo_lex_runtime_v2.types.slots.deserialize_json(
            data["subSlots"]
        )
    return out
