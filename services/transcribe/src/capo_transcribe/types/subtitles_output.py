"""Generated from Smithy shape ``com.amazonaws.transcribe#SubtitlesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.subtitle_file_uris
    import capo_transcribe.types.subtitle_formats
    import capo_transcribe.types.subtitle_output_start_index


class SubtitlesOutput(TypedDict, closed=True):
    formats: NotRequired["capo_transcribe.types.subtitle_formats.SubtitleFormats"]
    """<p>Provides the format of your subtitle files. If your request included both WebVTT (<code>vtt</code>) and SubRip (<code>srt</code>) formats, both formats are shown.</p>"""
    subtitle_file_uris: NotRequired[
        "capo_transcribe.types.subtitle_file_uris.SubtitleFileUris"
    ]
    """<p>The Amazon S3 location of your transcript. You can use this URI to access or download your subtitle file. Your subtitle file is stored in the same location as your transcript. If you specified both WebVTT and SubRip subtitle formats, two URIs are provided.</p> <p>If you included <code>OutputBucketName</code> in your transcription job request, this is the URI of that bucket. If you also included <code>OutputKey</code> in your request, your output is located in the path you specified in your request.</p> <p>If you didn't include <code>OutputBucketName</code> in your transcription job request, your subtitle file is stored in a service-managed bucket, and <code>TranscriptFileUri</code> provides you with a temporary URI you can use for secure access to your subtitle file.</p> <note> <p>Temporary URIs for service-managed Amazon S3 buckets are only valid for 15 minutes. If you get an <code>AccesDenied</code> error, you can get a new temporary URI by running a <code>GetTranscriptionJob</code> or <code>ListTranscriptionJob</code> request.</p> </note>"""
    output_start_index: NotRequired[
        "capo_transcribe.types.subtitle_output_start_index.SubtitleOutputStartIndex"
    ]
    """<p>Provides the start index value for your subtitle files. If you did not specify a value in your request, the default value of <code>0</code> is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubtitlesOutput) -> dict:
    out: dict = {}
    if "formats" in value:
        import capo_transcribe.types.subtitle_formats

        out["Formats"] = capo_transcribe.types.subtitle_formats.serialize_aws_json_1_1(
            value["formats"]
        )
    if "subtitle_file_uris" in value:
        import capo_transcribe.types.subtitle_file_uris

        out["SubtitleFileUris"] = (
            capo_transcribe.types.subtitle_file_uris.serialize_aws_json_1_1(
                value["subtitle_file_uris"]
            )
        )
    if "output_start_index" in value:
        out["OutputStartIndex"] = value["output_start_index"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubtitlesOutput:
    out: SubtitlesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Formats") is not None:
        import capo_transcribe.types.subtitle_formats

        out["formats"] = (
            capo_transcribe.types.subtitle_formats.deserialize_aws_json_1_1(
                data["Formats"]
            )
        )
    if data.get("SubtitleFileUris") is not None:
        import capo_transcribe.types.subtitle_file_uris

        out["subtitle_file_uris"] = (
            capo_transcribe.types.subtitle_file_uris.deserialize_aws_json_1_1(
                data["SubtitleFileUris"]
            )
        )
    if data.get("OutputStartIndex") is not None:
        out["output_start_index"] = data["OutputStartIndex"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubtitlesOutput) -> dict:
    out: dict = {}
    if "formats" in value:
        import capo_transcribe.types.subtitle_formats

        out["Formats"] = capo_transcribe.types.subtitle_formats.serialize_cbor(
            value["formats"]
        )
    if "subtitle_file_uris" in value:
        import capo_transcribe.types.subtitle_file_uris

        out["SubtitleFileUris"] = (
            capo_transcribe.types.subtitle_file_uris.serialize_cbor(
                value["subtitle_file_uris"]
            )
        )
    if "output_start_index" in value:
        out["OutputStartIndex"] = value["output_start_index"]
    return out


def deserialize_cbor(data: dict) -> SubtitlesOutput:
    out: SubtitlesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Formats") is not None:
        import capo_transcribe.types.subtitle_formats

        out["formats"] = capo_transcribe.types.subtitle_formats.deserialize_cbor(
            data["Formats"]
        )
    if data.get("SubtitleFileUris") is not None:
        import capo_transcribe.types.subtitle_file_uris

        out["subtitle_file_uris"] = (
            capo_transcribe.types.subtitle_file_uris.deserialize_cbor(
                data["SubtitleFileUris"]
            )
        )
    if data.get("OutputStartIndex") is not None:
        out["output_start_index"] = data["OutputStartIndex"]
    return out
