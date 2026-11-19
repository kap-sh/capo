"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_source_metadata_info
    import capo_mediaconnect.types.transport_media_info


class RouterInputMetadataTransportStreamMediaInfoMember(TypedDict, closed=True):
    TransportStreamMediaInfo: (
        "capo_mediaconnect.types.transport_media_info.TransportMediaInfo"
    )


class RouterInputMetadataRtmpInfoMember(TypedDict, closed=True):
    RtmpInfo: "capo_mediaconnect.types.rtmp_source_metadata_info.RtmpSourceMetadataInfo"


RouterInputMetadata: TypeAlias = (
    RouterInputMetadataTransportStreamMediaInfoMember
    | RouterInputMetadataRtmpInfoMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouterInputMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "TransportStreamMediaInfo" in value:
        import capo_mediaconnect.types.transport_media_info

        return {
            "transportStreamMediaInfo": capo_mediaconnect.types.transport_media_info.serialize_json(
                value["TransportStreamMediaInfo"]
            )
        }
    elif "RtmpInfo" in value:
        import capo_mediaconnect.types.rtmp_source_metadata_info

        return {
            "rtmpInfo": capo_mediaconnect.types.rtmp_source_metadata_info.serialize_json(
                value["RtmpInfo"]
            )
        }
    else:
        raise SerializationError("RouterInputMetadata: no variant present")


def deserialize_json(data: dict) -> RouterInputMetadata:
    if data.get("transportStreamMediaInfo") is not None:
        import capo_mediaconnect.types.transport_media_info

        return {
            "TransportStreamMediaInfo": capo_mediaconnect.types.transport_media_info.deserialize_json(
                data["transportStreamMediaInfo"]
            )
        }
    elif data.get("rtmpInfo") is not None:
        import capo_mediaconnect.types.rtmp_source_metadata_info

        return {
            "RtmpInfo": capo_mediaconnect.types.rtmp_source_metadata_info.deserialize_json(
                data["rtmpInfo"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RouterInputMetadata: no recognized variant key")
