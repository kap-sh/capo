"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.absolute_time_range
    import capo_transcribe.types.boolean
    import capo_transcribe.types.participant_role
    import capo_transcribe.types.relative_time_range
    import capo_transcribe.types.string_target_list
    import capo_transcribe.types.transcript_filter_type


class TranscriptFilter(TypedDict, closed=True):
    transcript_filter_type: (
        "capo_transcribe.types.transcript_filter_type.TranscriptFilterType"
    )
    """<p>Flag the presence or absence of an exact match to the phrases that you specify. For example, if you specify the phrase "speak to a manager" as your <code>Targets</code> value, only that exact phrase is flagged.</p> <p>Note that semantic matching is not supported. For example, if your customer says "speak to <i>the</i> manager", instead of "speak to <i>a</i> manager", your content is not flagged.</p>"""
    absolute_time_range: NotRequired[
        "capo_transcribe.types.absolute_time_range.AbsoluteTimeRange"
    ]
    """<p>Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for the specified key words or phrases. See for more detail.</p>"""
    relative_time_range: NotRequired[
        "capo_transcribe.types.relative_time_range.RelativeTimeRange"
    ]
    """<p>Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for the specified key words or phrases. See for more detail.</p>"""
    participant_role: NotRequired[
        "capo_transcribe.types.participant_role.ParticipantRole"
    ]
    """<p>Specify the participant that you want to flag. Omitting this parameter is equivalent to specifying both participants.</p>"""
    negate: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Set to <code>TRUE</code> to flag the absence of the phrase that you specified in your request. Set to <code>FALSE</code> to flag the presence of the phrase that you specified in your request.</p>"""
    targets: "capo_transcribe.types.string_target_list.StringTargetList"
    """<p>Specify the phrases that you want to flag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranscriptFilter) -> dict:
    out: dict = {}
    import capo_transcribe.types.transcript_filter_type

    out["TranscriptFilterType"] = (
        capo_transcribe.types.transcript_filter_type.serialize_aws_json_1_1(
            value["transcript_filter_type"]
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
    import capo_transcribe.types.string_target_list

    out["Targets"] = capo_transcribe.types.string_target_list.serialize_aws_json_1_1(
        value["targets"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranscriptFilter:
    out: TranscriptFilter = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptFilterType") is not None:
        import capo_transcribe.types.transcript_filter_type

        out["transcript_filter_type"] = (
            capo_transcribe.types.transcript_filter_type.deserialize_aws_json_1_1(
                data["TranscriptFilterType"]
            )
        )
    else:
        raise DeserializationError("TranscriptFilter.transcript_filter_type required")
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
    if data.get("Targets") is not None:
        import capo_transcribe.types.string_target_list

        out["targets"] = (
            capo_transcribe.types.string_target_list.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    else:
        raise DeserializationError("TranscriptFilter.targets required")
    return out
