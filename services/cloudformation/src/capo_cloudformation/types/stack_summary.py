"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.creation_time
    import capo_cloudformation.types.deletion_time
    import capo_cloudformation.types.last_operations
    import capo_cloudformation.types.last_updated_time
    import capo_cloudformation.types.stack_drift_information_summary
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.stack_name
    import capo_cloudformation.types.stack_status
    import capo_cloudformation.types.stack_status_reason
    import capo_cloudformation.types.template_description


class StackSummary(TypedDict, closed=True):
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>Unique stack identifier.</p>"""
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>The name associated with the stack.</p>"""
    template_description: NotRequired[
        "capo_cloudformation.types.template_description.TemplateDescription"
    ]
    """<p>The template description of the template used to create the stack.</p>"""
    creation_time: NotRequired["capo_cloudformation.types.creation_time.CreationTime"]
    """<p>The time the stack was created.</p>"""
    last_updated_time: NotRequired[
        "capo_cloudformation.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>The time the stack was last updated. This field will only be returned if the stack has been updated at least once.</p>"""
    deletion_time: NotRequired["capo_cloudformation.types.deletion_time.DeletionTime"]
    """<p>The time the stack was deleted.</p>"""
    stack_status: NotRequired["capo_cloudformation.types.stack_status.StackStatus"]
    """<p>The current status of the stack.</p>"""
    stack_status_reason: NotRequired[
        "capo_cloudformation.types.stack_status_reason.StackStatusReason"
    ]
    """<p>Success/Failure message associated with the stack status.</p>"""
    parent_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>For nested stacks, the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Nested stacks</a> in the <i>CloudFormation User Guide</i>.</p>"""
    root_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>For nested stacks, the stack ID of the top-level stack to which the nested stack ultimately belongs.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Nested stacks</a> in the <i>CloudFormation User Guide</i>.</p>"""
    drift_information: NotRequired[
        "capo_cloudformation.types.stack_drift_information_summary.StackDriftInformationSummary"
    ]
    """<p>Summarizes information about whether a stack's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detect unmanaged configuration changes to stacks and resources with drift detection</a>.</p>"""
    last_operations: NotRequired[
        "capo_cloudformation.types.last_operations.LastOperations"
    ]
    """<p>Information about the most recent operations performed on this stack.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "template_description" in value:
        pairs.append(
            (f"{key_prefix}TemplateDescription", str(value["template_description"]))
        )
    if "creation_time" in value:
        import capo_cloudformation.types.creation_time

        capo_cloudformation.types.creation_time.serialize_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "last_updated_time" in value:
        import capo_cloudformation.types.last_updated_time

        capo_cloudformation.types.last_updated_time.serialize_query(
            value["last_updated_time"], pairs, f"{key_prefix}LastUpdatedTime"
        )
    if "deletion_time" in value:
        import capo_cloudformation.types.deletion_time

        capo_cloudformation.types.deletion_time.serialize_query(
            value["deletion_time"], pairs, f"{key_prefix}DeletionTime"
        )
    if "stack_status" in value:
        import capo_cloudformation.types.stack_status

        capo_cloudformation.types.stack_status.serialize_query(
            value["stack_status"], pairs, f"{key_prefix}StackStatus"
        )
    if "stack_status_reason" in value:
        pairs.append(
            (f"{key_prefix}StackStatusReason", str(value["stack_status_reason"]))
        )
    if "parent_id" in value:
        pairs.append((f"{key_prefix}ParentId", str(value["parent_id"])))
    if "root_id" in value:
        pairs.append((f"{key_prefix}RootId", str(value["root_id"])))
    if "drift_information" in value:
        import capo_cloudformation.types.stack_drift_information_summary

        capo_cloudformation.types.stack_drift_information_summary.serialize_query(
            value["drift_information"], pairs, f"{key_prefix}DriftInformation"
        )
    if "last_operations" in value:
        import capo_cloudformation.types.last_operations

        capo_cloudformation.types.last_operations.serialize_query(
            value["last_operations"], pairs, f"{key_prefix}LastOperations"
        )


def deserialize_query(el: Element) -> StackSummary:
    out: StackSummary = {}  # type: ignore[typeddict-item]
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_template_description = el.find("TemplateDescription")
    if child_template_description is not None:
        out["template_description"] = str(child_template_description.text or "")
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_cloudformation.types.creation_time

        out["creation_time"] = (
            capo_cloudformation.types.creation_time.deserialize_query(
                child_creation_time
            )
        )
    child_last_updated_time = el.find("LastUpdatedTime")
    if child_last_updated_time is not None:
        import capo_cloudformation.types.last_updated_time

        out["last_updated_time"] = (
            capo_cloudformation.types.last_updated_time.deserialize_query(
                child_last_updated_time
            )
        )
    child_deletion_time = el.find("DeletionTime")
    if child_deletion_time is not None:
        import capo_cloudformation.types.deletion_time

        out["deletion_time"] = (
            capo_cloudformation.types.deletion_time.deserialize_query(
                child_deletion_time
            )
        )
    child_stack_status = el.find("StackStatus")
    if child_stack_status is not None:
        import capo_cloudformation.types.stack_status

        out["stack_status"] = capo_cloudformation.types.stack_status.deserialize_query(
            child_stack_status
        )
    child_stack_status_reason = el.find("StackStatusReason")
    if child_stack_status_reason is not None:
        out["stack_status_reason"] = str(child_stack_status_reason.text or "")
    child_parent_id = el.find("ParentId")
    if child_parent_id is not None:
        out["parent_id"] = str(child_parent_id.text or "")
    child_root_id = el.find("RootId")
    if child_root_id is not None:
        out["root_id"] = str(child_root_id.text or "")
    child_drift_information = el.find("DriftInformation")
    if child_drift_information is not None:
        import capo_cloudformation.types.stack_drift_information_summary

        out["drift_information"] = (
            capo_cloudformation.types.stack_drift_information_summary.deserialize_query(
                child_drift_information
            )
        )
    child_last_operations = el.find("LastOperations")
    if child_last_operations is not None:
        import capo_cloudformation.types.last_operations

        out["last_operations"] = (
            capo_cloudformation.types.last_operations.deserialize_query(
                child_last_operations
            )
        )
    return out
