"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValueOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_shape
    import capo_lex_models_v2.types.slot_value
    import capo_lex_models_v2.types.slot_values


class SlotValueOverride(TypedDict, closed=True):
    shape: NotRequired["capo_lex_models_v2.types.slot_shape.SlotShape"]
    """<p>When the shape value is <code>List</code>, it indicates that the <code>values</code> field contains a list of slot values. When the value is <code>Scalar</code>, it indicates that the <code>value</code> field contains a single value.</p>"""
    value: NotRequired["capo_lex_models_v2.types.slot_value.SlotValue"]
    """<p>The current value of the slot.</p>"""
    values: NotRequired["capo_lex_models_v2.types.slot_values.SlotValues"]
    """<p>A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be "pepperoni" and "pineapple."</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotValueOverride) -> dict:
    out: dict = {}
    if "shape" in value:
        import capo_lex_models_v2.types.slot_shape

        out["shape"] = capo_lex_models_v2.types.slot_shape.serialize_json(
            value["shape"]
        )
    if "value" in value:
        import capo_lex_models_v2.types.slot_value

        out["value"] = capo_lex_models_v2.types.slot_value.serialize_json(
            value["value"]
        )
    if "values" in value:
        import capo_lex_models_v2.types.slot_values

        out["values"] = capo_lex_models_v2.types.slot_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> SlotValueOverride:
    out: SlotValueOverride = {}  # type: ignore[typeddict-item]
    if data.get("shape") is not None:
        import capo_lex_models_v2.types.slot_shape

        out["shape"] = capo_lex_models_v2.types.slot_shape.deserialize_json(
            data["shape"]
        )
    if data.get("value") is not None:
        import capo_lex_models_v2.types.slot_value

        out["value"] = capo_lex_models_v2.types.slot_value.deserialize_json(
            data["value"]
        )
    if data.get("values") is not None:
        import capo_lex_models_v2.types.slot_values

        out["values"] = capo_lex_models_v2.types.slot_values.deserialize_json(
            data["values"]
        )
    return out
