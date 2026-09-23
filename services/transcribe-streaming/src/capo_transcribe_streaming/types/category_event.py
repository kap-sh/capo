"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CategoryEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.matched_category_details
    import capo_transcribe_streaming.types.string_list


class CategoryEvent(TypedDict, closed=True):
    matched_categories: NotRequired[
        "capo_transcribe_streaming.types.string_list.StringList"
    ]
    """<p>Lists the categories that were matched in your audio segment.</p>"""
    matched_details: NotRequired[
        "capo_transcribe_streaming.types.matched_category_details.MatchedCategoryDetails"
    ]
    """<p>Contains information about the matched categories, including category names and timestamps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryEvent) -> dict:
    out: dict = {}
    if "matched_categories" in value:
        import capo_transcribe_streaming.types.string_list

        out["MatchedCategories"] = (
            capo_transcribe_streaming.types.string_list.serialize_json(
                value["matched_categories"]
            )
        )
    if "matched_details" in value:
        import capo_transcribe_streaming.types.matched_category_details

        out["MatchedDetails"] = (
            capo_transcribe_streaming.types.matched_category_details.serialize_json(
                value["matched_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CategoryEvent:
    out: CategoryEvent = {}  # type: ignore[typeddict-item]
    if data.get("MatchedCategories") is not None:
        import capo_transcribe_streaming.types.string_list

        out["matched_categories"] = (
            capo_transcribe_streaming.types.string_list.deserialize_json(
                data["MatchedCategories"]
            )
        )
    if data.get("MatchedDetails") is not None:
        import capo_transcribe_streaming.types.matched_category_details

        out["matched_details"] = (
            capo_transcribe_streaming.types.matched_category_details.deserialize_json(
                data["MatchedDetails"]
            )
        )
    return out


def serialize_event_json(value: CategoryEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "CategoryEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> CategoryEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: CategoryEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
