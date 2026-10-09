"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceDriftInformationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_resource_drift_status
    import capo_cloudformation.types.timestamp


class StackResourceDriftInformationSummary(TypedDict, closed=True):
    stack_resource_drift_status: NotRequired[
        "capo_cloudformation.types.stack_resource_drift_status.StackResourceDriftStatus"
    ]
    """<p>Status of the resource's actual configuration compared to its expected configuration.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected configuration in that it has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: The resource differs from its expected configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the resource differs from its expected configuration.</p> <p>Any resources that don't currently support drift detection have a status of <code>NOT_CHECKED</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support for imports and drift detection</a>. If you performed a <a>ContinueUpdateRollback</a> operation on a stack, resources skipped using <code>ResourcesToSkip</code> or <code>ForceRollback</code> also have a status of <code>NOT_CHECKED</code>. To detect whether a skipped resource actually differs from the template, run <a>DetectStackResourceDrift</a>. For more information about skipping resources during rollback operations, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html">Continue rolling back an update</a> in the <i>CloudFormation User Guide</i>.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected configuration.</p> </li> </ul>"""
    last_check_timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>When CloudFormation last checked if the resource had drifted from its expected configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackResourceDriftInformationSummary,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_resource_drift_status" in value:
        import capo_cloudformation.types.stack_resource_drift_status

        capo_cloudformation.types.stack_resource_drift_status.serialize_query(
            value["stack_resource_drift_status"],
            pairs,
            f"{key_prefix}StackResourceDriftStatus",
        )
    if "last_check_timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["last_check_timestamp"], pairs, f"{key_prefix}LastCheckTimestamp"
        )


def deserialize_query(el: Element) -> StackResourceDriftInformationSummary:
    out: StackResourceDriftInformationSummary = {}  # type: ignore[typeddict-item]
    child_stack_resource_drift_status = el.find("StackResourceDriftStatus")
    if child_stack_resource_drift_status is not None:
        import capo_cloudformation.types.stack_resource_drift_status

        out["stack_resource_drift_status"] = (
            capo_cloudformation.types.stack_resource_drift_status.deserialize_query(
                child_stack_resource_drift_status
            )
        )
    child_last_check_timestamp = el.find("LastCheckTimestamp")
    if child_last_check_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["last_check_timestamp"] = (
            capo_cloudformation.types.timestamp.deserialize_query(
                child_last_check_timestamp
            )
        )
    return out
