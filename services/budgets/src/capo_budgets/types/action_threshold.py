"""Generated from Smithy shape ``com.amazonaws.budgets#ActionThreshold``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.notification_threshold
    import capo_budgets.types.threshold_type


class ActionThreshold(TypedDict, closed=True):
    action_threshold_value: (
        "capo_budgets.types.notification_threshold.NotificationThreshold"
    )
    action_threshold_type: "capo_budgets.types.threshold_type.ThresholdType"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionThreshold) -> dict:
    out: dict = {}
    out["ActionThresholdValue"] = (
        "NaN"
        if value.get("action_threshold_value", 0)
        != value.get("action_threshold_value", 0)
        else "Infinity"
        if value.get("action_threshold_value", 0) == float("inf")
        else "-Infinity"
        if value.get("action_threshold_value", 0) == float("-inf")
        else value.get("action_threshold_value", 0)
    )
    import capo_budgets.types.threshold_type

    out["ActionThresholdType"] = (
        capo_budgets.types.threshold_type.serialize_aws_json_1_1(
            value["action_threshold_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionThreshold:
    out: ActionThreshold = {}  # type: ignore[typeddict-item]
    if data.get("ActionThresholdValue") is not None:
        out["action_threshold_value"] = float(data["ActionThresholdValue"])
    else:
        out["action_threshold_value"] = 0
    if data.get("ActionThresholdType") is not None:
        import capo_budgets.types.threshold_type

        out["action_threshold_type"] = (
            capo_budgets.types.threshold_type.deserialize_aws_json_1_1(
                data["ActionThresholdType"]
            )
        )
    else:
        import typing

        out["action_threshold_type"] = typing.cast(
            "capo_budgets.types.threshold_type.ThresholdType", ""
        )
    return out
