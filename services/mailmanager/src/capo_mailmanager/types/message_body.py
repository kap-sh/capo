"""Generated from Smithy shape ``com.amazonaws.mailmanager#MessageBody``."""

from typing_extensions import NotRequired, TypedDict


class MessageBody(TypedDict, closed=True):
    text: NotRequired["str"]
    """<p>The plain text body content of the message.</p>"""
    html: NotRequired["str"]
    """<p>The HTML body content of the message.</p>"""
    message_malformed: NotRequired["bool"]
    """<p>A flag indicating if the email was malformed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageBody) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "html" in value:
        out["Html"] = value["html"]
    if "message_malformed" in value:
        out["MessageMalformed"] = value["message_malformed"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageBody:
    out: MessageBody = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Html") is not None:
        out["html"] = data["Html"]
    if data.get("MessageMalformed") is not None:
        out["message_malformed"] = data["MessageMalformed"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MessageBody) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "html" in value:
        out["Html"] = value["html"]
    if "message_malformed" in value:
        out["MessageMalformed"] = value["message_malformed"]
    return out


def deserialize_cbor(data: dict) -> MessageBody:
    out: MessageBody = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("Html") is not None:
        out["html"] = data["Html"]
    if data.get("MessageMalformed") is not None:
        out["message_malformed"] = data["MessageMalformed"]
    return out
