"""Generated from Smithy shape ``com.amazonaws.ses#RawMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.raw_message_data


class RawMessage(TypedDict, closed=True):
    data: "capo_ses.types.raw_message_data.RawMessageData"
    """<p>The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you. In all cases, the client must ensure that the message format complies with Internet email standards regarding email header fields, MIME types, and MIME encoding.</p> <p>The To:, CC:, and BCC: headers in the raw message can contain a group list.</p> <p>If you are using <code>SendRawEmail</code> with sending authorization, you can include X-headers in the raw message to specify the "Source," "From," and "Return-Path" addresses. For more information, see the documentation for <code>SendRawEmail</code>. </p> <important> <p>Do not include these X-headers in the DKIM signature, because they are removed by Amazon SES before sending the email.</p> </important> <p>For more information, go to the <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html">Amazon SES Developer Guide</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RawMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.raw_message_data

    capo_ses.types.raw_message_data.serialize_query(
        value["data"], pairs, f"{key_prefix}Data"
    )


def deserialize_query(el: Element) -> RawMessage:
    out: RawMessage = {}  # type: ignore[typeddict-item]
    child_data = el.find("Data")
    if child_data is not None:
        import capo_ses.types.raw_message_data

        out["data"] = capo_ses.types.raw_message_data.deserialize_query(child_data)
    else:
        raise DeserializationError("RawMessage.data required")
    return out
