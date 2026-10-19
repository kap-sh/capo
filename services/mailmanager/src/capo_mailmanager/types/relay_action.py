"""Generated from Smithy shape ``com.amazonaws.mailmanager#RelayAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.action_failure_policy
    import capo_mailmanager.types.id_or_arn
    import capo_mailmanager.types.mail_from


class RelayAction(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "capo_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified relay has been deleted.</p>"""
    relay: "capo_mailmanager.types.id_or_arn.IdOrArn"
    """<p>The identifier of the relay resource to be used when relaying an email.</p>"""
    mail_from: NotRequired["capo_mailmanager.types.mail_from.MailFrom"]
    """<p>This action specifies whether to preserve or replace original mail from address while relaying received emails to a destination server.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelayAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import capo_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            capo_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["Relay"] = value["relay"]
    if "mail_from" in value:
        import capo_mailmanager.types.mail_from

        out["MailFrom"] = capo_mailmanager.types.mail_from.serialize_aws_json_1_0(
            value["mail_from"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RelayAction:
    out: RelayAction = {}  # type: ignore[typeddict-item]
    if data.get("ActionFailurePolicy") is not None:
        import capo_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            capo_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if data.get("Relay") is not None:
        out["relay"] = data["Relay"]
    else:
        out["relay"] = ""
    if data.get("MailFrom") is not None:
        import capo_mailmanager.types.mail_from

        out["mail_from"] = capo_mailmanager.types.mail_from.deserialize_aws_json_1_0(
            data["MailFrom"]
        )
    return out
