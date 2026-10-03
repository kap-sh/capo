"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Criterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.value_list


class Criterion(TypedDict, closed=True):
    eq: NotRequired["capo_accessanalyzer.types.value_list.ValueList"]
    """<p>An "equals" operator to match for the filter used to create the rule.</p>"""
    neq: NotRequired["capo_accessanalyzer.types.value_list.ValueList"]
    """<p>A "not equals" operator to match for the filter used to create the rule.</p>"""
    contains: NotRequired["capo_accessanalyzer.types.value_list.ValueList"]
    """<p>A "contains" operator to match for the filter used to create the rule.</p>"""
    exists: NotRequired["bool"]
    """<p>An "exists" operator to match for the filter used to create the rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Criterion) -> dict:
    out: dict = {}
    if "eq" in value:
        import capo_accessanalyzer.types.value_list

        out["eq"] = capo_accessanalyzer.types.value_list.serialize_json(value["eq"])
    if "neq" in value:
        import capo_accessanalyzer.types.value_list

        out["neq"] = capo_accessanalyzer.types.value_list.serialize_json(value["neq"])
    if "contains" in value:
        import capo_accessanalyzer.types.value_list

        out["contains"] = capo_accessanalyzer.types.value_list.serialize_json(
            value["contains"]
        )
    if "exists" in value:
        out["exists"] = value["exists"]
    return out


def deserialize_json(data: dict) -> Criterion:
    out: Criterion = {}  # type: ignore[typeddict-item]
    if data.get("eq") is not None:
        import capo_accessanalyzer.types.value_list

        out["eq"] = capo_accessanalyzer.types.value_list.deserialize_json(data["eq"])
    if data.get("neq") is not None:
        import capo_accessanalyzer.types.value_list

        out["neq"] = capo_accessanalyzer.types.value_list.deserialize_json(data["neq"])
    if data.get("contains") is not None:
        import capo_accessanalyzer.types.value_list

        out["contains"] = capo_accessanalyzer.types.value_list.deserialize_json(
            data["contains"]
        )
    if data.get("exists") is not None:
        out["exists"] = data["exists"]
    return out
