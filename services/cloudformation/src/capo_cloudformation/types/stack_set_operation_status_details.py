"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.failed_stack_instances_count
    import capo_cloudformation.types.stack_set_operation_total_stack_instances_count
    import capo_cloudformation.types.stages
    import capo_cloudformation.types.total_accounts_count


class StackSetOperationStatusDetails(TypedDict, closed=True):
    stages: NotRequired["capo_cloudformation.types.stages.Stages"]
    """<p>The detailed progress information for the individual stages of the StackSet operation: the role provisioning stage and the stack instances deployment stage.</p>"""
    total_accounts_count: NotRequired[
        "capo_cloudformation.types.total_accounts_count.TotalAccountsCount"
    ]
    """<p>The total number of accounts targeted by this StackSet operation. Self-managed operations and service-managed operations that do not provision roles also report this value when it is known. CloudFormation populates this value after it resolves the target accounts. Until then, this field is not present.</p>"""
    total_stack_instances_count: NotRequired[
        "capo_cloudformation.types.stack_set_operation_total_stack_instances_count.StackSetOperationTotalStackInstancesCount"
    ]
    """<p>The total number of stack instances targeted by this StackSet operation. CloudFormation populates this value after it resolves the target stack instances. Until then, this field is not present.</p>"""
    failed_stack_instances_count: NotRequired[
        "capo_cloudformation.types.failed_stack_instances_count.FailedStackInstancesCount"
    ]
    """<p>The number of stack instances for which the StackSet operation failed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetOperationStatusDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stages" in value:
        import capo_cloudformation.types.stages

        capo_cloudformation.types.stages.serialize_query(
            value["stages"], pairs, f"{key_prefix}Stages"
        )
    if "total_accounts_count" in value:
        pairs.append(
            (f"{key_prefix}TotalAccountsCount", str(value["total_accounts_count"]))
        )
    if "total_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}TotalStackInstancesCount",
                str(value["total_stack_instances_count"]),
            )
        )
    if "failed_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}FailedStackInstancesCount",
                str(value["failed_stack_instances_count"]),
            )
        )


def deserialize_query(el: Element) -> StackSetOperationStatusDetails:
    out: StackSetOperationStatusDetails = {}  # type: ignore[typeddict-item]
    child_stages = el.find("Stages")
    if child_stages is not None:
        import capo_cloudformation.types.stages

        out["stages"] = capo_cloudformation.types.stages.deserialize_query(child_stages)
    child_total_accounts_count = el.find("TotalAccountsCount")
    if child_total_accounts_count is not None:
        out["total_accounts_count"] = int(child_total_accounts_count.text or "")
    child_total_stack_instances_count = el.find("TotalStackInstancesCount")
    if child_total_stack_instances_count is not None:
        out["total_stack_instances_count"] = int(
            child_total_stack_instances_count.text or ""
        )
    child_failed_stack_instances_count = el.find("FailedStackInstancesCount")
    if child_failed_stack_instances_count is not None:
        out["failed_stack_instances_count"] = int(
            child_failed_stack_instances_count.text or ""
        )
    return out
