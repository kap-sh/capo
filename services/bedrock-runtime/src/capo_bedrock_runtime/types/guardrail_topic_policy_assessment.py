"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTopicPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_topic_list


class GuardrailTopicPolicyAssessment(TypedDict, closed=True):
    topics: "capo_bedrock_runtime.types.guardrail_topic_list.GuardrailTopicList"
    """<p>The topics in the assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicPolicyAssessment) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_topic_list

    out["topics"] = capo_bedrock_runtime.types.guardrail_topic_list.serialize_json(
        value["topics"]
    )
    return out


def deserialize_json(data: dict) -> GuardrailTopicPolicyAssessment:
    out: GuardrailTopicPolicyAssessment = {}  # type: ignore[typeddict-item]
    if data.get("topics") is not None:
        import capo_bedrock_runtime.types.guardrail_topic_list

        out["topics"] = (
            capo_bedrock_runtime.types.guardrail_topic_list.deserialize_json(
                data["topics"]
            )
        )
    else:
        out["topics"] = []
    return out
