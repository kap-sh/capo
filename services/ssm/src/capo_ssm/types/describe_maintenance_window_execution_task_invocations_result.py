"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowExecutionTaskInvocationsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_task_invocation_identity_list
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowExecutionTaskInvocationsResult(TypedDict, closed=True):
    window_execution_task_invocation_identities: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_invocation_identity_list.MaintenanceWindowExecutionTaskInvocationIdentityList"
    ]
    """<p>Information about the task invocation results per invocation.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeMaintenanceWindowExecutionTaskInvocationsResult,
) -> dict:
    out: dict = {}
    if "window_execution_task_invocation_identities" in value:
        import capo_ssm.types.maintenance_window_execution_task_invocation_identity_list

        out["WindowExecutionTaskInvocationIdentities"] = (
            capo_ssm.types.maintenance_window_execution_task_invocation_identity_list.serialize_aws_json_1_1(
                value["window_execution_task_invocation_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeMaintenanceWindowExecutionTaskInvocationsResult:
    out: DescribeMaintenanceWindowExecutionTaskInvocationsResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionTaskInvocationIdentities") is not None:
        import capo_ssm.types.maintenance_window_execution_task_invocation_identity_list

        out["window_execution_task_invocation_identities"] = (
            capo_ssm.types.maintenance_window_execution_task_invocation_identity_list.deserialize_aws_json_1_1(
                data["WindowExecutionTaskInvocationIdentities"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: DescribeMaintenanceWindowExecutionTaskInvocationsResult,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "window_execution_task_invocation_identities" in value:
        import capo_ssm.types.maintenance_window_execution_task_invocation_identity_list

        out["window_execution_task_invocation_identities"] = (
            capo_ssm.types.maintenance_window_execution_task_invocation_identity_list.redact_sensitive(
                value["window_execution_task_invocation_identities"]
            )
        )
    return out
