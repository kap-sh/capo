"""Generated from Smithy shape ``com.amazonaws.medialive#HlsWebdavSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max15
    import capo_medialive.types.__integer_min0_max600
    import capo_medialive.types.hls_webdav_http_transfer_mode


class HlsWebdavSettings(TypedDict, closed=True):
    connection_retry_interval: NotRequired[
        "capo_medialive.types.__integer_min0.__integerMin0"
    ]
    """Number of seconds to wait before retrying connection to the CDN if the connection is lost."""
    filecache_duration: NotRequired[
        "capo_medialive.types.__integer_min0_max600.__integerMin0Max600"
    ]
    """Size in seconds of file cache for streaming outputs."""
    http_transfer_mode: NotRequired[
        "capo_medialive.types.hls_webdav_http_transfer_mode.HlsWebdavHttpTransferMode"
    ]
    """Specify whether or not to use chunked transfer encoding to WebDAV."""
    num_retries: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Number of retry attempts that will be made before the Live Event is put into an error state. Applies only if the CDN destination URI begins with "s3" or "mediastore". For other URIs, the value is always 3."""
    restart_delay: NotRequired[
        "capo_medialive.types.__integer_min0_max15.__integerMin0Max15"
    ]
    """If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsWebdavSettings) -> dict:
    out: dict = {}
    if "connection_retry_interval" in value:
        out["connectionRetryInterval"] = value["connection_retry_interval"]
    if "filecache_duration" in value:
        out["filecacheDuration"] = value["filecache_duration"]
    if "http_transfer_mode" in value:
        import capo_medialive.types.hls_webdav_http_transfer_mode

        out["httpTransferMode"] = (
            capo_medialive.types.hls_webdav_http_transfer_mode.serialize_json(
                value["http_transfer_mode"]
            )
        )
    if "num_retries" in value:
        out["numRetries"] = value["num_retries"]
    if "restart_delay" in value:
        out["restartDelay"] = value["restart_delay"]
    return out


def deserialize_json(data: dict) -> HlsWebdavSettings:
    out: HlsWebdavSettings = {}  # type: ignore[typeddict-item]
    if data.get("connectionRetryInterval") is not None:
        out["connection_retry_interval"] = data["connectionRetryInterval"]
    if data.get("filecacheDuration") is not None:
        out["filecache_duration"] = data["filecacheDuration"]
    if data.get("httpTransferMode") is not None:
        import capo_medialive.types.hls_webdav_http_transfer_mode

        out["http_transfer_mode"] = (
            capo_medialive.types.hls_webdav_http_transfer_mode.deserialize_json(
                data["httpTransferMode"]
            )
        )
    if data.get("numRetries") is not None:
        out["num_retries"] = data["numRetries"]
    if data.get("restartDelay") is not None:
        out["restart_delay"] = data["restartDelay"]
    return out
