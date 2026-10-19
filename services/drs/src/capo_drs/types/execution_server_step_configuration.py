"""Generated from Smithy shape ``com.amazonaws.drs#ExecutionServerStepConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_execution_servers


class ExecutionServerStepConfiguration(TypedDict, closed=True):
    servers: (
        "capo_drs.types.recovery_plan_execution_servers.RecoveryPlanExecutionServers"
    )
    """<p>The list of servers in this execution step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionServerStepConfiguration) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_execution_servers

    out["servers"] = capo_drs.types.recovery_plan_execution_servers.serialize_json(
        value["servers"]
    )
    return out


def deserialize_json(data: dict) -> ExecutionServerStepConfiguration:
    out: ExecutionServerStepConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("servers") is not None:
        import capo_drs.types.recovery_plan_execution_servers

        out["servers"] = (
            capo_drs.types.recovery_plan_execution_servers.deserialize_json(
                data["servers"]
            )
        )
    else:
        out["servers"] = []
    return out
