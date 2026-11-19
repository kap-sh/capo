"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StringCriteriaCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.comparison_operator
    import capo_compute_optimizer_automation.types.string_criteria_values


class StringCriteriaCondition(TypedDict, closed=True):
    comparison: NotRequired[
        "capo_compute_optimizer_automation.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The comparison operator used to evaluate the attribute against the specified values.</p>"""
    values: NotRequired[
        "capo_compute_optimizer_automation.types.string_criteria_values.StringCriteriaValues"
    ]
    """<p>List of string values to compare against when applying the criteria condition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringCriteriaCondition) -> dict:
    out: dict = {}
    if "comparison" in value:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.serialize_aws_json_1_0(
                value["comparison"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer_automation.types.string_criteria_values

        out["values"] = (
            capo_compute_optimizer_automation.types.string_criteria_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StringCriteriaCondition:
    out: StringCriteriaCondition = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.deserialize_aws_json_1_0(
                data["comparison"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_values

        out["values"] = (
            capo_compute_optimizer_automation.types.string_criteria_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringCriteriaCondition) -> dict:
    out: dict = {}
    if "comparison" in value:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.serialize_cbor(
                value["comparison"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer_automation.types.string_criteria_values

        out["values"] = (
            capo_compute_optimizer_automation.types.string_criteria_values.serialize_cbor(
                value["values"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StringCriteriaCondition:
    out: StringCriteriaCondition = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.deserialize_cbor(
                data["comparison"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer_automation.types.string_criteria_values

        out["values"] = (
            capo_compute_optimizer_automation.types.string_criteria_values.deserialize_cbor(
                data["values"]
            )
        )
    return out
