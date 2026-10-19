"""Generated from Smithy shape ``com.amazonaws.iot#UpdateTopicRuleDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.topic_rule_destination_status


class UpdateTopicRuleDestinationRequest(TypedDict, closed=True):
    arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the topic rule destination.</p>"""
    status: "capo_iot.types.topic_rule_destination_status.TopicRuleDestinationStatus"
    """<p>The status of the topic rule destination. Valid values are:</p> <dl> <dt>IN_PROGRESS</dt> <dd> <p>A topic rule destination was created but has not been confirmed. You can set <code>status</code> to <code>IN_PROGRESS</code> by calling <code>UpdateTopicRuleDestination</code>. Calling <code>UpdateTopicRuleDestination</code> causes a new confirmation challenge to be sent to your confirmation endpoint.</p> </dd> <dt>ENABLED</dt> <dd> <p>Confirmation was completed, and traffic to this destination is allowed. You can set <code>status</code> to <code>DISABLED</code> by calling <code>UpdateTopicRuleDestination</code>.</p> </dd> <dt>DISABLED</dt> <dd> <p>Confirmation was completed, and traffic to this destination is not allowed. You can set <code>status</code> to <code>ENABLED</code> by calling <code>UpdateTopicRuleDestination</code>.</p> </dd> <dt>ERROR</dt> <dd> <p>Confirmation could not be completed, for example if the confirmation timed out. You can call <code>GetTopicRuleDestination</code> for details about the error. You can set <code>status</code> to <code>IN_PROGRESS</code> by calling <code>UpdateTopicRuleDestination</code>. Calling <code>UpdateTopicRuleDestination</code> causes a new confirmation challenge to be sent to your confirmation endpoint.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicRuleDestinationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_iot.types.topic_rule_destination_status

    out["status"] = capo_iot.types.topic_rule_destination_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTopicRuleDestinationRequest:
    out: UpdateTopicRuleDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_iot.types.topic_rule_destination_status

        out["status"] = capo_iot.types.topic_rule_destination_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iot.types.topic_rule_destination_status.TopicRuleDestinationStatus",
            "",
        )
    return out
