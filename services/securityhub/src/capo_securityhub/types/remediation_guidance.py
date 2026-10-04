"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationGuidance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.remediation_guidance_context
    import capo_securityhub.types.remediation_guidance_examples
    import capo_securityhub.types.remediation_guidance_metadata
    import capo_securityhub.types.remediation_guidance_specification


class RemediationGuidance(TypedDict, closed=True):
    target_type_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the remediation target type.</p>"""
    pattern: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The remediation pattern of the remediation target.</p>"""
    version: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The guidance version.</p>"""
    context: NotRequired[
        "capo_securityhub.types.remediation_guidance_context.RemediationGuidanceContext"
    ]
    """<p>The context behind the remediation target's existence and guidance.</p>"""
    specification: NotRequired[
        "capo_securityhub.types.remediation_guidance_specification.RemediationGuidanceSpecification"
    ]
    """<p>The specification of the remediation target guidance. This outlines required resource parameters and permissions, remediation steps, and the end state.</p>"""
    examples: NotRequired[
        "capo_securityhub.types.remediation_guidance_examples.RemediationGuidanceExamples"
    ]
    """<p>Provided remediation guidance examples in different formats that can be run for remediating the target.</p>"""
    metadata: NotRequired[
        "capo_securityhub.types.remediation_guidance_metadata.RemediationGuidanceMetadata"
    ]
    """<p>The metadata of the remediation guidance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationGuidance) -> dict:
    out: dict = {}
    if "target_type_name" in value:
        out["TargetTypeName"] = value["target_type_name"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    if "version" in value:
        out["Version"] = value["version"]
    if "context" in value:
        import capo_securityhub.types.remediation_guidance_context

        out["Context"] = (
            capo_securityhub.types.remediation_guidance_context.serialize_json(
                value["context"]
            )
        )
    if "specification" in value:
        import capo_securityhub.types.remediation_guidance_specification

        out["Specification"] = (
            capo_securityhub.types.remediation_guidance_specification.serialize_json(
                value["specification"]
            )
        )
    if "examples" in value:
        import capo_securityhub.types.remediation_guidance_examples

        out["Examples"] = (
            capo_securityhub.types.remediation_guidance_examples.serialize_json(
                value["examples"]
            )
        )
    if "metadata" in value:
        import capo_securityhub.types.remediation_guidance_metadata

        out["Metadata"] = (
            capo_securityhub.types.remediation_guidance_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemediationGuidance:
    out: RemediationGuidance = {}  # type: ignore[typeddict-item]
    if data.get("TargetTypeName") is not None:
        out["target_type_name"] = data["TargetTypeName"]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("Context") is not None:
        import capo_securityhub.types.remediation_guidance_context

        out["context"] = (
            capo_securityhub.types.remediation_guidance_context.deserialize_json(
                data["Context"]
            )
        )
    if data.get("Specification") is not None:
        import capo_securityhub.types.remediation_guidance_specification

        out["specification"] = (
            capo_securityhub.types.remediation_guidance_specification.deserialize_json(
                data["Specification"]
            )
        )
    if data.get("Examples") is not None:
        import capo_securityhub.types.remediation_guidance_examples

        out["examples"] = (
            capo_securityhub.types.remediation_guidance_examples.deserialize_json(
                data["Examples"]
            )
        )
    if data.get("Metadata") is not None:
        import capo_securityhub.types.remediation_guidance_metadata

        out["metadata"] = (
            capo_securityhub.types.remediation_guidance_metadata.deserialize_json(
                data["Metadata"]
            )
        )
    return out
