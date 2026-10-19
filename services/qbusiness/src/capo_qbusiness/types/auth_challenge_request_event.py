"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeRequestEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_qbusiness.types.url


class AuthChallengeRequestEvent(TypedDict, closed=True):
    authorization_url: "capo_qbusiness.types.url.Url"
    """<p>The URL sent by Amazon Q Business to a third party authentication server in response to an authentication verification event activated by an end user request to use a custom plugin. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthChallengeRequestEvent) -> dict:
    out: dict = {}
    out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> AuthChallengeRequestEvent:
    out: AuthChallengeRequestEvent = {}  # type: ignore[typeddict-item]
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    else:
        out["authorization_url"] = ""
    return out


def serialize_event_json(value: AuthChallengeRequestEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "authChallengeRequestEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AuthChallengeRequestEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AuthChallengeRequestEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
