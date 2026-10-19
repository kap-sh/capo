"""Generated from Smithy shape ``com.amazonaws.sns#AddPermissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.actions_list
    import capo_sns.types.delegates_list
    import capo_sns.types.label
    import capo_sns.types.topic_arn


class AddPermissionInput(TypedDict, closed=True):
    topic_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic whose access control policy you wish to modify.</p>"""
    label: "capo_sns.types.label.label"
    """<p>A unique identifier for the new policy statement.</p>"""
    aws_account_id: "capo_sns.types.delegates_list.DelegatesList"
    """<p>The Amazon Web Services account IDs of the users (principals) who will be given access to the specified actions. The users must have Amazon Web Services account, but do not need to be signed up for this service.</p>"""
    action_name: "capo_sns.types.actions_list.ActionsList"
    """<p>The action you want to allow for the specified principal(s).</p> <p>Valid values: Any Amazon SNS action name, for example <code>Publish</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddPermissionInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    pairs.append((f"{key_prefix}Label", str(value["label"])))
    import capo_sns.types.delegates_list

    capo_sns.types.delegates_list.serialize_query(
        value["aws_account_id"], pairs, f"{key_prefix}AWSAccountId"
    )
    import capo_sns.types.actions_list

    capo_sns.types.actions_list.serialize_query(
        value["action_name"], pairs, f"{key_prefix}ActionName"
    )


def deserialize_query(el: Element) -> AddPermissionInput:
    out: AddPermissionInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        out["topic_arn"] = ""
    child_label = el.find("Label")
    if child_label is not None:
        out["label"] = str(child_label.text or "")
    else:
        out["label"] = ""
    child_aws_account_id = el.find("AWSAccountId")
    if child_aws_account_id is not None:
        import capo_sns.types.delegates_list

        out["aws_account_id"] = capo_sns.types.delegates_list.deserialize_query(
            child_aws_account_id
        )
    else:
        out["aws_account_id"] = []
    child_action_name = el.find("ActionName")
    if child_action_name is not None:
        import capo_sns.types.actions_list

        out["action_name"] = capo_sns.types.actions_list.deserialize_query(
            child_action_name
        )
    else:
        out["action_name"] = []
    return out
