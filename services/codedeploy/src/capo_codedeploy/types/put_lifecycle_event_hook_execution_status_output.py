"""Generated from Smithy shape ``com.amazonaws.codedeploy#PutLifecycleEventHookExecutionStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.lifecycle_event_hook_execution_id


class PutLifecycleEventHookExecutionStatusOutput(TypedDict, closed=True):
    lifecycle_event_hook_execution_id: NotRequired[
        "capo_codedeploy.types.lifecycle_event_hook_execution_id.LifecycleEventHookExecutionId"
    ]
    """<p>The execution ID of the lifecycle event hook. A hook is specified in the <code>hooks</code> section of the deployment's AppSpec file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLifecycleEventHookExecutionStatusOutput) -> dict:
    out: dict = {}
    if "lifecycle_event_hook_execution_id" in value:
        out["lifecycleEventHookExecutionId"] = value[
            "lifecycle_event_hook_execution_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLifecycleEventHookExecutionStatusOutput:
    out: PutLifecycleEventHookExecutionStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("lifecycleEventHookExecutionId") is not None:
        out["lifecycle_event_hook_execution_id"] = data["lifecycleEventHookExecutionId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutLifecycleEventHookExecutionStatusOutput) -> dict:
    out: dict = {}
    if "lifecycle_event_hook_execution_id" in value:
        out["lifecycleEventHookExecutionId"] = value[
            "lifecycle_event_hook_execution_id"
        ]
    return out


def deserialize_cbor(data: dict) -> PutLifecycleEventHookExecutionStatusOutput:
    out: PutLifecycleEventHookExecutionStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("lifecycleEventHookExecutionId") is not None:
        out["lifecycle_event_hook_execution_id"] = data["lifecycleEventHookExecutionId"]
    return out
