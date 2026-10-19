"""Generated from Smithy shape ``com.amazonaws.drs#TerminateRecoveryInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_instances_for_termination_request


class TerminateRecoveryInstancesRequest(TypedDict, closed=True):
    recovery_instance_i_ds: "capo_drs.types.recovery_instances_for_termination_request.RecoveryInstancesForTerminationRequest"
    """<p>The IDs of the Recovery Instances that should be terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateRecoveryInstancesRequest) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_instances_for_termination_request

    out["recoveryInstanceIDs"] = (
        capo_drs.types.recovery_instances_for_termination_request.serialize_json(
            value["recovery_instance_i_ds"]
        )
    )
    return out


def deserialize_json(data: dict) -> TerminateRecoveryInstancesRequest:
    out: TerminateRecoveryInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryInstanceIDs") is not None:
        import capo_drs.types.recovery_instances_for_termination_request

        out["recovery_instance_i_ds"] = (
            capo_drs.types.recovery_instances_for_termination_request.deserialize_json(
                data["recoveryInstanceIDs"]
            )
        )
    else:
        out["recovery_instance_i_ds"] = []
    return out
