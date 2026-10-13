"""Generated from Smithy shape ``com.amazonaws.drs#CancelRecoveryPlanExecutionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution


class CancelRecoveryPlanExecutionResponse(TypedDict, closed=True):
    recovery_plan_execution: (
        "capo_drs.types.recovery_plan_execution.RecoveryPlanExecution"
    )
    """<p>The cancelled Recovery Plan execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelRecoveryPlanExecutionResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_execution

    out["recoveryPlanExecution"] = (
        capo_drs.types.recovery_plan_execution.serialize_json(
            value["recovery_plan_execution"]
        )
    )
    return out


def deserialize_json(data: dict) -> CancelRecoveryPlanExecutionResponse:
    out: CancelRecoveryPlanExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecution") is not None:
        import capo_drs.types.recovery_plan_execution

        out["recovery_plan_execution"] = (
            capo_drs.types.recovery_plan_execution.deserialize_json(
                data["recoveryPlanExecution"]
            )
        )
    else:
        raise DeserializationError(
            "CancelRecoveryPlanExecutionResponse.recovery_plan_execution required"
        )
    return out


def redact_sensitive(value: CancelRecoveryPlanExecutionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recovery_plan_execution" in value:
        import capo_drs.types.recovery_plan_execution

        out["recovery_plan_execution"] = (
            capo_drs.types.recovery_plan_execution.redact_sensitive(
                value["recovery_plan_execution"]
            )
        )
    return out
