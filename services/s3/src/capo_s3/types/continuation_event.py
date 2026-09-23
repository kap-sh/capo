"""Generated from Smithy shape ``com.amazonaws.s3#ContinuationEvent``."""

from typing_extensions import TypedDict

from capo_s3._protocol.eventstream import HeaderValue, Message
from capo_s3._protocol.xml import Element, SubElement, fromstring, tostring


class ContinuationEvent(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: ContinuationEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ContinuationEvent:
    out: ContinuationEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_xml(value: ContinuationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "Cont",
        ":content-type": "application/xml",
    }
    payload = b""
    _payload_root = Element("_")
    serialize_xml(value, _payload_root, "ContinuationEvent")
    payload = tostring(_payload_root[0])
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_xml(message: Message) -> ContinuationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ContinuationEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_xml(fromstring(payload))
    return out
