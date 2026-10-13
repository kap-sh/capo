"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamKeyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.stream_key


class GetStreamKeyResponse(TypedDict, closed=True):
    stream_key: NotRequired["capo_ivs.types.stream_key.StreamKey"]


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamKeyResponse) -> dict:
    out: dict = {}
    if "stream_key" in value:
        import capo_ivs.types.stream_key

        out["streamKey"] = capo_ivs.types.stream_key.serialize_json(value["stream_key"])
    return out


def deserialize_json(data: dict) -> GetStreamKeyResponse:
    out: GetStreamKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("streamKey") is not None:
        import capo_ivs.types.stream_key

        out["stream_key"] = capo_ivs.types.stream_key.deserialize_json(
            data["streamKey"]
        )
    return out


def redact_sensitive(value: GetStreamKeyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stream_key" in value:
        import capo_ivs.types.stream_key

        out["stream_key"] = capo_ivs.types.stream_key.redact_sensitive(
            value["stream_key"]
        )
    return out
