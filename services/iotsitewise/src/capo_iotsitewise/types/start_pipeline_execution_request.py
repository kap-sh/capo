"""Generated from Smithy shape ``com.amazonaws.iotsitewise#StartPipelineExecutionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.execution_environment_variables
    import capo_iotsitewise.types.execution_priority
    import capo_iotsitewise.types.mount_overrides
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.workspace_name


class StartPipelineExecutionRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace containing the pipeline.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline to execute.</p>"""
    execution_environment_variable_overrides: NotRequired[
        "capo_iotsitewise.types.execution_environment_variables.ExecutionEnvironmentVariables"
    ]
    """<p>Runtime environment variable overrides for the execution. Includes global variables that apply to all compute nodes and computeNodes for per-node overrides. These take the highest priority in the environment variable hierarchy.</p>"""
    execution_mount_overrides: NotRequired[
        "capo_iotsitewise.types.mount_overrides.MountOverrides"
    ]
    """<p>Runtime mount overrides for the execution. Overrides are merged by mount name into each listed compute node's task-defined mounts: a matching name replaces the task-defined mount, a new name adds a mount, and task-defined mounts not referenced remain unchanged. Compute nodes not listed use their task-defined mounts as-is.</p>"""
    execution_priority: NotRequired[
        "capo_iotsitewise.types.execution_priority.ExecutionPriority"
    ]
    """<p>Scheduling priority for the execution. Lower values indicate higher priority. Defaults to 2 when not specified.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPipelineExecutionRequest) -> dict:
    out: dict = {}
    if "execution_environment_variable_overrides" in value:
        import capo_iotsitewise.types.execution_environment_variables

        out["executionEnvironmentVariableOverrides"] = (
            capo_iotsitewise.types.execution_environment_variables.serialize_json(
                value["execution_environment_variable_overrides"]
            )
        )
    if "execution_mount_overrides" in value:
        import capo_iotsitewise.types.mount_overrides

        out["executionMountOverrides"] = (
            capo_iotsitewise.types.mount_overrides.serialize_json(
                value["execution_mount_overrides"]
            )
        )
    if "execution_priority" in value:
        out["executionPriority"] = value["execution_priority"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartPipelineExecutionRequest:
    out: StartPipelineExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("executionEnvironmentVariableOverrides") is not None:
        import capo_iotsitewise.types.execution_environment_variables

        out["execution_environment_variable_overrides"] = (
            capo_iotsitewise.types.execution_environment_variables.deserialize_json(
                data["executionEnvironmentVariableOverrides"]
            )
        )
    if data.get("executionMountOverrides") is not None:
        import capo_iotsitewise.types.mount_overrides

        out["execution_mount_overrides"] = (
            capo_iotsitewise.types.mount_overrides.deserialize_json(
                data["executionMountOverrides"]
            )
        )
    if data.get("executionPriority") is not None:
        out["execution_priority"] = data["executionPriority"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: StartPipelineExecutionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "execution_environment_variable_overrides" in value:
        out["execution_environment_variable_overrides"] = (
            "*** Sensitive Data Redacted ***"
        )
    return out
