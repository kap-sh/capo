"""Generated from Smithy shape ``com.amazonaws.mailmanager#Row``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.archived_message_id
    import capo_mailmanager.types.email_received_headers_list
    import capo_mailmanager.types.envelope
    import capo_mailmanager.types.ingress_point_id
    import capo_mailmanager.types.sender_ip_address

Row = TypedDict(
    "Row",
    {
        "archived_message_id": NotRequired[
            "capo_mailmanager.types.archived_message_id.ArchivedMessageId"
        ],
        "received_timestamp": NotRequired["datetime.datetime"],
        "date": NotRequired["str"],
        "to": NotRequired["str"],
        "from": NotRequired["str"],
        "cc": NotRequired["str"],
        "subject": NotRequired["str"],
        "message_id": NotRequired["str"],
        "has_attachments": NotRequired["bool"],
        "received_headers": NotRequired[
            "capo_mailmanager.types.email_received_headers_list.EmailReceivedHeadersList"
        ],
        "in_reply_to": NotRequired["str"],
        "x_mailer": NotRequired["str"],
        "x_original_mailer": NotRequired["str"],
        "x_priority": NotRequired["str"],
        "ingress_point_id": NotRequired[
            "capo_mailmanager.types.ingress_point_id.IngressPointId"
        ],
        "sender_hostname": NotRequired["str"],
        "sender_ip_address": NotRequired[
            "capo_mailmanager.types.sender_ip_address.SenderIpAddress"
        ],
        "envelope": NotRequired["capo_mailmanager.types.envelope.Envelope"],
        "source_arn": NotRequired["str"],
    },
    closed=True,
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Row) -> dict:
    out: dict = {}
    if "archived_message_id" in value:
        out["ArchivedMessageId"] = value["archived_message_id"]
    if "received_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["ReceivedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["received_timestamp"]
            )
        )
    if "date" in value:
        out["Date"] = value["date"]
    if "to" in value:
        out["To"] = value["to"]
    if "from" in value:
        out["From"] = value["from"]
    if "cc" in value:
        out["Cc"] = value["cc"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "has_attachments" in value:
        out["HasAttachments"] = value["has_attachments"]
    if "received_headers" in value:
        import capo_mailmanager.types.email_received_headers_list

        out["ReceivedHeaders"] = (
            capo_mailmanager.types.email_received_headers_list.serialize_aws_json_1_0(
                value["received_headers"]
            )
        )
    if "in_reply_to" in value:
        out["InReplyTo"] = value["in_reply_to"]
    if "x_mailer" in value:
        out["XMailer"] = value["x_mailer"]
    if "x_original_mailer" in value:
        out["XOriginalMailer"] = value["x_original_mailer"]
    if "x_priority" in value:
        out["XPriority"] = value["x_priority"]
    if "ingress_point_id" in value:
        out["IngressPointId"] = value["ingress_point_id"]
    if "sender_hostname" in value:
        out["SenderHostname"] = value["sender_hostname"]
    if "sender_ip_address" in value:
        out["SenderIpAddress"] = value["sender_ip_address"]
    if "envelope" in value:
        import capo_mailmanager.types.envelope

        out["Envelope"] = capo_mailmanager.types.envelope.serialize_aws_json_1_0(
            value["envelope"]
        )
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Row:
    out: Row = {}  # type: ignore[typeddict-item]
    if data.get("ArchivedMessageId") is not None:
        out["archived_message_id"] = data["ArchivedMessageId"]
    if data.get("ReceivedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["received_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ReceivedTimestamp"]
            )
        )
    if data.get("Date") is not None:
        out["date"] = data["Date"]
    if data.get("To") is not None:
        out["to"] = data["To"]
    if data.get("From") is not None:
        out["from"] = data["From"]
    if data.get("Cc") is not None:
        out["cc"] = data["Cc"]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    if data.get("HasAttachments") is not None:
        out["has_attachments"] = data["HasAttachments"]
    if data.get("ReceivedHeaders") is not None:
        import capo_mailmanager.types.email_received_headers_list

        out["received_headers"] = (
            capo_mailmanager.types.email_received_headers_list.deserialize_aws_json_1_0(
                data["ReceivedHeaders"]
            )
        )
    if data.get("InReplyTo") is not None:
        out["in_reply_to"] = data["InReplyTo"]
    if data.get("XMailer") is not None:
        out["x_mailer"] = data["XMailer"]
    if data.get("XOriginalMailer") is not None:
        out["x_original_mailer"] = data["XOriginalMailer"]
    if data.get("XPriority") is not None:
        out["x_priority"] = data["XPriority"]
    if data.get("IngressPointId") is not None:
        out["ingress_point_id"] = data["IngressPointId"]
    if data.get("SenderHostname") is not None:
        out["sender_hostname"] = data["SenderHostname"]
    if data.get("SenderIpAddress") is not None:
        out["sender_ip_address"] = data["SenderIpAddress"]
    if data.get("Envelope") is not None:
        import capo_mailmanager.types.envelope

        out["envelope"] = capo_mailmanager.types.envelope.deserialize_aws_json_1_0(
            data["Envelope"]
        )
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    return out


def redact_sensitive(value: Row) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender_ip_address" in value:
        out["sender_ip_address"] = "*** Sensitive Data Redacted ***"
    return out
