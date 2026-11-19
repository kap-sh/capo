"""Generated from Smithy shape ``com.amazonaws.codedeploy#PutLifecycleEventHookExecutionStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.lifecycle_event_hook_execution_id
    import capo_codedeploy.types.lifecycle_event_status


class PutLifecycleEventHookExecutionStatusInput(TypedDict, closed=True):
    deployment_id: NotRequired["capo_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. Pass this ID to a Lambda function that validates a deployment lifecycle event. </p>"""
    lifecycle_event_hook_execution_id: NotRequired[
        "capo_codedeploy.types.lifecycle_event_hook_execution_id.LifecycleEventHookExecutionId"
    ]
    """<p> The execution ID of a deployment's lifecycle hook. A deployment lifecycle hook is specified in the <code>hooks</code> section of the AppSpec file. </p>"""
    status: NotRequired[
        "capo_codedeploy.types.lifecycle_event_status.LifecycleEventStatus"
    ]
    """<p>The result of a Lambda function that validates a deployment lifecycle event. The values listed in <b>Valid Values</b> are valid for lifecycle statuses in general; however, only <code>Succeeded</code> and <code>Failed</code> can be passed successfully in your API call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLifecycleEventHookExecutionStatusInput) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "lifecycle_event_hook_execution_id" in value:
        out["lifecycleEventHookExecutionId"] = value[
            "lifecycle_event_hook_execution_id"
        ]
    if "status" in value:
        import capo_codedeploy.types.lifecycle_event_status

        out["status"] = (
            capo_codedeploy.types.lifecycle_event_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLifecycleEventHookExecutionStatusInput:
    out: PutLifecycleEventHookExecutionStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("lifecycleEventHookExecutionId") is not None:
        out["lifecycle_event_hook_execution_id"] = data["lifecycleEventHookExecutionId"]
    if data.get("status") is not None:
        import capo_codedeploy.types.lifecycle_event_status

        out["status"] = (
            capo_codedeploy.types.lifecycle_event_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutLifecycleEventHookExecutionStatusInput) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "lifecycle_event_hook_execution_id" in value:
        out["lifecycleEventHookExecutionId"] = value[
            "lifecycle_event_hook_execution_id"
        ]
    if "status" in value:
        import capo_codedeploy.types.lifecycle_event_status

        out["status"] = capo_codedeploy.types.lifecycle_event_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> PutLifecycleEventHookExecutionStatusInput:
    out: PutLifecycleEventHookExecutionStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("lifecycleEventHookExecutionId") is not None:
        out["lifecycle_event_hook_execution_id"] = data["lifecycleEventHookExecutionId"]
    if data.get("status") is not None:
        import capo_codedeploy.types.lifecycle_event_status

        out["status"] = capo_codedeploy.types.lifecycle_event_status.deserialize_cbor(
            data["status"]
        )
    return out
