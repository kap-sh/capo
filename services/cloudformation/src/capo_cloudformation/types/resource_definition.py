"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.resource_identifier_properties
    import capo_cloudformation.types.resource_type


class ResourceDefinition(TypedDict, closed=True):
    resource_type: NotRequired["capo_cloudformation.types.resource_type.ResourceType"]
    """<p>The type of the resource, such as <code>AWS::DynamoDB::Table</code>. For the list of supported resources, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support for imports and drift detection</a> in the <i>CloudFormation User Guide</i> </p>"""
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical resource id for this resource in the generated template.</p>"""
    resource_identifier: NotRequired[
        "capo_cloudformation.types.resource_identifier_properties.ResourceIdentifierProperties"
    ]
    """<p>A list of up to 256 key-value pairs that identifies the scanned resource. The key is the name of one of the primary identifiers for the resource. (Primary identifiers are specified in the <code>primaryIdentifier</code> list in the resource schema.) The value is the value of that primary identifier. For example, for a <code>AWS::DynamoDB::Table</code> resource, the primary identifiers is <code>TableName</code> so the key-value pair could be <code>"TableName": "MyDDBTable"</code>. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-primaryidentifier">primaryIdentifier</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceDefinition, pairs: list[tuple[str, str]], prefix: str
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


def deserialize_query(el: Element) -> ResourceDefinition:
    out: ResourceDefinition = {}  # type: ignore[typeddict-item]
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
    return out
