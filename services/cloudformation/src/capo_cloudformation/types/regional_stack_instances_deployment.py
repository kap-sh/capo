"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegionalStackInstancesDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.cancelled_stack_instances_count
    import capo_cloudformation.types.completed_stack_instances_count
    import capo_cloudformation.types.pending_stack_instances_count
    import capo_cloudformation.types.regional_total_stack_instances_count
    import capo_cloudformation.types.skipped_stack_instances_count
    import capo_cloudformation.types.stack_instances_deployment_failed_stack_instances_count
    import capo_cloudformation.types.stage_percentage_completed
    import capo_cloudformation.types.stage_status
    import capo_cloudformation.types.succeeded_stack_instances_count


class RegionalStackInstancesDeployment(TypedDict, closed=True):
    status: NotRequired["capo_cloudformation.types.stage_status.StageStatus"]
    """<p>The status of the stack instances deployment stage can be one of the following values:</p> <ul> <li> <p> <code>NOT_APPLICABLE</code>: The operation does not deploy stack instances, such as a drift detection operation.</p> </li> <li> <p> <code>NOT_STARTED</code>: Stack instances deployment has not started. The operation is still provisioning roles, has not begun, or failed before this stage was reached.</p> </li> <li> <p> <code>IN_PROGRESS</code>: At least one stack instance has started deploying.</p> </li> <li> <p> <code>SUCCEEDED</code>: Deployment finished and succeeded for all stack instances that were not skipped.</p> </li> <li> <p> <code>PARTIAL_SUCCESS</code>: Deployment finished with a mix of succeeded, failed, and canceled stack instances.</p> </li> <li> <p> <code>FAILED</code>: Deployment finished and every stack instance that was not skipped failed or was canceled.</p> </li> </ul>"""
    succeeded_stack_instances_count: NotRequired[
        "capo_cloudformation.types.succeeded_stack_instances_count.SucceededStackInstancesCount"
    ]
    """<p>The number of stack instances that deployed successfully in this Region.</p>"""
    failed_stack_instances_count: NotRequired[
        "capo_cloudformation.types.stack_instances_deployment_failed_stack_instances_count.StackInstancesDeploymentFailedStackInstancesCount"
    ]
    """<p>The number of stack instances that failed to deploy in this Region.</p>"""
    completed_stack_instances_count: NotRequired[
        "capo_cloudformation.types.completed_stack_instances_count.CompletedStackInstancesCount"
    ]
    """<p>The number of stack instances in this Region that have reached a final state. This count includes stack instances that succeeded, failed, were skipped, or were canceled.</p>"""
    pending_stack_instances_count: NotRequired[
        "capo_cloudformation.types.pending_stack_instances_count.PendingStackInstancesCount"
    ]
    """<p>The number of stack instances in this Region that have not reached a final state. This is the total number of stack instances in this Region minus the completed count.</p>"""
    cancelled_stack_instances_count: NotRequired[
        "capo_cloudformation.types.cancelled_stack_instances_count.CancelledStackInstancesCount"
    ]
    """<p>The number of stack instances in this Region that were canceled because the operation exceeded its failure tolerance or was stopped.</p>"""
    skipped_stack_instances_count: NotRequired[
        "capo_cloudformation.types.skipped_stack_instances_count.SkippedStackInstancesCount"
    ]
    """<p>The number of stack instances in this Region that were skipped because role provisioning failed for their target account.</p>"""
    total_stack_instances_count: NotRequired[
        "capo_cloudformation.types.regional_total_stack_instances_count.RegionalTotalStackInstancesCount"
    ]
    """<p>The total number of stack instances targeted by this operation in this Region.</p>"""
    percentage_completed: NotRequired[
        "capo_cloudformation.types.stage_percentage_completed.StagePercentageCompleted"
    ]
    """<p>The percentage of stack instances in this Region that have reached a final state.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegionalStackInstancesDeployment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_cloudformation.types.stage_status

        capo_cloudformation.types.stage_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "succeeded_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}SucceededStackInstancesCount",
                str(value["succeeded_stack_instances_count"]),
            )
        )
    if "failed_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}FailedStackInstancesCount",
                str(value["failed_stack_instances_count"]),
            )
        )
    if "completed_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}CompletedStackInstancesCount",
                str(value["completed_stack_instances_count"]),
            )
        )
    if "pending_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}PendingStackInstancesCount",
                str(value["pending_stack_instances_count"]),
            )
        )
    if "cancelled_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}CancelledStackInstancesCount",
                str(value["cancelled_stack_instances_count"]),
            )
        )
    if "skipped_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}SkippedStackInstancesCount",
                str(value["skipped_stack_instances_count"]),
            )
        )
    if "total_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}TotalStackInstancesCount",
                str(value["total_stack_instances_count"]),
            )
        )
    if "percentage_completed" in value:
        pairs.append(
            (
                f"{key_prefix}PercentageCompleted",
                (
                    "NaN"
                    if value["percentage_completed"] != value["percentage_completed"]
                    else "Infinity"
                    if value["percentage_completed"] == float("inf")
                    else "-Infinity"
                    if value["percentage_completed"] == float("-inf")
                    else str(value["percentage_completed"])
                ),
            )
        )


def deserialize_query(el: Element) -> RegionalStackInstancesDeployment:
    out: RegionalStackInstancesDeployment = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.stage_status

        out["status"] = capo_cloudformation.types.stage_status.deserialize_query(
            child_status
        )
    child_succeeded_stack_instances_count = el.find("SucceededStackInstancesCount")
    if child_succeeded_stack_instances_count is not None:
        out["succeeded_stack_instances_count"] = int(
            child_succeeded_stack_instances_count.text or ""
        )
    child_failed_stack_instances_count = el.find("FailedStackInstancesCount")
    if child_failed_stack_instances_count is not None:
        out["failed_stack_instances_count"] = int(
            child_failed_stack_instances_count.text or ""
        )
    child_completed_stack_instances_count = el.find("CompletedStackInstancesCount")
    if child_completed_stack_instances_count is not None:
        out["completed_stack_instances_count"] = int(
            child_completed_stack_instances_count.text or ""
        )
    child_pending_stack_instances_count = el.find("PendingStackInstancesCount")
    if child_pending_stack_instances_count is not None:
        out["pending_stack_instances_count"] = int(
            child_pending_stack_instances_count.text or ""
        )
    child_cancelled_stack_instances_count = el.find("CancelledStackInstancesCount")
    if child_cancelled_stack_instances_count is not None:
        out["cancelled_stack_instances_count"] = int(
            child_cancelled_stack_instances_count.text or ""
        )
    child_skipped_stack_instances_count = el.find("SkippedStackInstancesCount")
    if child_skipped_stack_instances_count is not None:
        out["skipped_stack_instances_count"] = int(
            child_skipped_stack_instances_count.text or ""
        )
    child_total_stack_instances_count = el.find("TotalStackInstancesCount")
    if child_total_stack_instances_count is not None:
        out["total_stack_instances_count"] = int(
            child_total_stack_instances_count.text or ""
        )
    child_percentage_completed = el.find("PercentageCompleted")
    if child_percentage_completed is not None:
        out["percentage_completed"] = float(child_percentage_completed.text or "")
    return out
