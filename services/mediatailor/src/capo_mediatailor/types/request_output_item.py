"""Generated from Smithy shape ``com.amazonaws.mediatailor#RequestOutputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.dash_playlist_settings
    import capo_mediatailor.types.hls_playlist_settings


class RequestOutputItem(TypedDict, closed=True):
    dash_playlist_settings: NotRequired[
        "capo_mediatailor.types.dash_playlist_settings.DashPlaylistSettings"
    ]
    """<p>DASH manifest configuration parameters.</p>"""
    hls_playlist_settings: NotRequired[
        "capo_mediatailor.types.hls_playlist_settings.HlsPlaylistSettings"
    ]
    """<p>HLS playlist configuration parameters.</p>"""
    manifest_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the manifest for the channel. The name appears in the <code>PlaybackUrl</code>.</p>"""
    source_group: "capo_mediatailor.types.__string.__string"
    """<p>A string used to match which <code>HttpPackageConfiguration</code> is used for each <code>VodSource</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestOutputItem) -> dict:
    out: dict = {}
    if "dash_playlist_settings" in value:
        import capo_mediatailor.types.dash_playlist_settings

        out["DashPlaylistSettings"] = (
            capo_mediatailor.types.dash_playlist_settings.serialize_json(
                value["dash_playlist_settings"]
            )
        )
    if "hls_playlist_settings" in value:
        import capo_mediatailor.types.hls_playlist_settings

        out["HlsPlaylistSettings"] = (
            capo_mediatailor.types.hls_playlist_settings.serialize_json(
                value["hls_playlist_settings"]
            )
        )
    out["ManifestName"] = value["manifest_name"]
    out["SourceGroup"] = value["source_group"]
    return out


def deserialize_json(data: dict) -> RequestOutputItem:
    out: RequestOutputItem = {}  # type: ignore[typeddict-item]
    if data.get("DashPlaylistSettings") is not None:
        import capo_mediatailor.types.dash_playlist_settings

        out["dash_playlist_settings"] = (
            capo_mediatailor.types.dash_playlist_settings.deserialize_json(
                data["DashPlaylistSettings"]
            )
        )
    if data.get("HlsPlaylistSettings") is not None:
        import capo_mediatailor.types.hls_playlist_settings

        out["hls_playlist_settings"] = (
            capo_mediatailor.types.hls_playlist_settings.deserialize_json(
                data["HlsPlaylistSettings"]
            )
        )
    if data.get("ManifestName") is not None:
        out["manifest_name"] = data["ManifestName"]
    else:
        out["manifest_name"] = ""
    if data.get("SourceGroup") is not None:
        out["source_group"] = data["SourceGroup"]
    else:
        out["source_group"] = ""
    return out
