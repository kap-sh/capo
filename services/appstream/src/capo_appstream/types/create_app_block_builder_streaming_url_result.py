"""Generated from Smithy shape ``com.amazonaws.appstream#CreateAppBlockBuilderStreamingURLResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.streaming_url
    import capo_appstream.types.timestamp


class CreateAppBlockBuilderStreamingURLResult(TypedDict, closed=True):
    streaming_url: NotRequired["capo_appstream.types.streaming_url.StreamingUrl"]
    """<p>The URL to start the streaming session.</p>"""
    expires: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The elapsed time, in seconds after the Unix epoch, when this URL expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppBlockBuilderStreamingURLResult) -> dict:
    out: dict = {}
    if "streaming_url" in value:
        out["StreamingURL"] = value["streaming_url"]
    if "expires" in value:
        import capo_appstream.types.timestamp

        out["Expires"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["expires"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppBlockBuilderStreamingURLResult:
    out: CreateAppBlockBuilderStreamingURLResult = {}  # type: ignore[typeddict-item]
    if data.get("StreamingURL") is not None:
        out["streaming_url"] = data["StreamingURL"]
    if data.get("Expires") is not None:
        import capo_appstream.types.timestamp

        out["expires"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["Expires"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAppBlockBuilderStreamingURLResult) -> dict:
    out: dict = {}
    if "streaming_url" in value:
        out["StreamingURL"] = value["streaming_url"]
    if "expires" in value:
        import capo_appstream.types.timestamp

        out["Expires"] = capo_appstream.types.timestamp.serialize_cbor(value["expires"])
    return out


def deserialize_cbor(data: dict) -> CreateAppBlockBuilderStreamingURLResult:
    out: CreateAppBlockBuilderStreamingURLResult = {}  # type: ignore[typeddict-item]
    if data.get("StreamingURL") is not None:
        out["streaming_url"] = data["StreamingURL"]
    if data.get("Expires") is not None:
        import capo_appstream.types.timestamp

        out["expires"] = capo_appstream.types.timestamp.deserialize_cbor(
            data["Expires"]
        )
    return out


def redact_sensitive(value: CreateAppBlockBuilderStreamingURLResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "streaming_url" in value:
        out["streaming_url"] = "*** Sensitive Data Redacted ***"
    return out
