"""Generated from Smithy shape ``com.amazonaws.transcribe#SentimentFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.absolute_time_range
    import capo_transcribe.types.boolean
    import capo_transcribe.types.participant_role
    import capo_transcribe.types.relative_time_range
    import capo_transcribe.types.sentiment_value_list


class SentimentFilter(TypedDict, closed=True):
    sentiments: "capo_transcribe.types.sentiment_value_list.SentimentValueList"
    """<p>Specify the sentiments that you want to flag.</p>"""
    absolute_time_range: NotRequired[
        "capo_transcribe.types.absolute_time_range.AbsoluteTimeRange"
    ]
    """<p>Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for the specified sentiments. See for more detail.</p>"""
    relative_time_range: NotRequired[
        "capo_transcribe.types.relative_time_range.RelativeTimeRange"
    ]
    """<p>Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for the specified sentiments. See for more detail.</p>"""
    participant_role: NotRequired[
        "capo_transcribe.types.participant_role.ParticipantRole"
    ]
    """<p>Specify the participant that you want to flag. Omitting this parameter is equivalent to specifying both participants.</p>"""
    negate: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Set to <code>TRUE</code> to flag the sentiments that you didn't include in your request. Set to <code>FALSE</code> to flag the sentiments that you specified in your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SentimentFilter) -> dict:
    out: dict = {}
    import capo_transcribe.types.sentiment_value_list

    out["Sentiments"] = (
        capo_transcribe.types.sentiment_value_list.serialize_aws_json_1_1(
            value["sentiments"]
        )
    )
    if "absolute_time_range" in value:
        import capo_transcribe.types.absolute_time_range

        out["AbsoluteTimeRange"] = (
            capo_transcribe.types.absolute_time_range.serialize_aws_json_1_1(
                value["absolute_time_range"]
            )
        )
    if "relative_time_range" in value:
        import capo_transcribe.types.relative_time_range

        out["RelativeTimeRange"] = (
            capo_transcribe.types.relative_time_range.serialize_aws_json_1_1(
                value["relative_time_range"]
            )
        )
    if "participant_role" in value:
        import capo_transcribe.types.participant_role

        out["ParticipantRole"] = (
            capo_transcribe.types.participant_role.serialize_aws_json_1_1(
                value["participant_role"]
            )
        )
    if "negate" in value:
        out["Negate"] = value["negate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SentimentFilter:
    out: SentimentFilter = {}  # type: ignore[typeddict-item]
    if data.get("Sentiments") is not None:
        import capo_transcribe.types.sentiment_value_list

        out["sentiments"] = (
            capo_transcribe.types.sentiment_value_list.deserialize_aws_json_1_1(
                data["Sentiments"]
            )
        )
    else:
        out["sentiments"] = []
    if data.get("AbsoluteTimeRange") is not None:
        import capo_transcribe.types.absolute_time_range

        out["absolute_time_range"] = (
            capo_transcribe.types.absolute_time_range.deserialize_aws_json_1_1(
                data["AbsoluteTimeRange"]
            )
        )
    if data.get("RelativeTimeRange") is not None:
        import capo_transcribe.types.relative_time_range

        out["relative_time_range"] = (
            capo_transcribe.types.relative_time_range.deserialize_aws_json_1_1(
                data["RelativeTimeRange"]
            )
        )
    if data.get("ParticipantRole") is not None:
        import capo_transcribe.types.participant_role

        out["participant_role"] = (
            capo_transcribe.types.participant_role.deserialize_aws_json_1_1(
                data["ParticipantRole"]
            )
        )
    if data.get("Negate") is not None:
        out["negate"] = data["Negate"]
    return out
