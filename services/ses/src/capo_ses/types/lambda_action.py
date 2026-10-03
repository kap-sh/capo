"""Generated from Smithy shape ``com.amazonaws.ses#LambdaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.invocation_type


class LambdaAction(TypedDict, closed=True):
    topic_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed. You can find the ARN of a topic by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html">ListTopics</a> operation in Amazon SNS.</p> <p>For more information about Amazon SNS topics, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">Amazon SNS Developer Guide</a>.</p>"""
    function_arn: "capo_ses.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Lambda function. An example of an Amazon Web Services Lambda function ARN is <code>arn:aws:lambda:us-west-2:account-id:function:MyFunction</code>. For more information about Amazon Web Services Lambda, see the <a href="https://docs.aws.amazon.com/lambda/latest/dg/welcome.html">Amazon Web Services Lambda Developer Guide</a>.</p>"""
    invocation_type: NotRequired["capo_ses.types.invocation_type.InvocationType"]
    """<p>The invocation type of the Amazon Web Services Lambda function. An invocation type of <code>RequestResponse</code> means that the execution of the function immediately results in a response, and a value of <code>Event</code> means that the function is invoked asynchronously. The default value is <code>Event</code>. For information about Amazon Web Services Lambda invocation types, see the <a href="https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html">Amazon Web Services Lambda Developer Guide</a>.</p> <important> <p>There is a 30-second timeout on <code>RequestResponse</code> invocations. You should use <code>Event</code> invocation in most cases. Use <code>RequestResponse</code> only to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.</p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LambdaAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    pairs.append((f"{key_prefix}FunctionArn", str(value["function_arn"])))
    if "invocation_type" in value:
        import capo_ses.types.invocation_type

        capo_ses.types.invocation_type.serialize_query(
            value["invocation_type"], pairs, f"{key_prefix}InvocationType"
        )


def deserialize_query(el: Element) -> LambdaAction:
    out: LambdaAction = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_function_arn = el.find("FunctionArn")
    if child_function_arn is not None:
        out["function_arn"] = str(child_function_arn.text or "")
    else:
        raise DeserializationError("LambdaAction.function_arn required")
    child_invocation_type = el.find("InvocationType")
    if child_invocation_type is not None:
        import capo_ses.types.invocation_type

        out["invocation_type"] = capo_ses.types.invocation_type.deserialize_query(
            child_invocation_type
        )
    return out
