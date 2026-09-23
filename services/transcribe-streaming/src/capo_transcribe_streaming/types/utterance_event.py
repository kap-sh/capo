"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#UtteranceEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.boolean
    import capo_transcribe_streaming.types.call_analytics_entity_list
    import capo_transcribe_streaming.types.call_analytics_item_list
    import capo_transcribe_streaming.types.call_analytics_language_code
    import capo_transcribe_streaming.types.call_analytics_language_identification
    import capo_transcribe_streaming.types.issues_detected
    import capo_transcribe_streaming.types.long
    import capo_transcribe_streaming.types.participant_role
    import capo_transcribe_streaming.types.sentiment
    import capo_transcribe_streaming.types.string


class UtteranceEvent(TypedDict, closed=True):
    utterance_id: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>The unique identifier that is associated with the specified <code>UtteranceEvent</code>.</p>"""
    is_partial: "capo_transcribe_streaming.types.boolean.Boolean"
    """<p>Indicates whether the segment in the <code>UtteranceEvent</code> is complete (<code>FALSE</code>) or partial (<code>TRUE</code>).</p>"""
    participant_role: NotRequired[
        "capo_transcribe_streaming.types.participant_role.ParticipantRole"
    ]
    """<p>Provides the role of the speaker for each audio channel, either <code>CUSTOMER</code> or <code>AGENT</code>.</p>"""
    begin_offset_millis: NotRequired["capo_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the start of the <code>UtteranceEvent</code>.</p>"""
    end_offset_millis: NotRequired["capo_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the start of the <code>UtteranceEvent</code>.</p>"""
    transcript: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>Contains transcribed text.</p>"""
    items: NotRequired[
        "capo_transcribe_streaming.types.call_analytics_item_list.CallAnalyticsItemList"
    ]
    """<p>Contains words, phrases, or punctuation marks that are associated with the specified <code>UtteranceEvent</code>.</p>"""
    entities: NotRequired[
        "capo_transcribe_streaming.types.call_analytics_entity_list.CallAnalyticsEntityList"
    ]
    """<p>Contains entities identified as personally identifiable information (PII) in your transcription output.</p>"""
    sentiment: NotRequired["capo_transcribe_streaming.types.sentiment.Sentiment"]
    """<p>Provides the sentiment that was detected in the specified segment.</p>"""
    issues_detected: NotRequired[
        "capo_transcribe_streaming.types.issues_detected.IssuesDetected"
    ]
    """<p>Provides the issue that was detected in the specified segment.</p>"""
    language_code: NotRequired[
        "capo_transcribe_streaming.types.call_analytics_language_code.CallAnalyticsLanguageCode"
    ]
    """<p>The language code that represents the language spoken in your audio stream.</p>"""
    language_identification: NotRequired[
        "capo_transcribe_streaming.types.call_analytics_language_identification.CallAnalyticsLanguageIdentification"
    ]
    """<p>The language code of the dominant language identified in your stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceEvent) -> dict:
    out: dict = {}
    if "utterance_id" in value:
        out["UtteranceId"] = value["utterance_id"]
    out["IsPartial"] = value.get("is_partial", False)
    if "participant_role" in value:
        import capo_transcribe_streaming.types.participant_role

        out["ParticipantRole"] = (
            capo_transcribe_streaming.types.participant_role.serialize_json(
                value["participant_role"]
            )
        )
    if "begin_offset_millis" in value:
        out["BeginOffsetMillis"] = value["begin_offset_millis"]
    if "end_offset_millis" in value:
        out["EndOffsetMillis"] = value["end_offset_millis"]
    if "transcript" in value:
        out["Transcript"] = value["transcript"]
    if "items" in value:
        import capo_transcribe_streaming.types.call_analytics_item_list

        out["Items"] = (
            capo_transcribe_streaming.types.call_analytics_item_list.serialize_json(
                value["items"]
            )
        )
    if "entities" in value:
        import capo_transcribe_streaming.types.call_analytics_entity_list

        out["Entities"] = (
            capo_transcribe_streaming.types.call_analytics_entity_list.serialize_json(
                value["entities"]
            )
        )
    if "sentiment" in value:
        import capo_transcribe_streaming.types.sentiment

        out["Sentiment"] = capo_transcribe_streaming.types.sentiment.serialize_json(
            value["sentiment"]
        )
    if "issues_detected" in value:
        import capo_transcribe_streaming.types.issues_detected

        out["IssuesDetected"] = (
            capo_transcribe_streaming.types.issues_detected.serialize_json(
                value["issues_detected"]
            )
        )
    if "language_code" in value:
        import capo_transcribe_streaming.types.call_analytics_language_code

        out["LanguageCode"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "language_identification" in value:
        import capo_transcribe_streaming.types.call_analytics_language_identification

        out["LanguageIdentification"] = (
            capo_transcribe_streaming.types.call_analytics_language_identification.serialize_json(
                value["language_identification"]
            )
        )
    return out


def deserialize_json(data: dict) -> UtteranceEvent:
    out: UtteranceEvent = {}  # type: ignore[typeddict-item]
    if data.get("UtteranceId") is not None:
        out["utterance_id"] = data["UtteranceId"]
    if data.get("IsPartial") is not None:
        out["is_partial"] = data["IsPartial"]
    else:
        out["is_partial"] = False
    if data.get("ParticipantRole") is not None:
        import capo_transcribe_streaming.types.participant_role

        out["participant_role"] = (
            capo_transcribe_streaming.types.participant_role.deserialize_json(
                data["ParticipantRole"]
            )
        )
    if data.get("BeginOffsetMillis") is not None:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    if data.get("EndOffsetMillis") is not None:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    if data.get("Transcript") is not None:
        out["transcript"] = data["Transcript"]
    if data.get("Items") is not None:
        import capo_transcribe_streaming.types.call_analytics_item_list

        out["items"] = (
            capo_transcribe_streaming.types.call_analytics_item_list.deserialize_json(
                data["Items"]
            )
        )
    if data.get("Entities") is not None:
        import capo_transcribe_streaming.types.call_analytics_entity_list

        out["entities"] = (
            capo_transcribe_streaming.types.call_analytics_entity_list.deserialize_json(
                data["Entities"]
            )
        )
    if data.get("Sentiment") is not None:
        import capo_transcribe_streaming.types.sentiment

        out["sentiment"] = capo_transcribe_streaming.types.sentiment.deserialize_json(
            data["Sentiment"]
        )
    if data.get("IssuesDetected") is not None:
        import capo_transcribe_streaming.types.issues_detected

        out["issues_detected"] = (
            capo_transcribe_streaming.types.issues_detected.deserialize_json(
                data["IssuesDetected"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_transcribe_streaming.types.call_analytics_language_code

        out["language_code"] = (
            capo_transcribe_streaming.types.call_analytics_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if data.get("LanguageIdentification") is not None:
        import capo_transcribe_streaming.types.call_analytics_language_identification

        out["language_identification"] = (
            capo_transcribe_streaming.types.call_analytics_language_identification.deserialize_json(
                data["LanguageIdentification"]
            )
        )
    return out


def serialize_event_json(value: UtteranceEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "UtteranceEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> UtteranceEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: UtteranceEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
