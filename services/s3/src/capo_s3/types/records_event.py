"""Generated from Smithy shape ``com.amazonaws.s3#RecordsEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.eventstream import HeaderValue, Message
from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.body


class RecordsEvent(TypedDict, closed=True):
    payload: NotRequired["capo_s3.types.body.Body"]
    """<p>The byte array of partial, one or more result records. S3 Select doesn't guarantee that a record will be self-contained in one record frame. To ensure continuous streaming of data, S3 Select might split the same record across multiple record frames instead of aggregating the results in memory. Some S3 clients (for example, the SDK for Java) handle this behavior by creating a <code>ByteStream</code> out of the response by default. Other clients might not handle this behavior by default. In those cases, you must aggregate the results on the client side and parse the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RecordsEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> RecordsEvent:
    out: RecordsEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_xml(value: RecordsEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "Records",
        ":content-type": "application/octet-stream",
    }
    payload = b""
    payload = value["payload"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_xml(message: Message) -> RecordsEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: RecordsEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out["payload"] = payload
    return out
