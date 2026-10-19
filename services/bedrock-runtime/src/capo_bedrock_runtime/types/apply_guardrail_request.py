"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ApplyGuardrailRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_content_block_list
    import capo_bedrock_runtime.types.guardrail_content_source
    import capo_bedrock_runtime.types.guardrail_identifier
    import capo_bedrock_runtime.types.guardrail_output_scope
    import capo_bedrock_runtime.types.guardrail_version


class ApplyGuardrailRequest(TypedDict, closed=True):
    guardrail_identifier: (
        "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
    )
    """<p>The guardrail identifier used in the request to apply the guardrail.</p>"""
    guardrail_version: "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
    """<p>The guardrail version used in the request to apply the guardrail.</p>"""
    source: "capo_bedrock_runtime.types.guardrail_content_source.GuardrailContentSource"
    """<p>The source of data used in the request to apply the guardrail.</p>"""
    content: "capo_bedrock_runtime.types.guardrail_content_block_list.GuardrailContentBlockList"
    """<p>The content details used in the request to apply the guardrail.</p>"""
    output_scope: NotRequired[
        "capo_bedrock_runtime.types.guardrail_output_scope.GuardrailOutputScope"
    ]
    """<p>Specifies the scope of the output that you get in the response. Set to <code>FULL</code> to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.</p> <p>Note that the full output scope doesn't apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplyGuardrailRequest) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_content_source

    out["source"] = capo_bedrock_runtime.types.guardrail_content_source.serialize_json(
        value["source"]
    )
    import capo_bedrock_runtime.types.guardrail_content_block_list

    out["content"] = (
        capo_bedrock_runtime.types.guardrail_content_block_list.serialize_json(
            value["content"]
        )
    )
    if "output_scope" in value:
        import capo_bedrock_runtime.types.guardrail_output_scope

        out["outputScope"] = (
            capo_bedrock_runtime.types.guardrail_output_scope.serialize_json(
                value["output_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplyGuardrailRequest:
    out: ApplyGuardrailRequest = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_bedrock_runtime.types.guardrail_content_source

        out["source"] = (
            capo_bedrock_runtime.types.guardrail_content_source.deserialize_json(
                data["source"]
            )
        )
    else:
        import typing

        out["source"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_content_source.GuardrailContentSource",
            "",
        )
    if data.get("content") is not None:
        import capo_bedrock_runtime.types.guardrail_content_block_list

        out["content"] = (
            capo_bedrock_runtime.types.guardrail_content_block_list.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = []
    if data.get("outputScope") is not None:
        import capo_bedrock_runtime.types.guardrail_output_scope

        out["output_scope"] = (
            capo_bedrock_runtime.types.guardrail_output_scope.deserialize_json(
                data["outputScope"]
            )
        )
    return out


def redact_sensitive(value: ApplyGuardrailRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_runtime.types.guardrail_content_block_list

        out["content"] = (
            capo_bedrock_runtime.types.guardrail_content_block_list.redact_sensitive(
                value["content"]
            )
        )
    return out
