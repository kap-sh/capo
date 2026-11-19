"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#Transcript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.issues_detected
    import capo_connect_contact_lens.types.language_code
    import capo_connect_contact_lens.types.offset_millis
    import capo_connect_contact_lens.types.participant_id
    import capo_connect_contact_lens.types.participant_role
    import capo_connect_contact_lens.types.sentiment_value
    import capo_connect_contact_lens.types.transcript_content
    import capo_connect_contact_lens.types.transcript_id


class Transcript(TypedDict, closed=True):
    id: NotRequired["capo_connect_contact_lens.types.transcript_id.TranscriptId"]
    """<p>The identifier of the transcript.</p>"""
    participant_id: NotRequired[
        "capo_connect_contact_lens.types.participant_id.ParticipantId"
    ]
    """<p>The identifier of the participant. Valid values are CUSTOMER or AGENT.</p>"""
    participant_role: NotRequired[
        "capo_connect_contact_lens.types.participant_role.ParticipantRole"
    ]
    """<p>The role of participant. For example, is it a customer, agent, or system.</p>"""
    content: NotRequired[
        "capo_connect_contact_lens.types.transcript_content.TranscriptContent"
    ]
    """<p>The content of the transcript.</p>"""
    begin_offset_millis: NotRequired[
        "capo_connect_contact_lens.types.offset_millis.OffsetMillis"
    ]
    """<p>The beginning offset in the contact for this transcript.</p>"""
    end_offset_millis: NotRequired[
        "capo_connect_contact_lens.types.offset_millis.OffsetMillis"
    ]
    """<p>The end offset in the contact for this transcript.</p>"""
    sentiment: NotRequired[
        "capo_connect_contact_lens.types.sentiment_value.SentimentValue"
    ]
    """<p>The sentiment detected for this piece of transcript.</p>"""
    issues_detected: NotRequired[
        "capo_connect_contact_lens.types.issues_detected.IssuesDetected"
    ]
    """<p>List of positions where issues were detected on the transcript.</p>"""
    language_code: NotRequired[
        "capo_connect_contact_lens.types.language_code.LanguageCode"
    ]
    """<p>The language code detected for this piece of transcript, for example, <code>en-US</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transcript) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "participant_id" in value:
        out["ParticipantId"] = value["participant_id"]
    if "participant_role" in value:
        out["ParticipantRole"] = value["participant_role"]
    if "content" in value:
        out["Content"] = value["content"]
    if "begin_offset_millis" in value:
        out["BeginOffsetMillis"] = value["begin_offset_millis"]
    if "end_offset_millis" in value:
        out["EndOffsetMillis"] = value["end_offset_millis"]
    if "sentiment" in value:
        import capo_connect_contact_lens.types.sentiment_value

        out["Sentiment"] = (
            capo_connect_contact_lens.types.sentiment_value.serialize_json(
                value["sentiment"]
            )
        )
    if "issues_detected" in value:
        import capo_connect_contact_lens.types.issues_detected

        out["IssuesDetected"] = (
            capo_connect_contact_lens.types.issues_detected.serialize_json(
                value["issues_detected"]
            )
        )
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    return out


def deserialize_json(data: dict) -> Transcript:
    out: Transcript = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ParticipantId") is not None:
        out["participant_id"] = data["ParticipantId"]
    if data.get("ParticipantRole") is not None:
        out["participant_role"] = data["ParticipantRole"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("BeginOffsetMillis") is not None:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    if data.get("EndOffsetMillis") is not None:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    if data.get("Sentiment") is not None:
        import capo_connect_contact_lens.types.sentiment_value

        out["sentiment"] = (
            capo_connect_contact_lens.types.sentiment_value.deserialize_json(
                data["Sentiment"]
            )
        )
    if data.get("IssuesDetected") is not None:
        import capo_connect_contact_lens.types.issues_detected

        out["issues_detected"] = (
            capo_connect_contact_lens.types.issues_detected.deserialize_json(
                data["IssuesDetected"]
            )
        )
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    return out
