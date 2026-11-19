"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#IntegerCriteriaCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.comparison_operator
    import capo_compute_optimizer_automation.types.integer_list


class IntegerCriteriaCondition(TypedDict, closed=True):
    comparison: NotRequired[
        "capo_compute_optimizer_automation.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The comparison operator used to evaluate the attribute against the specified values.</p>"""
    values: NotRequired[
        "capo_compute_optimizer_automation.types.integer_list.IntegerList"
    ]
    """<p>The list of integer values to compare against using the specified comparison operator.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IntegerCriteriaCondition) -> dict:
    out: dict = {}
    if "comparison" in value:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.serialize_aws_json_1_0(
                value["comparison"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer_automation.types.integer_list

        out["values"] = (
            capo_compute_optimizer_automation.types.integer_list.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IntegerCriteriaCondition:
    out: IntegerCriteriaCondition = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.deserialize_aws_json_1_0(
                data["comparison"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer_automation.types.integer_list

        out["values"] = (
            capo_compute_optimizer_automation.types.integer_list.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IntegerCriteriaCondition) -> dict:
    out: dict = {}
    if "comparison" in value:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.serialize_cbor(
                value["comparison"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer_automation.types.integer_list

        out["values"] = (
            capo_compute_optimizer_automation.types.integer_list.serialize_cbor(
                value["values"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> IntegerCriteriaCondition:
    out: IntegerCriteriaCondition = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.deserialize_cbor(
                data["comparison"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer_automation.types.integer_list

        out["values"] = (
            capo_compute_optimizer_automation.types.integer_list.deserialize_cbor(
                data["values"]
            )
        )
    return out
