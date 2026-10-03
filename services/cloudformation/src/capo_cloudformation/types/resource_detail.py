"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.generated_template_resource_status
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.resource_identifier_properties
    import capo_cloudformation.types.resource_status_reason
    import capo_cloudformation.types.resource_type
    import capo_cloudformation.types.warning_details


class ResourceDetail(TypedDict, closed=True):
    resource_type: NotRequired["capo_cloudformation.types.resource_type.ResourceType"]
    """<p>The type of the resource, such as <code>AWS::DynamoDB::Table</code>. For the list of supported resources, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support for imports and drift detection</a> In the <i>CloudFormation User Guide</i> </p>"""
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical id for this resource in the final generated template.</p>"""
    resource_identifier: NotRequired[
        "capo_cloudformation.types.resource_identifier_properties.ResourceIdentifierProperties"
    ]
    """<p>A list of up to 256 key-value pairs that identifies the resource in the generated template. The key is the name of one of the primary identifiers for the resource. (Primary identifiers are specified in the <code>primaryIdentifier</code> list in the resource schema.) The value is the value of that primary identifier. For example, for a <code>AWS::DynamoDB::Table</code> resource, the primary identifiers is <code>TableName</code> so the key-value pair could be <code>"TableName": "MyDDBTable"</code>. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-primaryidentifier">primaryIdentifier</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p>"""
    resource_status: NotRequired[
        "capo_cloudformation.types.generated_template_resource_status.GeneratedTemplateResourceStatus"
    ]
    """<p>Status of the processing of a resource in a generated template.</p> <dl> <dt> InProgress </dt> <dd> <p>The resource processing is still in progress.</p> </dd> <dt> Complete </dt> <dd> <p>The resource processing is complete.</p> </dd> <dt> Pending </dt> <dd> <p>The resource processing is pending.</p> </dd> <dt> Failed </dt> <dd> <p>The resource processing has failed.</p> </dd> </dl>"""
    resource_status_reason: NotRequired[
        "capo_cloudformation.types.resource_status_reason.ResourceStatusReason"
    ]
    """<p>The reason for the resource detail, providing more information if a failure happened.</p>"""
    warnings: NotRequired["capo_cloudformation.types.warning_details.WarningDetails"]
    """<p>The warnings generated for this resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))
    if "logical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}LogicalResourceId", str(value["logical_resource_id"]))
        )
    if "resource_identifier" in value:
        import capo_cloudformation.types.resource_identifier_properties

        capo_cloudformation.types.resource_identifier_properties.serialize_query(
            value["resource_identifier"], pairs, f"{key_prefix}ResourceIdentifier"
        )
    if "resource_status" in value:
        import capo_cloudformation.types.generated_template_resource_status

        capo_cloudformation.types.generated_template_resource_status.serialize_query(
            value["resource_status"], pairs, f"{key_prefix}ResourceStatus"
        )
    if "resource_status_reason" in value:
        pairs.append(
            (f"{key_prefix}ResourceStatusReason", str(value["resource_status_reason"]))
        )
    if "warnings" in value:
        import capo_cloudformation.types.warning_details

        capo_cloudformation.types.warning_details.serialize_query(
            value["warnings"], pairs, f"{key_prefix}Warnings"
        )


def deserialize_query(el: Element) -> ResourceDetail:
    out: ResourceDetail = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_resource_identifier = el.find("ResourceIdentifier")
    if child_resource_identifier is not None:
        import capo_cloudformation.types.resource_identifier_properties

        out["resource_identifier"] = (
            capo_cloudformation.types.resource_identifier_properties.deserialize_query(
                child_resource_identifier
            )
        )
    child_resource_status = el.find("ResourceStatus")
    if child_resource_status is not None:
        import capo_cloudformation.types.generated_template_resource_status

        out["resource_status"] = (
            capo_cloudformation.types.generated_template_resource_status.deserialize_query(
                child_resource_status
            )
        )
    child_resource_status_reason = el.find("ResourceStatusReason")
    if child_resource_status_reason is not None:
        out["resource_status_reason"] = str(child_resource_status_reason.text or "")
    child_warnings = el.find("Warnings")
    if child_warnings is not None:
        import capo_cloudformation.types.warning_details

        out["warnings"] = capo_cloudformation.types.warning_details.deserialize_query(
            child_warnings
        )
    return out
