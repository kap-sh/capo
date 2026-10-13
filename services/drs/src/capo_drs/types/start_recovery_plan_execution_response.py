"""Generated from Smithy shape ``com.amazonaws.drs#StartRecoveryPlanExecutionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution


class StartRecoveryPlanExecutionResponse(TypedDict, closed=True):
    recovery_plan_execution: (
        "capo_drs.types.recovery_plan_execution.RecoveryPlanExecution"
    )
    """<p>The started Recovery Plan execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecoveryPlanExecutionResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_execution

    out["recoveryPlanExecution"] = (
        capo_drs.types.recovery_plan_execution.serialize_json(
            value["recovery_plan_execution"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartRecoveryPlanExecutionResponse:
    out: StartRecoveryPlanExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecution") is not None:
        import capo_drs.types.recovery_plan_execution

        out["recovery_plan_execution"] = (
            capo_drs.types.recovery_plan_execution.deserialize_json(
                data["recoveryPlanExecution"]
            )
        )
    else:
        raise DeserializationError(
            "StartRecoveryPlanExecutionResponse.recovery_plan_execution required"
        )
    return out


def redact_sensitive(value: StartRecoveryPlanExecutionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recovery_plan_execution" in value:
        import capo_drs.types.recovery_plan_execution

        out["recovery_plan_execution"] = (
            capo_drs.types.recovery_plan_execution.redact_sensitive(
                value["recovery_plan_execution"]
            )
        )
    return out
