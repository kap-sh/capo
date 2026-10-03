"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetTemplateSummaryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.capabilities_reason
    import capo_cloudformation.types.description
    import capo_cloudformation.types.metadata
    import capo_cloudformation.types.parameter_declarations
    import capo_cloudformation.types.resource_identifier_summaries
    import capo_cloudformation.types.resource_types
    import capo_cloudformation.types.transforms_list
    import capo_cloudformation.types.version
    import capo_cloudformation.types.warnings


class GetTemplateSummaryOutput(TypedDict, closed=True):
    parameters: NotRequired[
        "capo_cloudformation.types.parameter_declarations.ParameterDeclarations"
    ]
    """<p>A list of parameter declarations that describe various properties for each parameter.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>The value that's defined in the <code>Description</code> property of the template.</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>The capabilities found within the template. If your template contains IAM resources, you must specify the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> value for this parameter when you use the <a>CreateStack</a> or <a>UpdateStack</a> actions with your template; otherwise, those actions return an <code>InsufficientCapabilities</code> error.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p>"""
    capabilities_reason: NotRequired[
        "capo_cloudformation.types.capabilities_reason.CapabilitiesReason"
    ]
    """<p>The list of resources that generated the values in the <code>Capabilities</code> response element.</p>"""
    resource_types: NotRequired[
        "capo_cloudformation.types.resource_types.ResourceTypes"
    ]
    """<p>A list of all the template resource types that are defined in the template, such as <code>AWS::EC2::Instance</code>, <code>AWS::Dynamo::Table</code>, and <code>Custom::MyCustomInstance</code>.</p>"""
    version: NotRequired["capo_cloudformation.types.version.Version"]
    """<p>The Amazon Web Services template format version, which identifies the capabilities of the template.</p>"""
    metadata: NotRequired["capo_cloudformation.types.metadata.Metadata"]
    """<p>The value that's defined for the <code>Metadata</code> property of the template.</p>"""
    declared_transforms: NotRequired[
        "capo_cloudformation.types.transforms_list.TransformsList"
    ]
    """<p>A list of the transforms that are declared in the template.</p>"""
    resource_identifier_summaries: NotRequired[
        "capo_cloudformation.types.resource_identifier_summaries.ResourceIdentifierSummaries"
    ]
    """<p>A list of resource identifier summaries that describe the target resources of an import operation and the properties you can provide during the import to identify the target resources. For example, <code>BucketName</code> is a possible identifier property for an <code>AWS::S3::Bucket</code> resource.</p>"""
    warnings: NotRequired["capo_cloudformation.types.warnings.Warnings"]
    """<p>An object that contains any warnings returned.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTemplateSummaryOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameters" in value:
        import capo_cloudformation.types.parameter_declarations

        capo_cloudformation.types.parameter_declarations.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "capabilities" in value:
        import capo_cloudformation.types.capabilities

        capo_cloudformation.types.capabilities.serialize_query(
            value["capabilities"], pairs, f"{key_prefix}Capabilities"
        )
    if "capabilities_reason" in value:
        pairs.append(
            (f"{key_prefix}CapabilitiesReason", str(value["capabilities_reason"]))
        )
    if "resource_types" in value:
        import capo_cloudformation.types.resource_types

        capo_cloudformation.types.resource_types.serialize_query(
            value["resource_types"], pairs, f"{key_prefix}ResourceTypes"
        )
    if "version" in value:
        pairs.append((f"{key_prefix}Version", str(value["version"])))
    if "metadata" in value:
        pairs.append((f"{key_prefix}Metadata", str(value["metadata"])))
    if "declared_transforms" in value:
        import capo_cloudformation.types.transforms_list

        capo_cloudformation.types.transforms_list.serialize_query(
            value["declared_transforms"], pairs, f"{key_prefix}DeclaredTransforms"
        )
    if "resource_identifier_summaries" in value:
        import capo_cloudformation.types.resource_identifier_summaries

        capo_cloudformation.types.resource_identifier_summaries.serialize_query(
            value["resource_identifier_summaries"],
            pairs,
            f"{key_prefix}ResourceIdentifierSummaries",
        )
    if "warnings" in value:
        import capo_cloudformation.types.warnings

        capo_cloudformation.types.warnings.serialize_query(
            value["warnings"], pairs, f"{key_prefix}Warnings"
        )


def deserialize_query(el: Element) -> GetTemplateSummaryOutput:
    out: GetTemplateSummaryOutput = {}  # type: ignore[typeddict-item]
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_cloudformation.types.parameter_declarations

        out["parameters"] = (
            capo_cloudformation.types.parameter_declarations.deserialize_query(
                child_parameters
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_capabilities = el.find("Capabilities")
    if child_capabilities is not None:
        import capo_cloudformation.types.capabilities

        out["capabilities"] = capo_cloudformation.types.capabilities.deserialize_query(
            child_capabilities
        )
    child_capabilities_reason = el.find("CapabilitiesReason")
    if child_capabilities_reason is not None:
        out["capabilities_reason"] = str(child_capabilities_reason.text or "")
    child_resource_types = el.find("ResourceTypes")
    if child_resource_types is not None:
        import capo_cloudformation.types.resource_types

        out["resource_types"] = (
            capo_cloudformation.types.resource_types.deserialize_query(
                child_resource_types
            )
        )
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    child_metadata = el.find("Metadata")
    if child_metadata is not None:
        out["metadata"] = str(child_metadata.text or "")
    child_declared_transforms = el.find("DeclaredTransforms")
    if child_declared_transforms is not None:
        import capo_cloudformation.types.transforms_list

        out["declared_transforms"] = (
            capo_cloudformation.types.transforms_list.deserialize_query(
                child_declared_transforms
            )
        )
    child_resource_identifier_summaries = el.find("ResourceIdentifierSummaries")
    if child_resource_identifier_summaries is not None:
        import capo_cloudformation.types.resource_identifier_summaries

        out["resource_identifier_summaries"] = (
            capo_cloudformation.types.resource_identifier_summaries.deserialize_query(
                child_resource_identifier_summaries
            )
        )
    child_warnings = el.find("Warnings")
    if child_warnings is not None:
        import capo_cloudformation.types.warnings

        out["warnings"] = capo_cloudformation.types.warnings.deserialize_query(
            child_warnings
        )
    return out
