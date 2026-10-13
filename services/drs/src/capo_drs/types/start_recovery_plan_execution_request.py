"""Generated from Smithy shape ``com.amazonaws.drs#StartRecoveryPlanExecutionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.client_idempotency_token
    import capo_drs.types.recovery_plan_execution_mode
    import capo_drs.types.recovery_plan_execution_source_server_list
    import capo_drs.types.strict_drsarn
    import capo_drs.types.tags_map


class StartRecoveryPlanExecutionRequest(TypedDict, closed=True):
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan to execute.</p>"""
    mode: "capo_drs.types.recovery_plan_execution_mode.RecoveryPlanExecutionMode"
    """<p>The execution mode (<code>DRILL</code> or <code>RECOVERY</code>).</p>"""
    client_token: NotRequired[
        "capo_drs.types.client_idempotency_token.ClientIdempotencyToken"
    ]
    """<p>A unique string provided to ensure request idempotency.</p>"""
    source_servers: NotRequired[
        "capo_drs.types.recovery_plan_execution_source_server_list.RecoveryPlanExecutionSourceServerList"
    ]
    """<p>Optional list of source servers with specific recovery snapshots. If not provided, the latest snapshot is used for each server.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>The tags to apply to the Recovery Plan execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecoveryPlanExecutionRequest) -> dict:
    out: dict = {}
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    out["mode"] = value["mode"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "source_servers" in value:
        import capo_drs.types.recovery_plan_execution_source_server_list

        out["sourceServers"] = (
            capo_drs.types.recovery_plan_execution_source_server_list.serialize_json(
                value["source_servers"]
            )
        )
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartRecoveryPlanExecutionRequest:
    out: StartRecoveryPlanExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        raise DeserializationError(
            "StartRecoveryPlanExecutionRequest.recovery_plan_arn required"
        )
    if data.get("mode") is not None:
        out["mode"] = data["mode"]
    else:
        raise DeserializationError("StartRecoveryPlanExecutionRequest.mode required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("sourceServers") is not None:
        import capo_drs.types.recovery_plan_execution_source_server_list

        out["source_servers"] = (
            capo_drs.types.recovery_plan_execution_source_server_list.deserialize_json(
                data["sourceServers"]
            )
        )
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: StartRecoveryPlanExecutionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
