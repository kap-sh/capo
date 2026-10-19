"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeResponseEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_qbusiness.types.authorization_response_map


class AuthChallengeResponseEvent(TypedDict, closed=True):
    response_map: (
        "capo_qbusiness.types.authorization_response_map.AuthorizationResponseMap"
    )
    """<p>The mapping of key-value pairs in an authentication challenge response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthChallengeResponseEvent) -> dict:
    out: dict = {}
    import capo_qbusiness.types.authorization_response_map

    out["responseMap"] = capo_qbusiness.types.authorization_response_map.serialize_json(
        value["response_map"]
    )
    return out


def deserialize_json(data: dict) -> AuthChallengeResponseEvent:
    out: AuthChallengeResponseEvent = {}  # type: ignore[typeddict-item]
    if data.get("responseMap") is not None:
        import capo_qbusiness.types.authorization_response_map

        out["response_map"] = (
            capo_qbusiness.types.authorization_response_map.deserialize_json(
                data["responseMap"]
            )
        )
    else:
        out["response_map"] = {}
    return out


def serialize_event_json(value: AuthChallengeResponseEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "authChallengeResponseEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AuthChallengeResponseEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AuthChallengeResponseEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
