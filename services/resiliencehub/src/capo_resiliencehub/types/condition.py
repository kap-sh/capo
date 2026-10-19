"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.condition_operator_type
    import capo_resiliencehub.types.string255


class Condition(TypedDict, closed=True):
    field: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the field in the metric.</p>"""
    operator: "capo_resiliencehub.types.condition_operator_type.ConditionOperatorType"
    """<p>Indicates the type of operator or comparison to be used when evaluating a condition against the specified field. </p>"""
    value: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Indicates the value or data against which a condition is evaluated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    import capo_resiliencehub.types.condition_operator_type

    out["operator"] = capo_resiliencehub.types.condition_operator_type.serialize_json(
        value["operator"]
    )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    else:
        out["field"] = ""
    if data.get("operator") is not None:
        import capo_resiliencehub.types.condition_operator_type

        out["operator"] = (
            capo_resiliencehub.types.condition_operator_type.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_resiliencehub.types.condition_operator_type.ConditionOperatorType", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
