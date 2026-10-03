"""Generated from Smithy shape ``com.amazonaws.ses#RecipientDsnFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.address
    import capo_ses.types.diagnostic_code
    import capo_ses.types.dsn_action
    import capo_ses.types.dsn_status
    import capo_ses.types.extension_field_list
    import capo_ses.types.last_attempt_date
    import capo_ses.types.remote_mta


class RecipientDsnFields(TypedDict, closed=True):
    final_recipient: NotRequired["capo_ses.types.address.Address"]
    """<p>The email address that the message was ultimately delivered to. This corresponds to the <code>Final-Recipient</code> in the DSN. If not specified, <code>FinalRecipient</code> is set to the <code>Recipient</code> specified in the <code>BouncedRecipientInfo</code> structure. Either <code>FinalRecipient</code> or the recipient in <code>BouncedRecipientInfo</code> must be a recipient of the original bounced message.</p> <note> <p>Do not prepend the <code>FinalRecipient</code> email address with <code>rfc 822;</code>, as described in <a href="https://tools.ietf.org/html/rfc3798">RFC 3798</a>.</p> </note>"""
    action: "capo_ses.types.dsn_action.DsnAction"
    """<p>The action performed by the reporting mail transfer agent (MTA) as a result of its attempt to deliver the message to the recipient address. This is required by <a href="https://tools.ietf.org/html/rfc3464">RFC 3464</a>.</p>"""
    remote_mta: NotRequired["capo_ses.types.remote_mta.RemoteMta"]
    """<p>The MTA to which the remote MTA attempted to deliver the message, formatted as specified in <a href="https://tools.ietf.org/html/rfc3464">RFC 3464</a> (<code>mta-name-type; mta-name</code>). This parameter typically applies only to propagating synchronous bounces.</p>"""
    status: "capo_ses.types.dsn_status.DsnStatus"
    """<p>The status code that indicates what went wrong. This is required by <a href="https://tools.ietf.org/html/rfc3464">RFC 3464</a>.</p>"""
    diagnostic_code: NotRequired["capo_ses.types.diagnostic_code.DiagnosticCode"]
    """<p>An extended explanation of what went wrong; this is usually an SMTP response. See <a href="https://tools.ietf.org/html/rfc3463">RFC 3463</a> for the correct formatting of this parameter.</p>"""
    last_attempt_date: NotRequired["capo_ses.types.last_attempt_date.LastAttemptDate"]
    """<p>The time the final delivery attempt was made, in <a href="https://www.ietf.org/rfc/rfc0822.txt">RFC 822</a> date-time format.</p>"""
    extension_fields: NotRequired[
        "capo_ses.types.extension_field_list.ExtensionFieldList"
    ]
    """<p>Additional X-headers to include in the DSN.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecipientDsnFields, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "final_recipient" in value:
        pairs.append((f"{key_prefix}FinalRecipient", str(value["final_recipient"])))
    import capo_ses.types.dsn_action

    capo_ses.types.dsn_action.serialize_query(
        value["action"], pairs, f"{key_prefix}Action"
    )
    if "remote_mta" in value:
        pairs.append((f"{key_prefix}RemoteMta", str(value["remote_mta"])))
    pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "diagnostic_code" in value:
        pairs.append((f"{key_prefix}DiagnosticCode", str(value["diagnostic_code"])))
    if "last_attempt_date" in value:
        import capo_ses.types.last_attempt_date

        capo_ses.types.last_attempt_date.serialize_query(
            value["last_attempt_date"], pairs, f"{key_prefix}LastAttemptDate"
        )
    if "extension_fields" in value:
        import capo_ses.types.extension_field_list

        capo_ses.types.extension_field_list.serialize_query(
            value["extension_fields"], pairs, f"{key_prefix}ExtensionFields"
        )


def deserialize_query(el: Element) -> RecipientDsnFields:
    out: RecipientDsnFields = {}  # type: ignore[typeddict-item]
    child_final_recipient = el.find("FinalRecipient")
    if child_final_recipient is not None:
        out["final_recipient"] = str(child_final_recipient.text or "")
    child_action = el.find("Action")
    if child_action is not None:
        import capo_ses.types.dsn_action

        out["action"] = capo_ses.types.dsn_action.deserialize_query(child_action)
    else:
        raise DeserializationError("RecipientDsnFields.action required")
    child_remote_mta = el.find("RemoteMta")
    if child_remote_mta is not None:
        out["remote_mta"] = str(child_remote_mta.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        raise DeserializationError("RecipientDsnFields.status required")
    child_diagnostic_code = el.find("DiagnosticCode")
    if child_diagnostic_code is not None:
        out["diagnostic_code"] = str(child_diagnostic_code.text or "")
    child_last_attempt_date = el.find("LastAttemptDate")
    if child_last_attempt_date is not None:
        import capo_ses.types.last_attempt_date

        out["last_attempt_date"] = capo_ses.types.last_attempt_date.deserialize_query(
            child_last_attempt_date
        )
    child_extension_fields = el.find("ExtensionFields")
    if child_extension_fields is not None:
        import capo_ses.types.extension_field_list

        out["extension_fields"] = capo_ses.types.extension_field_list.deserialize_query(
            child_extension_fields
        )
    return out
