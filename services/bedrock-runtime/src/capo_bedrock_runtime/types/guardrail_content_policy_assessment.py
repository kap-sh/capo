"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_content_filter_list


class GuardrailContentPolicyAssessment(TypedDict, closed=True):
    filters: "capo_bedrock_runtime.types.guardrail_content_filter_list.GuardrailContentFilterList"
    """<p>The content policy filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentPolicyAssessment) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_content_filter_list

    out["filters"] = (
        capo_bedrock_runtime.types.guardrail_content_filter_list.serialize_json(
            value["filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailContentPolicyAssessment:
    out: GuardrailContentPolicyAssessment = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_bedrock_runtime.types.guardrail_content_filter_list

        out["filters"] = (
            capo_bedrock_runtime.types.guardrail_content_filter_list.deserialize_json(
                data["filters"]
            )
        )
    else:
        out["filters"] = []
    return out
