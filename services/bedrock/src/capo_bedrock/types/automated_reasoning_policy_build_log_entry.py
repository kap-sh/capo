"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildLogEntry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation
    import capo_bedrock.types.automated_reasoning_policy_annotation_status
    import capo_bedrock.types.automated_reasoning_policy_build_step_list


class AutomatedReasoningPolicyBuildLogEntry(TypedDict, closed=True):
    annotation: "capo_bedrock.types.automated_reasoning_policy_annotation.AutomatedReasoningPolicyAnnotation"
    """<p>The annotation or operation that was being processed when this log entry was created.</p>"""
    status: "capo_bedrock.types.automated_reasoning_policy_annotation_status.AutomatedReasoningPolicyAnnotationStatus"
    """<p>The status of the build step (e.g., SUCCESS, FAILED, IN_PROGRESS).</p>"""
    build_steps: "capo_bedrock.types.automated_reasoning_policy_build_step_list.AutomatedReasoningPolicyBuildStepList"
    """<p>Detailed information about the specific build steps that were executed, including any sub-operations or transformations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildLogEntry) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_annotation

    out["annotation"] = (
        capo_bedrock.types.automated_reasoning_policy_annotation.serialize_json(
            value["annotation"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_annotation_status

    out["status"] = (
        capo_bedrock.types.automated_reasoning_policy_annotation_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_build_step_list

    out["buildSteps"] = (
        capo_bedrock.types.automated_reasoning_policy_build_step_list.serialize_json(
            value["build_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildLogEntry:
    out: AutomatedReasoningPolicyBuildLogEntry = {}  # type: ignore[typeddict-item]
    if data.get("annotation") is not None:
        import capo_bedrock.types.automated_reasoning_policy_annotation

        out["annotation"] = (
            capo_bedrock.types.automated_reasoning_policy_annotation.deserialize_json(
                data["annotation"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildLogEntry.annotation required"
        )
    if data.get("status") is not None:
        import capo_bedrock.types.automated_reasoning_policy_annotation_status

        out["status"] = (
            capo_bedrock.types.automated_reasoning_policy_annotation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildLogEntry.status required"
        )
    if data.get("buildSteps") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_step_list

        out["build_steps"] = (
            capo_bedrock.types.automated_reasoning_policy_build_step_list.deserialize_json(
                data["buildSteps"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildLogEntry.build_steps required"
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyBuildLogEntry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "annotation" in value:
        import capo_bedrock.types.automated_reasoning_policy_annotation

        out["annotation"] = (
            capo_bedrock.types.automated_reasoning_policy_annotation.redact_sensitive(
                value["annotation"]
            )
        )
    if "build_steps" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_step_list

        out["build_steps"] = (
            capo_bedrock.types.automated_reasoning_policy_build_step_list.redact_sensitive(
                value["build_steps"]
            )
        )
    return out
