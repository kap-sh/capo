"""Generated from Smithy shape ``com.amazonaws.s3#ProgressEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.eventstream import HeaderValue, Message
from capo_s3._protocol.xml import Element, SubElement, fromstring, tostring

if TYPE_CHECKING:
    import capo_s3.types.progress


class ProgressEvent(TypedDict, closed=True):
    details: NotRequired["capo_s3.types.progress.Progress"]
    """<p>The Progress event details.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ProgressEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ProgressEvent:
    out: ProgressEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_xml(value: ProgressEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "Progress",
        ":content-type": "application/xml",
    }
    payload = b""
    import capo_s3.types.progress

    _payload_root = Element("_")
    capo_s3.types.progress.serialize_xml(value["details"], _payload_root, "Details")
    payload = tostring(_payload_root[0])
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_xml(message: Message) -> ProgressEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ProgressEvent = {}  # type: ignore[typeddict-item]
    if payload:
        import capo_s3.types.progress

        out["details"] = capo_s3.types.progress.deserialize_xml(fromstring(payload))
    return out
