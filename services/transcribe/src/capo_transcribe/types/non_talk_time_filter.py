"""Generated from Smithy shape ``com.amazonaws.transcribe#NonTalkTimeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.absolute_time_range
    import capo_transcribe.types.boolean
    import capo_transcribe.types.relative_time_range
    import capo_transcribe.types.timestamp_milliseconds


class NonTalkTimeFilter(TypedDict, closed=True):
    threshold: NotRequired[
        "capo_transcribe.types.timestamp_milliseconds.TimestampMilliseconds"
    ]
    """<p>Specify the duration, in milliseconds, of the period of silence that you want to flag. For example, you can flag a silent period that lasts 30,000 milliseconds.</p>"""
    absolute_time_range: NotRequired[
        "capo_transcribe.types.absolute_time_range.AbsoluteTimeRange"
    ]
    """<p>Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for a period of silence. See for more detail.</p>"""
    relative_time_range: NotRequired[
        "capo_transcribe.types.relative_time_range.RelativeTimeRange"
    ]
    """<p>Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for a period of silence. See for more detail.</p>"""
    negate: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Set to <code>TRUE</code> to flag periods of speech. Set to <code>FALSE</code> to flag periods of silence</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NonTalkTimeFilter) -> dict:
    out: dict = {}
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
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
    if "negate" in value:
        out["Negate"] = value["negate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NonTalkTimeFilter:
    out: NonTalkTimeFilter = {}  # type: ignore[typeddict-item]
    if data.get("Threshold") is not None:
        out["threshold"] = data["Threshold"]
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
    if data.get("Negate") is not None:
        out["negate"] = data["Negate"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NonTalkTimeFilter) -> dict:
    out: dict = {}
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
    if "absolute_time_range" in value:
        import capo_transcribe.types.absolute_time_range

        out["AbsoluteTimeRange"] = (
            capo_transcribe.types.absolute_time_range.serialize_cbor(
                value["absolute_time_range"]
            )
        )
    if "relative_time_range" in value:
        import capo_transcribe.types.relative_time_range

        out["RelativeTimeRange"] = (
            capo_transcribe.types.relative_time_range.serialize_cbor(
                value["relative_time_range"]
            )
        )
    if "negate" in value:
        out["Negate"] = value["negate"]
    return out


def deserialize_cbor(data: dict) -> NonTalkTimeFilter:
    out: NonTalkTimeFilter = {}  # type: ignore[typeddict-item]
    if data.get("Threshold") is not None:
        out["threshold"] = data["Threshold"]
    if data.get("AbsoluteTimeRange") is not None:
        import capo_transcribe.types.absolute_time_range

        out["absolute_time_range"] = (
            capo_transcribe.types.absolute_time_range.deserialize_cbor(
                data["AbsoluteTimeRange"]
            )
        )
    if data.get("RelativeTimeRange") is not None:
        import capo_transcribe.types.relative_time_range

        out["relative_time_range"] = (
            capo_transcribe.types.relative_time_range.deserialize_cbor(
                data["RelativeTimeRange"]
            )
        )
    if data.get("Negate") is not None:
        out["negate"] = data["Negate"]
    return out
