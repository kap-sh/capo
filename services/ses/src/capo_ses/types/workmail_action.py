"""Generated from Smithy shape ``com.amazonaws.ses#WorkmailAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.amazon_resource_name


class WorkmailAction(TypedDict, closed=True):
    topic_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. You can find the ARN of a topic by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html">ListTopics</a> operation in Amazon SNS.</p> <p>For more information about Amazon SNS topics, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">Amazon SNS Developer Guide</a>.</p>"""
    organization_arn: "capo_ses.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon WorkMail organization. Amazon WorkMail ARNs use the following format:</p> <p> <code>arn:aws:workmail:<region>:<awsAccountId>:organization/<workmailOrganizationId></code> </p> <p>You can find the ID of your organization by using the <a href="https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListOrganizations.html">ListOrganizations</a> operation in Amazon WorkMail. Amazon WorkMail organization IDs begin with "<code>m-</code>", followed by a string of alphanumeric characters.</p> <p>For information about Amazon WorkMail organizations, see the <a href="https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html">Amazon WorkMail Administrator Guide</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: WorkmailAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    pairs.append((f"{key_prefix}OrganizationArn", str(value["organization_arn"])))


def deserialize_query(el: Element) -> WorkmailAction:
    out: WorkmailAction = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_organization_arn = el.find("OrganizationArn")
    if child_organization_arn is not None:
        out["organization_arn"] = str(child_organization_arn.text or "")
    else:
        raise DeserializationError("WorkmailAction.organization_arn required")
    return out
