"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeliverToMailboxAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.action_failure_policy
    import capo_mailmanager.types.iam_role_arn
    import capo_mailmanager.types.name_or_arn


class DeliverToMailboxAction(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "capo_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the mailbox ARN is no longer valid.</p>"""
    mailbox_arn: "capo_mailmanager.types.name_or_arn.NameOrArn"
    """<p>The Amazon Resource Name (ARN) of a WorkMail organization to deliver the email to.</p>"""
    role_arn: "capo_mailmanager.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role to use to execute this action. The role must have access to the workmail:DeliverToMailbox API.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeliverToMailboxAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import capo_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            capo_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["MailboxArn"] = value["mailbox_arn"]
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeliverToMailboxAction:
    out: DeliverToMailboxAction = {}  # type: ignore[typeddict-item]
    if data.get("ActionFailurePolicy") is not None:
        import capo_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            capo_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if data.get("MailboxArn") is not None:
        out["mailbox_arn"] = data["MailboxArn"]
    else:
        out["mailbox_arn"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
