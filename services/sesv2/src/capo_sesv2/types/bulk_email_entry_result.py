"""Generated from Smithy shape ``com.amazonaws.sesv2#BulkEmailEntryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.bulk_email_status
    import capo_sesv2.types.error_message
    import capo_sesv2.types.outbound_message_id


class BulkEmailEntryResult(TypedDict, closed=True):
    status: NotRequired["capo_sesv2.types.bulk_email_status.BulkEmailStatus"]
    """<p>The status of a message sent using the <code>SendBulkTemplatedEmail</code> operation.</p> <p>Possible values for this parameter include:</p> <ul> <li> <p>SUCCESS: Amazon SES accepted the message, and will attempt to deliver it to the recipients.</p> </li> <li> <p>MESSAGE_REJECTED: The message was rejected because it contained a virus.</p> </li> <li> <p>MAIL_FROM_DOMAIN_NOT_VERIFIED: The sender's email address or domain was not verified.</p> </li> <li> <p>CONFIGURATION_SET_DOES_NOT_EXIST: The configuration set you specified does not exist.</p> </li> <li> <p>TEMPLATE_DOES_NOT_EXIST: The template you specified does not exist.</p> </li> <li> <p>ACCOUNT_SUSPENDED: Your account has been shut down because of issues related to your email sending practices.</p> </li> <li> <p>ACCOUNT_THROTTLED: The number of emails you can send has been reduced because your account has exceeded its allocated sending limit.</p> </li> <li> <p>ACCOUNT_DAILY_QUOTA_EXCEEDED: You have reached or exceeded the maximum number of emails you can send from your account in a 24-hour period.</p> </li> <li> <p>INVALID_SENDING_POOL_NAME: The configuration set you specified refers to an IP pool that does not exist.</p> </li> <li> <p>ACCOUNT_SENDING_PAUSED: Email sending for the Amazon SES account was disabled using the <a href="https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateAccountSendingEnabled.html">UpdateAccountSendingEnabled</a> operation.</p> </li> <li> <p>CONFIGURATION_SET_SENDING_PAUSED: Email sending for this configuration set was disabled using the <a href="https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetSendingEnabled.html">UpdateConfigurationSetSendingEnabled</a> operation.</p> </li> <li> <p>INVALID_PARAMETER_VALUE: One or more of the parameters you specified when calling this operation was invalid. See the error message for additional information.</p> </li> <li> <p>TRANSIENT_FAILURE: Amazon SES was unable to process your request because of a temporary issue.</p> </li> <li> <p>FAILED: Amazon SES was unable to process your request. See the error message for additional information.</p> </li> </ul>"""
    error: NotRequired["capo_sesv2.types.error_message.ErrorMessage"]
    """<p>A description of an error that prevented a message being sent using the <code>SendBulkTemplatedEmail</code> operation.</p>"""
    message_id: NotRequired["capo_sesv2.types.outbound_message_id.OutboundMessageId"]
    """<p>The unique message identifier returned from the <code>SendBulkTemplatedEmail</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BulkEmailEntryResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_sesv2.types.bulk_email_status

        out["Status"] = capo_sesv2.types.bulk_email_status.serialize_json(
            value["status"]
        )
    if "error" in value:
        out["Error"] = value["error"]
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    return out


def deserialize_json(data: dict) -> BulkEmailEntryResult:
    out: BulkEmailEntryResult = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_sesv2.types.bulk_email_status

        out["status"] = capo_sesv2.types.bulk_email_status.deserialize_json(
            data["Status"]
        )
    if data.get("Error") is not None:
        out["error"] = data["Error"]
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    return out
