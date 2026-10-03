"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceResourceDriftsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.physical_resource_id
    import capo_cloudformation.types.physical_resource_id_context
    import capo_cloudformation.types.property_differences
    import capo_cloudformation.types.resource_type
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.stack_resource_drift_status
    import capo_cloudformation.types.timestamp


class StackInstanceResourceDriftsSummary(TypedDict, closed=True):
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>The ID of the stack instance.</p>"""
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical name of the resource specified in the template.</p>"""
    physical_resource_id: NotRequired[
        "capo_cloudformation.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.</p>"""
    physical_resource_id_context: NotRequired[
        "capo_cloudformation.types.physical_resource_id_context.PhysicalResourceIdContext"
    ]
    """<p>Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses context key-value pairs in cases where a resource's logical and physical IDs aren't enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.</p>"""
    resource_type: NotRequired["capo_cloudformation.types.resource_type.ResourceType"]
    """<p>Type of resource. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the <i>CloudFormation User Guide</i>.</p>"""
    property_differences: NotRequired[
        "capo_cloudformation.types.property_differences.PropertyDifferences"
    ]
    """<p>Status of the actual configuration of the resource compared to its expected configuration. These will be present only for resources whose <code>StackInstanceResourceDriftStatus</code> is <code>MODIFIED</code>. </p>"""
    stack_resource_drift_status: NotRequired[
        "capo_cloudformation.types.stack_resource_drift_status.StackResourceDriftStatus"
    ]
    """<p>The drift status of the resource in a stack instance.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration in that the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected template values.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation doesn't currently return this value.</p> </li> </ul>"""
    timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>Time at which the stack instance drift detection operation was initiated.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackInstanceResourceDriftsSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
    if "logical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}LogicalResourceId", str(value["logical_resource_id"]))
        )
    if "physical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}PhysicalResourceId", str(value["physical_resource_id"]))
        )
    if "physical_resource_id_context" in value:
        import capo_cloudformation.types.physical_resource_id_context

        capo_cloudformation.types.physical_resource_id_context.serialize_query(
            value["physical_resource_id_context"],
            pairs,
            f"{key_prefix}PhysicalResourceIdContext",
        )
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))
    if "property_differences" in value:
        import capo_cloudformation.types.property_differences

        capo_cloudformation.types.property_differences.serialize_query(
            value["property_differences"], pairs, f"{key_prefix}PropertyDifferences"
        )
    if "stack_resource_drift_status" in value:
        import capo_cloudformation.types.stack_resource_drift_status

        capo_cloudformation.types.stack_resource_drift_status.serialize_query(
            value["stack_resource_drift_status"],
            pairs,
            f"{key_prefix}StackResourceDriftStatus",
        )
    if "timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )


def deserialize_query(el: Element) -> StackInstanceResourceDriftsSummary:
    out: StackInstanceResourceDriftsSummary = {}  # type: ignore[typeddict-item]
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_physical_resource_id = el.find("PhysicalResourceId")
    if child_physical_resource_id is not None:
        out["physical_resource_id"] = str(child_physical_resource_id.text or "")
    child_physical_resource_id_context = el.find("PhysicalResourceIdContext")
    if child_physical_resource_id_context is not None:
        import capo_cloudformation.types.physical_resource_id_context

        out["physical_resource_id_context"] = (
            capo_cloudformation.types.physical_resource_id_context.deserialize_query(
                child_physical_resource_id_context
            )
        )
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_property_differences = el.find("PropertyDifferences")
    if child_property_differences is not None:
        import capo_cloudformation.types.property_differences

        out["property_differences"] = (
            capo_cloudformation.types.property_differences.deserialize_query(
                child_property_differences
            )
        )
    child_stack_resource_drift_status = el.find("StackResourceDriftStatus")
    if child_stack_resource_drift_status is not None:
        import capo_cloudformation.types.stack_resource_drift_status

        out["stack_resource_drift_status"] = (
            capo_cloudformation.types.stack_resource_drift_status.deserialize_query(
                child_stack_resource_drift_status
            )
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["timestamp"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_timestamp
        )
    return out
