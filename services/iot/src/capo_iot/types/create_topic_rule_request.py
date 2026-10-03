"""Generated from Smithy shape ``com.amazonaws.iot#CreateTopicRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.rule_name
    import capo_iot.types.string
    import capo_iot.types.topic_rule_payload


class CreateTopicRuleRequest(TypedDict, closed=True):
    rule_name: "capo_iot.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    topic_rule_payload: "capo_iot.types.topic_rule_payload.TopicRulePayload"
    """<p>The rule payload.</p>"""
    tags: NotRequired["capo_iot.types.string.String"]
    """<p>Metadata which can be used to manage the topic rule.</p> <note> <p>For URI Request parameters use format: ...key1=value1&key2=value2...</p> <p>For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..."</p> <p>For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicRuleRequest) -> dict:
    out: dict = {}
    import capo_iot.types.topic_rule_payload

    out["topicRulePayload"] = capo_iot.types.topic_rule_payload.serialize_json(
        value["topic_rule_payload"]
    )
    return out


def deserialize_json(data: dict) -> CreateTopicRuleRequest:
    out: CreateTopicRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("topicRulePayload") is not None:
        import capo_iot.types.topic_rule_payload

        out["topic_rule_payload"] = capo_iot.types.topic_rule_payload.deserialize_json(
            data["topicRulePayload"]
        )
    else:
        raise DeserializationError("CreateTopicRuleRequest.topic_rule_payload required")
    return out
