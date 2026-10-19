"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopic``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_topic_action
    import capo_bedrock.types.guardrail_topic_definition
    import capo_bedrock.types.guardrail_topic_examples
    import capo_bedrock.types.guardrail_topic_name
    import capo_bedrock.types.guardrail_topic_type


class GuardrailTopic(TypedDict, closed=True):
    name: "capo_bedrock.types.guardrail_topic_name.GuardrailTopicName"
    """<p>The name of the topic to deny.</p>"""
    definition: "capo_bedrock.types.guardrail_topic_definition.GuardrailTopicDefinition"
    """<p>A definition of the topic to deny.</p>"""
    examples: NotRequired[
        "capo_bedrock.types.guardrail_topic_examples.GuardrailTopicExamples"
    ]
    """<p>A list of prompts, each of which is an example of a prompt that can be categorized as belonging to the topic.</p>"""
    type: NotRequired["capo_bedrock.types.guardrail_topic_type.GuardrailTopicType"]
    """<p>Specifies to deny the topic.</p>"""
    input_action: NotRequired[
        "capo_bedrock.types.guardrail_topic_action.GuardrailTopicAction"
    ]
    """<p>The action to take when harmful content is detected in the input. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    output_action: NotRequired[
        "capo_bedrock.types.guardrail_topic_action.GuardrailTopicAction"
    ]
    """<p>The action to take when harmful content is detected in the output. Supported values include:</p> <ul> <li> <p> <code>BLOCK</code> – Block the content and replace it with blocked messaging.</p> </li> <li> <p> <code>NONE</code> – Take no action but return detection information in the trace response.</p> </li> </ul>"""
    input_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""
    output_enabled: NotRequired["bool"]
    """<p>Indicates whether guardrail evaluation is enabled on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopic) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["definition"] = value["definition"]
    if "examples" in value:
        import capo_bedrock.types.guardrail_topic_examples

        out["examples"] = capo_bedrock.types.guardrail_topic_examples.serialize_json(
            value["examples"]
        )
    if "type" in value:
        import capo_bedrock.types.guardrail_topic_type

        out["type"] = capo_bedrock.types.guardrail_topic_type.serialize_json(
            value["type"]
        )
    if "input_action" in value:
        import capo_bedrock.types.guardrail_topic_action

        out["inputAction"] = capo_bedrock.types.guardrail_topic_action.serialize_json(
            value["input_action"]
        )
    if "output_action" in value:
        import capo_bedrock.types.guardrail_topic_action

        out["outputAction"] = capo_bedrock.types.guardrail_topic_action.serialize_json(
            value["output_action"]
        )
    if "input_enabled" in value:
        out["inputEnabled"] = value["input_enabled"]
    if "output_enabled" in value:
        out["outputEnabled"] = value["output_enabled"]
    return out


def deserialize_json(data: dict) -> GuardrailTopic:
    out: GuardrailTopic = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        out["definition"] = ""
    if data.get("examples") is not None:
        import capo_bedrock.types.guardrail_topic_examples

        out["examples"] = capo_bedrock.types.guardrail_topic_examples.deserialize_json(
            data["examples"]
        )
    if data.get("type") is not None:
        import capo_bedrock.types.guardrail_topic_type

        out["type"] = capo_bedrock.types.guardrail_topic_type.deserialize_json(
            data["type"]
        )
    if data.get("inputAction") is not None:
        import capo_bedrock.types.guardrail_topic_action

        out["input_action"] = (
            capo_bedrock.types.guardrail_topic_action.deserialize_json(
                data["inputAction"]
            )
        )
    if data.get("outputAction") is not None:
        import capo_bedrock.types.guardrail_topic_action

        out["output_action"] = (
            capo_bedrock.types.guardrail_topic_action.deserialize_json(
                data["outputAction"]
            )
        )
    if data.get("inputEnabled") is not None:
        out["input_enabled"] = data["inputEnabled"]
    if data.get("outputEnabled") is not None:
        out["output_enabled"] = data["outputEnabled"]
    return out


def redact_sensitive(value: GuardrailTopic) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "definition" in value:
        out["definition"] = "*** Sensitive Data Redacted ***"
    if "examples" in value:
        import capo_bedrock.types.guardrail_topic_examples

        out["examples"] = capo_bedrock.types.guardrail_topic_examples.redact_sensitive(
            value["examples"]
        )
    if "input_action" in value:
        out["input_action"] = "*** Sensitive Data Redacted ***"
    if "output_action" in value:
        out["output_action"] = "*** Sensitive Data Redacted ***"
    return out
