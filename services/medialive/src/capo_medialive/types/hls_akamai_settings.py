"""Generated from Smithy shape ``com.amazonaws.medialive#HlsAkamaiSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max15
    import capo_medialive.types.__integer_min0_max600
    import capo_medialive.types.__string
    import capo_medialive.types.hls_akamai_http_transfer_mode


class HlsAkamaiSettings(TypedDict, closed=True):
    connection_retry_interval: NotRequired[
        "capo_medialive.types.__integer_min0.__integerMin0"
    ]
    """Number of seconds to wait before retrying connection to the CDN if the connection is lost."""
    filecache_duration: NotRequired[
        "capo_medialive.types.__integer_min0_max600.__integerMin0Max600"
    ]
    """Size in seconds of file cache for streaming outputs."""
    http_transfer_mode: NotRequired[
        "capo_medialive.types.hls_akamai_http_transfer_mode.HlsAkamaiHttpTransferMode"
    ]
    """Specify whether or not to use chunked transfer encoding to Akamai. User should contact Akamai to enable this feature."""
    num_retries: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """Number of retry attempts that will be made before the Live Event is put into an error state. Applies only if the CDN destination URI begins with "s3" or "mediastore". For other URIs, the value is always 3."""
    restart_delay: NotRequired[
        "capo_medialive.types.__integer_min0_max15.__integerMin0Max15"
    ]
    """If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart."""
    salt: NotRequired["capo_medialive.types.__string.__string"]
    """Salt for authenticated Akamai."""
    token: NotRequired["capo_medialive.types.__string.__string"]
    """Token parameter for authenticated akamai. If not specified, _gda_ is used."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsAkamaiSettings) -> dict:
    out: dict = {}
    if "connection_retry_interval" in value:
        out["connectionRetryInterval"] = value["connection_retry_interval"]
    if "filecache_duration" in value:
        out["filecacheDuration"] = value["filecache_duration"]
    if "http_transfer_mode" in value:
        import capo_medialive.types.hls_akamai_http_transfer_mode

        out["httpTransferMode"] = (
            capo_medialive.types.hls_akamai_http_transfer_mode.serialize_json(
                value["http_transfer_mode"]
            )
        )
    if "num_retries" in value:
        out["numRetries"] = value["num_retries"]
    if "restart_delay" in value:
        out["restartDelay"] = value["restart_delay"]
    if "salt" in value:
        out["salt"] = value["salt"]
    if "token" in value:
        out["token"] = value["token"]
    return out


def deserialize_json(data: dict) -> HlsAkamaiSettings:
    out: HlsAkamaiSettings = {}  # type: ignore[typeddict-item]
    if data.get("connectionRetryInterval") is not None:
        out["connection_retry_interval"] = data["connectionRetryInterval"]
    if data.get("filecacheDuration") is not None:
        out["filecache_duration"] = data["filecacheDuration"]
    if data.get("httpTransferMode") is not None:
        import capo_medialive.types.hls_akamai_http_transfer_mode

        out["http_transfer_mode"] = (
            capo_medialive.types.hls_akamai_http_transfer_mode.deserialize_json(
                data["httpTransferMode"]
            )
        )
    if data.get("numRetries") is not None:
        out["num_retries"] = data["numRetries"]
    if data.get("restartDelay") is not None:
        out["restart_delay"] = data["restartDelay"]
    if data.get("salt") is not None:
        out["salt"] = data["salt"]
    if data.get("token") is not None:
        out["token"] = data["token"]
    return out
