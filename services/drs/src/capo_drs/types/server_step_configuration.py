"""Generated from Smithy shape ``com.amazonaws.drs#ServerStepConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_servers


class ServerStepConfiguration(TypedDict, closed=True):
    servers: "capo_drs.types.recovery_plan_servers.RecoveryPlanServers"
    """<p>The list of servers to recover in this step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerStepConfiguration) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_servers

    out["servers"] = capo_drs.types.recovery_plan_servers.serialize_json(
        value["servers"]
    )
    return out


def deserialize_json(data: dict) -> ServerStepConfiguration:
    out: ServerStepConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("servers") is not None:
        import capo_drs.types.recovery_plan_servers

        out["servers"] = capo_drs.types.recovery_plan_servers.deserialize_json(
            data["servers"]
        )
    else:
        out["servers"] = []
    return out
