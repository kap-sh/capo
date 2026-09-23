"""Generated from Smithy shape ``com.amazonaws.s3#EndEvent``."""

from typing_extensions import TypedDict

from capo_s3._protocol.eventstream import HeaderValue, Message
from capo_s3._protocol.xml import Element, SubElement, fromstring, tostring


class EndEvent(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: EndEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> EndEvent:
    out: EndEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_xml(value: EndEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "End",
        ":content-type": "application/xml",
    }
    payload = b""
    _payload_root = Element("_")
    serialize_xml(value, _payload_root, "EndEvent")
    payload = tostring(_payload_root[0])
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_xml(message: Message) -> EndEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: EndEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_xml(fromstring(payload))
    return out
