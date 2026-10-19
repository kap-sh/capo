"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksSensitiveInformationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_list


class GuardrailChecksSensitiveInformationResult(TypedDict, closed=True):
    results: "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_list.GuardrailChecksSensitiveInformationResultList"
    """<p>The detected sensitive information entities.</p>"""
    truncated: NotRequired["bool"]
    """<p>Specifies whether the results were truncated because the number of detected entities exceeded the maximum limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksSensitiveInformationResult) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_list

    out["results"] = (
        capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_list.serialize_json(
            value["results"]
        )
    )
    if "truncated" in value:
        out["truncated"] = value["truncated"]
    return out


def deserialize_json(data: dict) -> GuardrailChecksSensitiveInformationResult:
    out: GuardrailChecksSensitiveInformationResult = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_list

        out["results"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_result_list.deserialize_json(
                data["results"]
            )
        )
    else:
        out["results"] = []
    if data.get("truncated") is not None:
        out["truncated"] = data["truncated"]
    return out
