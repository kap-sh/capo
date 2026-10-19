"""Generated from Smithy shape ``com.amazonaws.connectcases#HiddenCaseRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.boolean_condition_list


class HiddenCaseRule(TypedDict, closed=True):
    default_value: "bool"
    """<p>Whether the field is hidden when no conditions match.</p>"""
    conditions: "capo_connectcases.types.boolean_condition_list.BooleanConditionList"
    """<p>A list of conditions that determine field visibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HiddenCaseRule) -> dict:
    out: dict = {}
    out["defaultValue"] = value["default_value"]
    import capo_connectcases.types.boolean_condition_list

    out["conditions"] = capo_connectcases.types.boolean_condition_list.serialize_json(
        value["conditions"]
    )
    return out


def deserialize_json(data: dict) -> HiddenCaseRule:
    out: HiddenCaseRule = {}  # type: ignore[typeddict-item]
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
