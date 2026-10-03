"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.module_info
    import capo_cloudformation.types.physical_resource_id
    import capo_cloudformation.types.resource_status
    import capo_cloudformation.types.resource_status_reason
    import capo_cloudformation.types.resource_type
    import capo_cloudformation.types.stack_resource_drift_information_summary
    import capo_cloudformation.types.timestamp


class StackResourceSummary(TypedDict, closed=True):
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical name of the resource specified in the template.</p>"""
    physical_resource_id: NotRequired[
        "capo_cloudformation.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The name or unique identifier that corresponds to a physical instance ID of the resource.</p>"""
    resource_type: NotRequired["capo_cloudformation.types.resource_type.ResourceType"]
    """<p>Type of resource. (For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the <i>CloudFormation User Guide</i>.)</p>"""
    last_updated_timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>Time the status was updated.</p>"""
    resource_status: NotRequired[
        "capo_cloudformation.types.resource_status.ResourceStatus"
    ]
    """<p>Current status of the resource.</p>"""
    resource_status_reason: NotRequired[
        "capo_cloudformation.types.resource_status_reason.ResourceStatusReason"
    ]
    """<p>Success/failure message associated with the resource.</p>"""
    drift_information: NotRequired[
        "capo_cloudformation.types.stack_resource_drift_information_summary.StackResourceDriftInformationSummary"
    ]
    """<p>Information about whether the resource's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detect unmanaged configuration changes to stacks and resources with drift detection</a>.</p>"""
    module_info: NotRequired["capo_cloudformation.types.module_info.ModuleInfo"]
    """<p>Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackResourceSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "logical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}LogicalResourceId", str(value["logical_resource_id"]))
        )
    if "physical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}PhysicalResourceId", str(value["physical_resource_id"]))
        )
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))
    if "last_updated_timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["last_updated_timestamp"], pairs, f"{key_prefix}LastUpdatedTimestamp"
        )
    if "resource_status" in value:
        import capo_cloudformation.types.resource_status

        capo_cloudformation.types.resource_status.serialize_query(
            value["resource_status"], pairs, f"{key_prefix}ResourceStatus"
        )
    if "resource_status_reason" in value:
        pairs.append(
            (f"{key_prefix}ResourceStatusReason", str(value["resource_status_reason"]))
        )
    if "drift_information" in value:
        import capo_cloudformation.types.stack_resource_drift_information_summary

        capo_cloudformation.types.stack_resource_drift_information_summary.serialize_query(
            value["drift_information"], pairs, f"{key_prefix}DriftInformation"
        )
    if "module_info" in value:
        import capo_cloudformation.types.module_info

        capo_cloudformation.types.module_info.serialize_query(
            value["module_info"], pairs, f"{key_prefix}ModuleInfo"
        )


def deserialize_query(el: Element) -> StackResourceSummary:
    out: StackResourceSummary = {}  # type: ignore[typeddict-item]
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_physical_resource_id = el.find("PhysicalResourceId")
    if child_physical_resource_id is not None:
        out["physical_resource_id"] = str(child_physical_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_last_updated_timestamp = el.find("LastUpdatedTimestamp")
    if child_last_updated_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["last_updated_timestamp"] = (
            capo_cloudformation.types.timestamp.deserialize_query(
                child_last_updated_timestamp
            )
        )
    child_resource_status = el.find("ResourceStatus")
    if child_resource_status is not None:
        import capo_cloudformation.types.resource_status

        out["resource_status"] = (
            capo_cloudformation.types.resource_status.deserialize_query(
                child_resource_status
            )
        )
    child_resource_status_reason = el.find("ResourceStatusReason")
    if child_resource_status_reason is not None:
        out["resource_status_reason"] = str(child_resource_status_reason.text or "")
    child_drift_information = el.find("DriftInformation")
    if child_drift_information is not None:
        import capo_cloudformation.types.stack_resource_drift_information_summary

        out["drift_information"] = (
            capo_cloudformation.types.stack_resource_drift_information_summary.deserialize_query(
                child_drift_information
            )
        )
    child_module_info = el.find("ModuleInfo")
    if child_module_info is not None:
        import capo_cloudformation.types.module_info

        out["module_info"] = capo_cloudformation.types.module_info.deserialize_query(
            child_module_info
        )
    return out
