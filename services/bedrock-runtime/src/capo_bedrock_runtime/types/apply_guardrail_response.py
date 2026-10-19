"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ApplyGuardrailResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_action
    import capo_bedrock_runtime.types.guardrail_assessment_list
    import capo_bedrock_runtime.types.guardrail_coverage
    import capo_bedrock_runtime.types.guardrail_output_content_list
    import capo_bedrock_runtime.types.guardrail_usage


class ApplyGuardrailResponse(TypedDict, closed=True):
    usage: "capo_bedrock_runtime.types.guardrail_usage.GuardrailUsage"
    """<p>The usage details in the response from the guardrail.</p>"""
    action: "capo_bedrock_runtime.types.guardrail_action.GuardrailAction"
    """<p>The action taken in the response from the guardrail.</p>"""
    action_reason: NotRequired["str"]
    """<p>The reason for the action taken when harmful content is detected.</p>"""
    outputs: "capo_bedrock_runtime.types.guardrail_output_content_list.GuardrailOutputContentList"
    """<p>The output details in the response from the guardrail.</p>"""
    assessments: (
        "capo_bedrock_runtime.types.guardrail_assessment_list.GuardrailAssessmentList"
    )
    """<p>The assessment details in the response from the guardrail.</p>"""
    guardrail_coverage: NotRequired[
        "capo_bedrock_runtime.types.guardrail_coverage.GuardrailCoverage"
    ]
    """<p>The guardrail coverage details in the apply guardrail response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplyGuardrailResponse) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_usage

    out["usage"] = capo_bedrock_runtime.types.guardrail_usage.serialize_json(
        value["usage"]
    )
    import capo_bedrock_runtime.types.guardrail_action

    out["action"] = capo_bedrock_runtime.types.guardrail_action.serialize_json(
        value["action"]
    )
    if "action_reason" in value:
        out["actionReason"] = value["action_reason"]
    import capo_bedrock_runtime.types.guardrail_output_content_list

    out["outputs"] = (
        capo_bedrock_runtime.types.guardrail_output_content_list.serialize_json(
            value["outputs"]
        )
    )
    import capo_bedrock_runtime.types.guardrail_assessment_list

    out["assessments"] = (
        capo_bedrock_runtime.types.guardrail_assessment_list.serialize_json(
            value["assessments"]
        )
    )
    if "guardrail_coverage" in value:
        import capo_bedrock_runtime.types.guardrail_coverage

        out["guardrailCoverage"] = (
            capo_bedrock_runtime.types.guardrail_coverage.serialize_json(
                value["guardrail_coverage"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplyGuardrailResponse:
    out: ApplyGuardrailResponse = {}  # type: ignore[typeddict-item]
    if data.get("usage") is not None:
        import capo_bedrock_runtime.types.guardrail_usage

        out["usage"] = capo_bedrock_runtime.types.guardrail_usage.deserialize_json(
            data["usage"]
        )
    else:
        raise DeserializationError("ApplyGuardrailResponse.usage required")
    if data.get("action") is not None:
        import capo_bedrock_runtime.types.guardrail_action

        out["action"] = capo_bedrock_runtime.types.guardrail_action.deserialize_json(
            data["action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_action.GuardrailAction", ""
        )
    if data.get("actionReason") is not None:
        out["action_reason"] = data["actionReason"]
    if data.get("outputs") is not None:
        import capo_bedrock_runtime.types.guardrail_output_content_list

        out["outputs"] = (
            capo_bedrock_runtime.types.guardrail_output_content_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        out["outputs"] = []
    if data.get("assessments") is not None:
        import capo_bedrock_runtime.types.guardrail_assessment_list

        out["assessments"] = (
            capo_bedrock_runtime.types.guardrail_assessment_list.deserialize_json(
                data["assessments"]
            )
        )
    else:
        out["assessments"] = []
    if data.get("guardrailCoverage") is not None:
        import capo_bedrock_runtime.types.guardrail_coverage

        out["guardrail_coverage"] = (
            capo_bedrock_runtime.types.guardrail_coverage.deserialize_json(
                data["guardrailCoverage"]
            )
        )
    return out


def redact_sensitive(value: ApplyGuardrailResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assessments" in value:
        import capo_bedrock_runtime.types.guardrail_assessment_list

        out["assessments"] = (
            capo_bedrock_runtime.types.guardrail_assessment_list.redact_sensitive(
                value["assessments"]
            )
        )
    return out
