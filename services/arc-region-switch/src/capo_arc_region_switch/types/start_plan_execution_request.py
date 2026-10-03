"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#StartPlanExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.execution_action
    import capo_arc_region_switch.types.execution_comment
    import capo_arc_region_switch.types.execution_mode
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.recovery_execution_id


class StartPlanExecutionRequest(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan to execute.</p>"""
    target_region: "str"
    """<p>The Amazon Web Services Region to target with this execution. This is the Region that traffic will be shifted to or from, depending on the action.</p>"""
    action: "capo_arc_region_switch.types.execution_action.ExecutionAction"
    """<p>The action to perform. Valid values are <code>activate</code> (to shift traffic to the target Region) or <code>deactivate</code> (to shift traffic away from the target Region).</p>"""
    mode: "capo_arc_region_switch.types.execution_mode.ExecutionMode"
    """<p>The plan execution mode. Valid values are <code>graceful</code>, for starting the execution in graceful mode, or <code>ungraceful</code>, for starting the execution in ungraceful mode.</p>"""
    comment: NotRequired[
        "capo_arc_region_switch.types.execution_comment.ExecutionComment"
    ]
    """<p>An optional comment explaining why the plan execution is being started.</p>"""
    latest_version: NotRequired["str"]
    """<p>A boolean value indicating whether to use the latest version of the plan. If set to false, you must specify a specific version.</p>"""
    recovery_execution_id: NotRequired[
        "capo_arc_region_switch.types.recovery_execution_id.RecoveryExecutionId"
    ]
    """<p>The execution identifier of the recovery execution that ran in the opposite region post-recovery is ran in. Required when starting a post-recovery execution.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request and returns the result of the original successful request. If you don't provide a client token, the service automatically generates one. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartPlanExecutionRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["targetRegion"] = value["target_region"]
    import capo_arc_region_switch.types.execution_action

    out["action"] = (
        capo_arc_region_switch.types.execution_action.serialize_aws_json_1_0(
            value["action"]
        )
    )
    import capo_arc_region_switch.types.execution_mode

    out["mode"] = capo_arc_region_switch.types.execution_mode.serialize_aws_json_1_0(
        value.get("mode", "graceful")
    )
    if "comment" in value:
        out["comment"] = value["comment"]
    if "latest_version" in value:
        out["latestVersion"] = value["latest_version"]
    if "recovery_execution_id" in value:
        out["recoveryExecutionId"] = value["recovery_execution_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartPlanExecutionRequest:
    out: StartPlanExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("planArn") is not None:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("StartPlanExecutionRequest.plan_arn required")
    if data.get("targetRegion") is not None:
        out["target_region"] = data["targetRegion"]
    else:
        raise DeserializationError("StartPlanExecutionRequest.target_region required")
    if data.get("action") is not None:
        import capo_arc_region_switch.types.execution_action

        out["action"] = (
            capo_arc_region_switch.types.execution_action.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    else:
        raise DeserializationError("StartPlanExecutionRequest.action required")
    if data.get("mode") is not None:
        import capo_arc_region_switch.types.execution_mode

        out["mode"] = (
            capo_arc_region_switch.types.execution_mode.deserialize_aws_json_1_0(
                data["mode"]
            )
        )
    else:
        out["mode"] = "graceful"
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("latestVersion") is not None:
        out["latest_version"] = data["latestVersion"]
    if data.get("recoveryExecutionId") is not None:
        out["recovery_execution_id"] = data["recoveryExecutionId"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
