"""Generated from Smithy shape ``com.amazonaws.ses#StopAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.stop_scope


class StopAction(TypedDict, closed=True):
    scope: "capo_ses.types.stop_scope.StopScope"
    """<p>The scope of the StopAction. The only acceptable value is <code>RuleSet</code>.</p>"""
    topic_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. You can find the ARN of a topic by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html">ListTopics</a> Amazon SNS operation.</p> <p>For more information about Amazon SNS topics, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">Amazon SNS Developer Guide</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StopAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.stop_scope

    capo_ses.types.stop_scope.serialize_query(
        value["scope"], pairs, f"{key_prefix}Scope"
    )
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))


def deserialize_query(el: Element) -> StopAction:
    out: StopAction = {}  # type: ignore[typeddict-item]
    child_scope = el.find("Scope")
    if child_scope is not None:
        import capo_ses.types.stop_scope

        out["scope"] = capo_ses.types.stop_scope.deserialize_query(child_scope)
    else:
        raise DeserializationError("StopAction.scope required")
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    return out
