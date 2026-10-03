"""Generated from Smithy shape ``com.amazonaws.medialive#HlsMediaStoreSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max15
    import capo_medialive.types.__integer_min0_max600
    import capo_medialive.types.hls_media_store_storage_class


class HlsMediaStoreSettings(TypedDict, closed=True):
    connection_retry_interval: NotRequired[
        "capo_medialive.types.__integer_min0.__integerMin0"
    ]
    """Number of seconds to wait before retrying connection to the CDN if the connection is lost."""
    filecache_duration: NotRequired[
        "capo_medialive.types.__integer_min0_max600.__integerMin0Max600"
    ]
    """Size in seconds of file cache for streaming outputs."""
    media_store_storage_class: NotRequired[
        "capo_medialive.types.hls_media_store_storage_class.HlsMediaStoreStorageClass"
    ]
    """When set to temporal, output files are stored in non-persistent memory for faster reading and writing."""
    num_retries: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Number of retry attempts that will be made before the Live Event is put into an error state. Applies only if the CDN destination URI begins with "s3" or "mediastore". For other URIs, the value is always 3."""
    restart_delay: NotRequired[
        "capo_medialive.types.__integer_min0_max15.__integerMin0Max15"
    ]
    """If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsMediaStoreSettings) -> dict:
    out: dict = {}
    if "connection_retry_interval" in value:
        out["connectionRetryInterval"] = value["connection_retry_interval"]
    if "filecache_duration" in value:
        out["filecacheDuration"] = value["filecache_duration"]
    if "media_store_storage_class" in value:
        import capo_medialive.types.hls_media_store_storage_class

        out["mediaStoreStorageClass"] = (
            capo_medialive.types.hls_media_store_storage_class.serialize_json(
                value["media_store_storage_class"]
            )
        )
    if "num_retries" in value:
        out["numRetries"] = value["num_retries"]
    if "restart_delay" in value:
        out["restartDelay"] = value["restart_delay"]
    return out


def deserialize_json(data: dict) -> HlsMediaStoreSettings:
    out: HlsMediaStoreSettings = {}  # type: ignore[typeddict-item]
    if data.get("connectionRetryInterval") is not None:
        out["connection_retry_interval"] = data["connectionRetryInterval"]
    if data.get("filecacheDuration") is not None:
        out["filecache_duration"] = data["filecacheDuration"]
    if data.get("mediaStoreStorageClass") is not None:
        import capo_medialive.types.hls_media_store_storage_class

        out["media_store_storage_class"] = (
            capo_medialive.types.hls_media_store_storage_class.deserialize_json(
                data["mediaStoreStorageClass"]
            )
        )
    if data.get("numRetries") is not None:
        out["num_retries"] = data["numRetries"]
    if data.get("restartDelay") is not None:
        out["restart_delay"] = data["restartDelay"]
    return out
