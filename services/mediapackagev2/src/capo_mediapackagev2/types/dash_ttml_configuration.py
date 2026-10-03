"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashTtmlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.dash_ttml_profile


class DashTtmlConfiguration(TypedDict, closed=True):
    ttml_profile: "capo_mediapackagev2.types.dash_ttml_profile.DashTtmlProfile"
    """<p>The profile that MediaPackage uses when signaling subtitles in the manifest. <code>IMSC</code> is the default profile. <code>EBU-TT-D</code> produces subtitles that are compliant with the EBU-TT-D TTML profile. MediaPackage passes through subtitle styles to the manifest. For more information about EBU-TT-D subtitles, see <a href="https://tech.ebu.ch/publications/tech3380">EBU-TT-D Subtitling Distribution Format</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashTtmlConfiguration) -> dict:
    out: dict = {}
    import capo_mediapackagev2.types.dash_ttml_profile

    out["TtmlProfile"] = capo_mediapackagev2.types.dash_ttml_profile.serialize_json(
        value["ttml_profile"]
    )
    return out


def deserialize_json(data: dict) -> DashTtmlConfiguration:
    out: DashTtmlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TtmlProfile") is not None:
        import capo_mediapackagev2.types.dash_ttml_profile

        out["ttml_profile"] = (
            capo_mediapackagev2.types.dash_ttml_profile.deserialize_json(
                data["TtmlProfile"]
            )
        )
    else:
        raise DeserializationError("DashTtmlConfiguration.ttml_profile required")
    return out
