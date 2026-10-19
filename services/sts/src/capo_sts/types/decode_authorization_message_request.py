"""Generated from Smithy shape ``com.amazonaws.sts#DecodeAuthorizationMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.encoded_message_type


class DecodeAuthorizationMessageRequest(TypedDict, closed=True):
    encoded_message: "capo_sts.types.encoded_message_type.encodedMessageType"
    """<p>The encoded message that was returned with the response.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DecodeAuthorizationMessageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EncodedMessage", str(value["encoded_message"])))


def deserialize_query(el: Element) -> DecodeAuthorizationMessageRequest:
    out: DecodeAuthorizationMessageRequest = {}  # type: ignore[typeddict-item]
    child_encoded_message = el.find("EncodedMessage")
    if child_encoded_message is not None:
        out["encoded_message"] = str(child_encoded_message.text or "")
    else:
        out["encoded_message"] = ""
    return out
