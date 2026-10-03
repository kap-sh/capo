"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashDvbFontDownload``."""

from typing_extensions import NotRequired, TypedDict


class DashDvbFontDownload(TypedDict, closed=True):
    url: NotRequired["str"]
    """<p>The URL for downloading fonts for subtitles.</p>"""
    mime_type: NotRequired["str"]
    """<p>The <code>mimeType</code> of the resource that's at the font download URL.</p> <p>For information about font MIME types, see the <a href="https://dvb.org/wp-content/uploads/2021/06/A168r4_MPEG-DASH-Profile-for-Transport-of-ISO-BMFF-Based-DVB-Services_Draft-ts_103-285-v140_November_2021.pdf">MPEG-DASH Profile for Transport of ISO BMFF Based DVB Services over IP Based Networks</a> document. </p>"""
    font_family: NotRequired["str"]
    """<p>The <code>fontFamily</code> name for subtitles, as described in <a href="https://tech.ebu.ch/publications/tech3380">EBU-TT-D Subtitling Distribution Format</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashDvbFontDownload) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "mime_type" in value:
        out["MimeType"] = value["mime_type"]
    if "font_family" in value:
        out["FontFamily"] = value["font_family"]
    return out


def deserialize_json(data: dict) -> DashDvbFontDownload:
    out: DashDvbFontDownload = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("MimeType") is not None:
        out["mime_type"] = data["MimeType"]
    if data.get("FontFamily") is not None:
        out["font_family"] = data["FontFamily"]
    return out
