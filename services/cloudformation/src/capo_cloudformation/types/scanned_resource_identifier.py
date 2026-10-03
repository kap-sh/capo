"""Generated from Smithy shape ``com.amazonaws.cloudformation#ScannedResourceIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.jazz_resource_identifier_properties
    import capo_cloudformation.types.resource_type


class ScannedResourceIdentifier(TypedDict, closed=True):
    resource_type: NotRequired["capo_cloudformation.types.resource_type.ResourceType"]
    """<p>The type of the resource, such as <code>AWS::DynamoDB::Table</code>. For the list of supported resources, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support for imports and drift detection</a> In the <i>CloudFormation User Guide</i>.</p>"""
    resource_identifier: NotRequired[
        "capo_cloudformation.types.jazz_resource_identifier_properties.JazzResourceIdentifierProperties"
    ]
    """<p>A list of up to 256 key-value pairs that identifies the scanned resource. The key is the name of one of the primary identifiers for the resource. (Primary identifiers are specified in the <code>primaryIdentifier</code> list in the resource schema.) The value is the value of that primary identifier. For example, for a <code>AWS::DynamoDB::Table</code> resource, the primary identifiers is <code>TableName</code> so the key-value pair could be <code>"TableName": "MyDDBTable"</code>. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-primaryidentifier">primaryIdentifier</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScannedResourceIdentifier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))
    if "resource_identifier" in value:
        import capo_cloudformation.types.jazz_resource_identifier_properties

        capo_cloudformation.types.jazz_resource_identifier_properties.serialize_query(
            value["resource_identifier"], pairs, f"{key_prefix}ResourceIdentifier"
        )


def deserialize_query(el: Element) -> ScannedResourceIdentifier:
    out: ScannedResourceIdentifier = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_resource_identifier = el.find("ResourceIdentifier")
    if child_resource_identifier is not None:
        import capo_cloudformation.types.jazz_resource_identifier_properties

        out["resource_identifier"] = (
            capo_cloudformation.types.jazz_resource_identifier_properties.deserialize_query(
                child_resource_identifier
            )
        )
    return out
