"""Generated from Smithy shape ``com.amazonaws.ses#MessageDsn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.arrival_date
    import capo_ses.types.extension_field_list
    import capo_ses.types.reporting_mta


class MessageDsn(TypedDict, closed=True):
    reporting_mta: "capo_ses.types.reporting_mta.ReportingMta"
    """<p>The reporting MTA that attempted to deliver the message, formatted as specified in <a href="https://tools.ietf.org/html/rfc3464">RFC 3464</a> (<code>mta-name-type; mta-name</code>). The default value is <code>dns; inbound-smtp.[region].amazonaws.com</code>.</p>"""
    arrival_date: NotRequired["capo_ses.types.arrival_date.ArrivalDate"]
    """<p>When the message was received by the reporting mail transfer agent (MTA), in <a href="https://www.ietf.org/rfc/rfc0822.txt">RFC 822</a> date-time format.</p>"""
    extension_fields: NotRequired[
        "capo_ses.types.extension_field_list.ExtensionFieldList"
    ]
    """<p>Additional X-headers to include in the DSN.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MessageDsn, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ReportingMta", str(value["reporting_mta"])))
    if "arrival_date" in value:
        import capo_ses.types.arrival_date

        capo_ses.types.arrival_date.serialize_query(
            value["arrival_date"], pairs, f"{key_prefix}ArrivalDate"
        )
    if "extension_fields" in value:
        import capo_ses.types.extension_field_list

        capo_ses.types.extension_field_list.serialize_query(
            value["extension_fields"], pairs, f"{key_prefix}ExtensionFields"
        )


def deserialize_query(el: Element) -> MessageDsn:
    out: MessageDsn = {}  # type: ignore[typeddict-item]
    child_reporting_mta = el.find("ReportingMta")
    if child_reporting_mta is not None:
        out["reporting_mta"] = str(child_reporting_mta.text or "")
    else:
        raise DeserializationError("MessageDsn.reporting_mta required")
    child_arrival_date = el.find("ArrivalDate")
    if child_arrival_date is not None:
        import capo_ses.types.arrival_date

        out["arrival_date"] = capo_ses.types.arrival_date.deserialize_query(
            child_arrival_date
        )
    child_extension_fields = el.find("ExtensionFields")
    if child_extension_fields is not None:
        import capo_ses.types.extension_field_list

        out["extension_fields"] = capo_ses.types.extension_field_list.deserialize_query(
            child_extension_fields
        )
    return out
