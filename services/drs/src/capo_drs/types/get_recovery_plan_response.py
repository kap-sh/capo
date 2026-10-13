"""Generated from Smithy shape ``com.amazonaws.drs#GetRecoveryPlanResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan


class GetRecoveryPlanResponse(TypedDict, closed=True):
    recovery_plan: "capo_drs.types.recovery_plan.RecoveryPlan"


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryPlanResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan

    out["recoveryPlan"] = capo_drs.types.recovery_plan.serialize_json(
        value["recovery_plan"]
    )
    return out


def deserialize_json(data: dict) -> GetRecoveryPlanResponse:
    out: GetRecoveryPlanResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlan") is not None:
        import capo_drs.types.recovery_plan

        out["recovery_plan"] = capo_drs.types.recovery_plan.deserialize_json(
            data["recoveryPlan"]
        )
    else:
        raise DeserializationError("GetRecoveryPlanResponse.recovery_plan required")
    return out


def redact_sensitive(value: GetRecoveryPlanResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recovery_plan" in value:
        import capo_drs.types.recovery_plan

        out["recovery_plan"] = capo_drs.types.recovery_plan.redact_sensitive(
            value["recovery_plan"]
        )
    return out
