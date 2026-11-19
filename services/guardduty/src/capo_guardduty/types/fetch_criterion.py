"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchCriterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_criterion_condition
    import capo_guardduty.types.fetch_field_name
    import capo_guardduty.types.fetch_field_values


class FetchCriterion(TypedDict, closed=True):
    field: NotRequired["capo_guardduty.types.fetch_field_name.FetchFieldName"]
    """<p>The name of the field that the condition applies to.</p>"""
    condition: NotRequired[
        "capo_guardduty.types.fetch_criterion_condition.FetchCriterionCondition"
    ]
    """<p>The comparison operator of the condition. Possible values are <code>EQUALS</code>, <code>NOT_EQUALS</code>, <code>GREATER_THAN</code>, <code>GREATER_THAN_OR_EQUAL</code>, <code>LESS_THAN</code>, and <code>LESS_THAN_OR_EQUAL</code>.</p>"""
    values: NotRequired["capo_guardduty.types.fetch_field_values.FetchFieldValues"]
    """<p>The values that the field is compared against. Numeric and Boolean values are represented as strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FetchCriterion) -> dict:
    out: dict = {}
    if "field" in value:
        out["field"] = value["field"]
    if "condition" in value:
        import capo_guardduty.types.fetch_criterion_condition

        out["condition"] = (
            capo_guardduty.types.fetch_criterion_condition.serialize_json(
                value["condition"]
            )
        )
    if "values" in value:
        import capo_guardduty.types.fetch_field_values

        out["values"] = capo_guardduty.types.fetch_field_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> FetchCriterion:
    out: FetchCriterion = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    if data.get("condition") is not None:
        import capo_guardduty.types.fetch_criterion_condition

        out["condition"] = (
            capo_guardduty.types.fetch_criterion_condition.deserialize_json(
                data["condition"]
            )
        )
    if data.get("values") is not None:
        import capo_guardduty.types.fetch_field_values

        out["values"] = capo_guardduty.types.fetch_field_values.deserialize_json(
            data["values"]
        )
    return out
