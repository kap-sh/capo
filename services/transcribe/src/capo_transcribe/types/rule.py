"""Generated from Smithy shape ``com.amazonaws.transcribe#Rule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transcribe.errors import DeserializationError, SerializationError
from capo_transcribe.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_transcribe.types.interruption_filter
    import capo_transcribe.types.non_talk_time_filter
    import capo_transcribe.types.sentiment_filter
    import capo_transcribe.types.transcript_filter


class RuleNonTalkTimeFilterMember(TypedDict, closed=True):
    NonTalkTimeFilter: "capo_transcribe.types.non_talk_time_filter.NonTalkTimeFilter"


class RuleInterruptionFilterMember(TypedDict, closed=True):
    InterruptionFilter: "capo_transcribe.types.interruption_filter.InterruptionFilter"


class RuleTranscriptFilterMember(TypedDict, closed=True):
    TranscriptFilter: "capo_transcribe.types.transcript_filter.TranscriptFilter"


class RuleSentimentFilterMember(TypedDict, closed=True):
    SentimentFilter: "capo_transcribe.types.sentiment_filter.SentimentFilter"


Rule: TypeAlias = (
    RuleNonTalkTimeFilterMember
    | RuleInterruptionFilterMember
    | RuleTranscriptFilterMember
    | RuleSentimentFilterMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Rule: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "NonTalkTimeFilter" in value:
        import capo_transcribe.types.non_talk_time_filter

        return {
            "NonTalkTimeFilter": capo_transcribe.types.non_talk_time_filter.serialize_aws_json_1_1(
                value["NonTalkTimeFilter"]
            )
        }
    elif "InterruptionFilter" in value:
        import capo_transcribe.types.interruption_filter

        return {
            "InterruptionFilter": capo_transcribe.types.interruption_filter.serialize_aws_json_1_1(
                value["InterruptionFilter"]
            )
        }
    elif "TranscriptFilter" in value:
        import capo_transcribe.types.transcript_filter

        return {
            "TranscriptFilter": capo_transcribe.types.transcript_filter.serialize_aws_json_1_1(
                value["TranscriptFilter"]
            )
        }
    elif "SentimentFilter" in value:
        import capo_transcribe.types.sentiment_filter

        return {
            "SentimentFilter": capo_transcribe.types.sentiment_filter.serialize_aws_json_1_1(
                value["SentimentFilter"]
            )
        }
    else:
        raise SerializationError("Rule: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Rule:
    if data.get("NonTalkTimeFilter") is not None:
        import capo_transcribe.types.non_talk_time_filter

        return {
            "NonTalkTimeFilter": capo_transcribe.types.non_talk_time_filter.deserialize_aws_json_1_1(
                data["NonTalkTimeFilter"]
            )
        }
    elif data.get("InterruptionFilter") is not None:
        import capo_transcribe.types.interruption_filter

        return {
            "InterruptionFilter": capo_transcribe.types.interruption_filter.deserialize_aws_json_1_1(
                data["InterruptionFilter"]
            )
        }
    elif data.get("TranscriptFilter") is not None:
        import capo_transcribe.types.transcript_filter

        return {
            "TranscriptFilter": capo_transcribe.types.transcript_filter.deserialize_aws_json_1_1(
                data["TranscriptFilter"]
            )
        }
    elif data.get("SentimentFilter") is not None:
        import capo_transcribe.types.sentiment_filter

        return {
            "SentimentFilter": capo_transcribe.types.sentiment_filter.deserialize_aws_json_1_1(
                data["SentimentFilter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Rule: no recognized variant key")
