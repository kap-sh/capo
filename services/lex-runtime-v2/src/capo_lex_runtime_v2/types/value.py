"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Value``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.string_list


class Value(TypedDict, closed=True):
    original_value: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The part of the user's response to the slot elicitation that Amazon Lex V2 determines is relevant to the slot value.</p>"""
    interpreted_value: "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    """<p>The value that Amazon Lex V2 determines for the slot, given the user input. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex V2 choose the first value in the <code>resolvedValues</code> list.</p>"""
    resolved_values: NotRequired["capo_lex_runtime_v2.types.string_list.StringList"]
    """<p>A list of values that Amazon Lex V2 determines are possible resolutions for the user input. The first value matches the <code>interpretedValue</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Value) -> dict:
    out: dict = {}
    if "original_value" in value:
        out["originalValue"] = value["original_value"]
    out["interpretedValue"] = value["interpreted_value"]
    if "resolved_values" in value:
        import capo_lex_runtime_v2.types.string_list

        out["resolvedValues"] = capo_lex_runtime_v2.types.string_list.serialize_json(
            value["resolved_values"]
        )
    return out


def deserialize_json(data: dict) -> Value:
    out: Value = {}  # type: ignore[typeddict-item]
    if data.get("originalValue") is not None:
        out["original_value"] = data["originalValue"]
    if data.get("interpretedValue") is not None:
        out["interpreted_value"] = data["interpretedValue"]
    else:
        out["interpreted_value"] = ""
    if data.get("resolvedValues") is not None:
        import capo_lex_runtime_v2.types.string_list

        out["resolved_values"] = capo_lex_runtime_v2.types.string_list.deserialize_json(
            data["resolvedValues"]
        )
    return out
