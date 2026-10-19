"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentFilterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_result_list


class GuardrailChecksContentFilterResult(TypedDict, closed=True):
    results: "capo_bedrock_runtime.types.guardrail_checks_content_filter_result_list.GuardrailChecksContentFilterResultList"
    """<p>The per-category content filter results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentFilterResult) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_content_filter_result_list

    out["results"] = (
        capo_bedrock_runtime.types.guardrail_checks_content_filter_result_list.serialize_json(
            value["results"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksContentFilterResult:
    out: GuardrailChecksContentFilterResult = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_content_filter_result_list

        out["results"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_filter_result_list.deserialize_json(
                data["results"]
            )
        )
    else:
        out["results"] = []
    return out
