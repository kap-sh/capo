"""Generated from Smithy shape ``com.amazonaws.detective#CreateMembersRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.account_list
    import capo_detective.types.boolean
    import capo_detective.types.email_message
    import capo_detective.types.graph_arn


class CreateMembersRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph.</p>"""
    message: NotRequired["capo_detective.types.email_message.EmailMessage"]
    """<p>Customized message text to include in the invitation email message to the invited member accounts.</p>"""
    disable_email_notification: NotRequired["capo_detective.types.boolean.Boolean"]
    """<p>if set to <code>true</code>, then the invited accounts do not receive email notifications. By default, this is set to <code>false</code>, and the invited accounts receive email notifications.</p> <p>Organization accounts in the organization behavior graph do not receive email notifications.</p>"""
    accounts: "capo_detective.types.account_list.AccountList"
    """<p>The list of Amazon Web Services accounts to invite or to enable. You can invite or enable up to 50 accounts at a time. For each invited account, the account list contains the account identifier and the Amazon Web Services account root user email address. For organization accounts in the organization behavior graph, the email address is not required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembersRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    if "disable_email_notification" in value:
        out["DisableEmailNotification"] = value["disable_email_notification"]
    import capo_detective.types.account_list

    out["Accounts"] = capo_detective.types.account_list.serialize_json(
        value["accounts"]
    )
    return out


def deserialize_json(data: dict) -> CreateMembersRequest:
    out: CreateMembersRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("DisableEmailNotification") is not None:
        out["disable_email_notification"] = data["DisableEmailNotification"]
    if data.get("Accounts") is not None:
        import capo_detective.types.account_list

        out["accounts"] = capo_detective.types.account_list.deserialize_json(
            data["Accounts"]
        )
    else:
        out["accounts"] = []
    return out


def redact_sensitive(value: CreateMembersRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    if "accounts" in value:
        import capo_detective.types.account_list

        out["accounts"] = capo_detective.types.account_list.redact_sensitive(
            value["accounts"]
        )
    return out
