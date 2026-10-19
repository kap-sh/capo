"""Generated from Smithy shape ``com.amazonaws.connectcases#RequiredCaseRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.boolean_condition_list


class RequiredCaseRule(TypedDict, closed=True):
    default_value: "bool"
    """<p>The value of the rule (that is, whether the field is required) should none of the conditions evaluate to true.</p>"""
    conditions: "capo_connectcases.types.boolean_condition_list.BooleanConditionList"
    """<p>List of conditions for the required rule; the first condition to evaluate to true dictates the value of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequiredCaseRule) -> dict:
    out: dict = {}
    out["defaultValue"] = value["default_value"]
    import capo_connectcases.types.boolean_condition_list

    out["conditions"] = capo_connectcases.types.boolean_condition_list.serialize_json(
        value["conditions"]
    )
    return out


def deserialize_json(data: dict) -> RequiredCaseRule:
    out: RequiredCaseRule = {}  # type: ignore[typeddict-item]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    else:
        out["default_value"] = False
    if data.get("conditions") is not None:
        import capo_connectcases.types.boolean_condition_list

        out["conditions"] = (
            capo_connectcases.types.boolean_condition_list.deserialize_json(
                data["conditions"]
            )
        )
    else:
        out["conditions"] = []
    return out
