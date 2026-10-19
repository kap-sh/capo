"""Generated from Smithy shape ``com.amazonaws.mailmanager#BounceAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.action_failure_policy
    import capo_mailmanager.types.bounce_message
    import capo_mailmanager.types.diagnostic_message
    import capo_mailmanager.types.email_address
    import capo_mailmanager.types.iam_role_arn
    import capo_mailmanager.types.smtp_reply_code
    import capo_mailmanager.types.status_code


class BounceAction(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "capo_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the caller does not have the permissions to call the SendBounce API.</p>"""
    role_arn: "capo_mailmanager.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to use to send the bounce message.</p>"""
    sender: "capo_mailmanager.types.email_address.EmailAddress"
    """<p>The sender email address of the bounce message.</p>"""
    status_code: "capo_mailmanager.types.status_code.StatusCode"
    """<p>The enhanced status code for the bounce, in the format of x.y.z (e.g. 5.1.1).</p>"""
    smtp_reply_code: "capo_mailmanager.types.smtp_reply_code.SmtpReplyCode"
    """<p>The SMTP reply code for the bounce, as defined by RFC 5321.</p>"""
    diagnostic_message: "capo_mailmanager.types.diagnostic_message.DiagnosticMessage"
    """<p>The diagnostic message included in the Diagnostic-Code header of the bounce.</p>"""
    message: NotRequired["capo_mailmanager.types.bounce_message.BounceMessage"]
    """<p>The human-readable text to include in the bounce message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BounceAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import capo_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            capo_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    out["Sender"] = value["sender"]
    out["StatusCode"] = value["status_code"]
    out["SmtpReplyCode"] = value["smtp_reply_code"]
    out["DiagnosticMessage"] = value["diagnostic_message"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BounceAction:
    out: BounceAction = {}  # type: ignore[typeddict-item]
    if data.get("ActionFailurePolicy") is not None:
        import capo_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            capo_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("Sender") is not None:
        out["sender"] = data["Sender"]
    else:
        out["sender"] = ""
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    else:
        out["status_code"] = ""
    if data.get("SmtpReplyCode") is not None:
        out["smtp_reply_code"] = data["SmtpReplyCode"]
    else:
        out["smtp_reply_code"] = ""
    if data.get("DiagnosticMessage") is not None:
        out["diagnostic_message"] = data["DiagnosticMessage"]
    else:
        out["diagnostic_message"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


def redact_sensitive(value: BounceAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender" in value:
        out["sender"] = "*** Sensitive Data Redacted ***"
    if "diagnostic_message" in value:
        out["diagnostic_message"] = "*** Sensitive Data Redacted ***"
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
