"""Generated from Smithy shape ``com.amazonaws.cloudformation#ValidateTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.capabilities_reason
    import capo_cloudformation.types.description
    import capo_cloudformation.types.template_parameters
    import capo_cloudformation.types.transforms_list


class ValidateTemplateOutput(TypedDict, closed=True):
    parameters: NotRequired[
        "capo_cloudformation.types.template_parameters.TemplateParameters"
    ]
    """<p>A list of <code>TemplateParameter</code> structures.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>The description found within the template.</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM value for this parameter when you use the <a>CreateStack</a> or <a>UpdateStack</a> actions with your template; otherwise, those actions return an InsufficientCapabilities error.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p>"""
    capabilities_reason: NotRequired[
        "capo_cloudformation.types.capabilities_reason.CapabilitiesReason"
    ]
    """<p>The list of resources that generated the values in the <code>Capabilities</code> response element.</p>"""
    declared_transforms: NotRequired[
        "capo_cloudformation.types.transforms_list.TransformsList"
    ]
    """<p>A list of the transforms that are declared in the template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidateTemplateOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameters" in value:
        import capo_cloudformation.types.template_parameters

        capo_cloudformation.types.template_parameters.serialize_query(
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
    if "declared_transforms" in value:
        import capo_cloudformation.types.transforms_list

        capo_cloudformation.types.transforms_list.serialize_query(
            value["declared_transforms"], pairs, f"{key_prefix}DeclaredTransforms"
        )


def deserialize_query(el: Element) -> ValidateTemplateOutput:
    out: ValidateTemplateOutput = {}  # type: ignore[typeddict-item]
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_cloudformation.types.template_parameters

        out["parameters"] = (
            capo_cloudformation.types.template_parameters.deserialize_query(
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
    child_declared_transforms = el.find("DeclaredTransforms")
    if child_declared_transforms is not None:
        import capo_cloudformation.types.transforms_list

        out["declared_transforms"] = (
            capo_cloudformation.types.transforms_list.deserialize_query(
                child_declared_transforms
            )
        )
    return out
