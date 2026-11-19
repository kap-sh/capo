"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SetRtmpPushSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_push_naming_configuration


class SetRtmpPushSourceSettings(TypedDict, closed=True):
    naming_configuration: NotRequired[
        "capo_mediaconnect.types.rtmp_push_naming_configuration.RtmpPushNamingConfiguration"
    ]
    """<p>The configuration settings for the application and stream names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetRtmpPushSourceSettings) -> dict:
    out: dict = {}
    if "naming_configuration" in value:
        import capo_mediaconnect.types.rtmp_push_naming_configuration

        out["namingConfiguration"] = (
            capo_mediaconnect.types.rtmp_push_naming_configuration.serialize_json(
                value["naming_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SetRtmpPushSourceSettings:
    out: SetRtmpPushSourceSettings = {}  # type: ignore[typeddict-item]
    if data.get("namingConfiguration") is not None:
        import capo_mediaconnect.types.rtmp_push_naming_configuration

        out["naming_configuration"] = (
            capo_mediaconnect.types.rtmp_push_naming_configuration.deserialize_json(
                data["namingConfiguration"]
            )
        )
    return out
