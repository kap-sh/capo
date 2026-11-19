"""Generated from Smithy shape ``com.amazonaws.transcribe#Subtitles``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.subtitle_formats
    import capo_transcribe.types.subtitle_output_start_index


class Subtitles(TypedDict, closed=True):
    formats: NotRequired["capo_transcribe.types.subtitle_formats.SubtitleFormats"]
    """<p>Specify the output format for your subtitle file; if you select both WebVTT (<code>vtt</code>) and SubRip (<code>srt</code>) formats, two output files are generated.</p>"""
    output_start_index: NotRequired[
        "capo_transcribe.types.subtitle_output_start_index.SubtitleOutputStartIndex"
    ]
    """<p>Specify the starting value that is assigned to the first subtitle segment.</p> <p>The default start index for Amazon Transcribe is <code>0</code>, which differs from the more widely used standard of <code>1</code>. If you're uncertain which value to use, we recommend choosing <code>1</code>, as this may improve compatibility with other services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subtitles) -> dict:
    out: dict = {}
    if "formats" in value:
        import capo_transcribe.types.subtitle_formats

        out["Formats"] = capo_transcribe.types.subtitle_formats.serialize_aws_json_1_1(
            value["formats"]
        )
    if "output_start_index" in value:
        out["OutputStartIndex"] = value["output_start_index"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Subtitles:
    out: Subtitles = {}  # type: ignore[typeddict-item]
    if data.get("Formats") is not None:
        import capo_transcribe.types.subtitle_formats

        out["formats"] = (
            capo_transcribe.types.subtitle_formats.deserialize_aws_json_1_1(
                data["Formats"]
            )
        )
    if data.get("OutputStartIndex") is not None:
        out["output_start_index"] = data["OutputStartIndex"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Subtitles) -> dict:
    out: dict = {}
    if "formats" in value:
        import capo_transcribe.types.subtitle_formats

        out["Formats"] = capo_transcribe.types.subtitle_formats.serialize_cbor(
            value["formats"]
        )
    if "output_start_index" in value:
        out["OutputStartIndex"] = value["output_start_index"]
    return out


def deserialize_cbor(data: dict) -> Subtitles:
    out: Subtitles = {}  # type: ignore[typeddict-item]
    if data.get("Formats") is not None:
        import capo_transcribe.types.subtitle_formats

        out["formats"] = capo_transcribe.types.subtitle_formats.deserialize_cbor(
            data["Formats"]
        )
    if data.get("OutputStartIndex") is not None:
        out["output_start_index"] = data["OutputStartIndex"]
    return out
