"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CaptionFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.caption_format_format
    import capo_elastic_transcoder.types.caption_format_pattern
    import capo_elastic_transcoder.types.encryption


class CaptionFormat(TypedDict, closed=True):
    format: NotRequired[
        "capo_elastic_transcoder.types.caption_format_format.CaptionFormatFormat"
    ]
    """<p>The format you specify determines whether Elastic Transcoder generates an embedded or sidecar caption for this output.</p> <ul> <li> <p> <b>Valid Embedded Caption Formats:</b> </p> <ul> <li> <p> <b>for FLAC</b>: None</p> </li> <li> <p> <b>For MP3</b>: None</p> </li> <li> <p> <b>For MP4</b>: mov-text</p> </li> <li> <p> <b>For MPEG-TS</b>: None</p> </li> <li> <p> <b>For ogg</b>: None</p> </li> <li> <p> <b>For webm</b>: None</p> </li> </ul> </li> <li> <p> <b>Valid Sidecar Caption Formats:</b> Elastic Transcoder supports dfxp (first div element only), scc, srt, and webvtt. If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.</p> <ul> <li> <p> <b>For FMP4</b>: dfxp</p> </li> <li> <p> <b>Non-FMP4 outputs</b>: All sidecar types</p> </li> </ul> <p> <code>fmp4</code> captions have an extension of <code>.ismt</code> </p> </li> </ul>"""
    pattern: NotRequired[
        "capo_elastic_transcoder.types.caption_format_pattern.CaptionFormatPattern"
    ]
    """<p>The prefix for caption filenames, in the form <i>description</i>-<code>{language}</code>, where:</p> <ul> <li> <p> <i>description</i> is a description of the video.</p> </li> <li> <p> <code>{language}</code> is a literal value that Elastic Transcoder replaces with the two- or three-letter code for the language of the caption in the output file names.</p> </li> </ul> <p>If you don't include <code>{language}</code> in the file name pattern, Elastic Transcoder automatically appends "<code>{language}</code>" to the value that you specify for the description. In addition, Elastic Transcoder automatically appends the count to the end of the segment files.</p> <p>For example, suppose you're transcoding into srt format. When you enter "Sydney-{language}-sunrise", and the language of the captions is English (en), the name of the first caption file is be Sydney-en-sunrise00000.srt.</p>"""
    encryption: NotRequired["capo_elastic_transcoder.types.encryption.Encryption"]
    """<p>The encryption settings, if any, that you want Elastic Transcoder to apply to your caption formats.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionFormat) -> dict:
    out: dict = {}
    if "format" in value:
        out["Format"] = value["format"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    if "encryption" in value:
        import capo_elastic_transcoder.types.encryption

        out["Encryption"] = capo_elastic_transcoder.types.encryption.serialize_json(
            value["encryption"]
        )
    return out


def deserialize_json(data: dict) -> CaptionFormat:
    out: CaptionFormat = {}  # type: ignore[typeddict-item]
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("Encryption") is not None:
        import capo_elastic_transcoder.types.encryption

        out["encryption"] = capo_elastic_transcoder.types.encryption.deserialize_json(
            data["Encryption"]
        )
    return out
