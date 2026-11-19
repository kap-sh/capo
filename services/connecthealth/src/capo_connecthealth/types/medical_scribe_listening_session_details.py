"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeListeningSessionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.medical_scribe_channel_definitions
    import capo_connecthealth.types.medical_scribe_language_code
    import capo_connecthealth.types.medical_scribe_media_encoding
    import capo_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import capo_connecthealth.types.medical_scribe_post_stream_action_settings_response
    import capo_connecthealth.types.medical_scribe_post_stream_actions_result
    import capo_connecthealth.types.medical_scribe_stream_status
    import capo_connecthealth.types.non_null_boolean
    import capo_connecthealth.types.scribe_session_id
    import capo_connecthealth.types.subscription_id


class MedicalScribeListeningSessionDetails(TypedDict, closed=True):
    session_id: NotRequired[
        "capo_connecthealth.types.scribe_session_id.ScribeSessionId"
    ]
    """<p>The Session identifier</p>"""
    domain_id: NotRequired["capo_connecthealth.types.domain_id.DomainId"]
    """<p>The Domain identifier</p>"""
    subscription_id: NotRequired[
        "capo_connecthealth.types.subscription_id.SubscriptionId"
    ]
    """<p>The Subscription identifier</p>"""
    language_code: NotRequired[
        "capo_connecthealth.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The Language Code for the audio in the session</p>"""
    media_sample_rate_hertz: NotRequired[
        "capo_connecthealth.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    ]
    """<p>The sample rate of the input audio</p>"""
    media_encoding: NotRequired[
        "capo_connecthealth.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    ]
    """<p>The encoding for the input audio</p>"""
    channel_definitions: NotRequired[
        "capo_connecthealth.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>Channel definitions for the audio stream</p>"""
    post_stream_action_settings: NotRequired[
        "capo_connecthealth.types.medical_scribe_post_stream_action_settings_response.MedicalScribePostStreamActionSettingsResponse"
    ]
    """<p>Settings for post-stream actions</p>"""
    post_stream_action_result: NotRequired[
        "capo_connecthealth.types.medical_scribe_post_stream_actions_result.MedicalScribePostStreamActionsResult"
    ]
    """<p>Results of post-stream actions</p>"""
    encounter_context_provided: NotRequired[
        "capo_connecthealth.types.non_null_boolean.NonNullBoolean"
    ]
    """<p>Indicates whether encounter context was provided</p>"""
    medical_coding_context_provided: NotRequired[
        "capo_connecthealth.types.non_null_boolean.NonNullBoolean"
    ]
    """<p>Indicates whether medical coding context was provided.</p>"""
    stream_status: NotRequired[
        "capo_connecthealth.types.medical_scribe_stream_status.MedicalScribeStreamStatus"
    ]
    """<p>The current status of the stream</p>"""
    stream_creation_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the stream was created</p>"""
    stream_end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the stream ended</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeListeningSessionDetails) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    if "language_code" in value:
        import capo_connecthealth.types.medical_scribe_language_code

        out["languageCode"] = (
            capo_connecthealth.types.medical_scribe_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "media_sample_rate_hertz" in value:
        out["mediaSampleRateHertz"] = value["media_sample_rate_hertz"]
    if "media_encoding" in value:
        import capo_connecthealth.types.medical_scribe_media_encoding

        out["mediaEncoding"] = (
            capo_connecthealth.types.medical_scribe_media_encoding.serialize_json(
                value["media_encoding"]
            )
        )
    if "channel_definitions" in value:
        import capo_connecthealth.types.medical_scribe_channel_definitions

        out["channelDefinitions"] = (
            capo_connecthealth.types.medical_scribe_channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    if "post_stream_action_settings" in value:
        import capo_connecthealth.types.medical_scribe_post_stream_action_settings_response

        out["postStreamActionSettings"] = (
            capo_connecthealth.types.medical_scribe_post_stream_action_settings_response.serialize_json(
                value["post_stream_action_settings"]
            )
        )
    if "post_stream_action_result" in value:
        import capo_connecthealth.types.medical_scribe_post_stream_actions_result

        out["postStreamActionResult"] = (
            capo_connecthealth.types.medical_scribe_post_stream_actions_result.serialize_json(
                value["post_stream_action_result"]
            )
        )
    if "encounter_context_provided" in value:
        out["encounterContextProvided"] = value["encounter_context_provided"]
    if "medical_coding_context_provided" in value:
        out["medicalCodingContextProvided"] = value["medical_coding_context_provided"]
    if "stream_status" in value:
        import capo_connecthealth.types.medical_scribe_stream_status

        out["streamStatus"] = (
            capo_connecthealth.types.medical_scribe_stream_status.serialize_json(
                value["stream_status"]
            )
        )
    if "stream_creation_time" in value:
        import capo_connecthealth.types._prelude.timestamp

        out["streamCreationTime"] = (
            capo_connecthealth.types._prelude.timestamp.serialize_json(
                value["stream_creation_time"]
            )
        )
    if "stream_end_time" in value:
        import capo_connecthealth.types._prelude.timestamp

        out["streamEndTime"] = (
            capo_connecthealth.types._prelude.timestamp.serialize_json(
                value["stream_end_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeListeningSessionDetails:
    out: MedicalScribeListeningSessionDetails = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("subscriptionId") is not None:
        out["subscription_id"] = data["subscriptionId"]
    if data.get("languageCode") is not None:
        import capo_connecthealth.types.medical_scribe_language_code

        out["language_code"] = (
            capo_connecthealth.types.medical_scribe_language_code.deserialize_json(
                data["languageCode"]
            )
        )
    if data.get("mediaSampleRateHertz") is not None:
        out["media_sample_rate_hertz"] = data["mediaSampleRateHertz"]
    if data.get("mediaEncoding") is not None:
        import capo_connecthealth.types.medical_scribe_media_encoding

        out["media_encoding"] = (
            capo_connecthealth.types.medical_scribe_media_encoding.deserialize_json(
                data["mediaEncoding"]
            )
        )
    if data.get("channelDefinitions") is not None:
        import capo_connecthealth.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            capo_connecthealth.types.medical_scribe_channel_definitions.deserialize_json(
                data["channelDefinitions"]
            )
        )
    if data.get("postStreamActionSettings") is not None:
        import capo_connecthealth.types.medical_scribe_post_stream_action_settings_response

        out["post_stream_action_settings"] = (
            capo_connecthealth.types.medical_scribe_post_stream_action_settings_response.deserialize_json(
                data["postStreamActionSettings"]
            )
        )
    if data.get("postStreamActionResult") is not None:
        import capo_connecthealth.types.medical_scribe_post_stream_actions_result

        out["post_stream_action_result"] = (
            capo_connecthealth.types.medical_scribe_post_stream_actions_result.deserialize_json(
                data["postStreamActionResult"]
            )
        )
    if data.get("encounterContextProvided") is not None:
        out["encounter_context_provided"] = data["encounterContextProvided"]
    if data.get("medicalCodingContextProvided") is not None:
        out["medical_coding_context_provided"] = data["medicalCodingContextProvided"]
    if data.get("streamStatus") is not None:
        import capo_connecthealth.types.medical_scribe_stream_status

        out["stream_status"] = (
            capo_connecthealth.types.medical_scribe_stream_status.deserialize_json(
                data["streamStatus"]
            )
        )
    if data.get("streamCreationTime") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["stream_creation_time"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["streamCreationTime"]
            )
        )
    if data.get("streamEndTime") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["stream_end_time"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["streamEndTime"]
            )
        )
    return out
