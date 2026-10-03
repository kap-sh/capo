"""Generated from Smithy shape ``com.amazonaws.cloudformation#ScanFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.resource_type_filters


class ScanFilter(TypedDict, closed=True):
    types: NotRequired[
        "capo_cloudformation.types.resource_type_filters.ResourceTypeFilters"
    ]
    """<p>An array of strings where each string represents an Amazon Web Services resource type you want to scan. Each string defines the resource type using the format <code>AWS::ServiceName::ResourceType</code>, for example, <code>AWS::DynamoDB::Table</code>. For the full list of supported resource types, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support</a> table in the <i>CloudFormation User Guide</i>.</p> <p>To scan all resource types within a service, you can use a wildcard, represented by an asterisk (<code>*</code>). You can place an asterisk at only the end of the string, for example, <code>AWS::S3::*</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScanFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "types" in value:
        import capo_cloudformation.types.resource_type_filters

        capo_cloudformation.types.resource_type_filters.serialize_query(
            value["types"], pairs, f"{key_prefix}Types"
        )


def deserialize_query(el: Element) -> ScanFilter:
    out: ScanFilter = {}  # type: ignore[typeddict-item]
    child_types = el.find("Types")
    if child_types is not None:
        import capo_cloudformation.types.resource_type_filters

        out["types"] = (
            capo_cloudformation.types.resource_type_filters.deserialize_query(
                child_types
            )
        )
    return out
