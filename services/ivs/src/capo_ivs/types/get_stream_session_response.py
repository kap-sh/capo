"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamSessionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.stream_session


class GetStreamSessionResponse(TypedDict, closed=True):
    stream_session: NotRequired["capo_ivs.types.stream_session.StreamSession"]
    """<p>List of stream details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamSessionResponse) -> dict:
    out: dict = {}
    if "stream_session" in value:
        import capo_ivs.types.stream_session

        out["streamSession"] = capo_ivs.types.stream_session.serialize_json(
            value["stream_session"]
        )
    return out


def deserialize_json(data: dict) -> GetStreamSessionResponse:
    out: GetStreamSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("streamSession") is not None:
        import capo_ivs.types.stream_session

        out["stream_session"] = capo_ivs.types.stream_session.deserialize_json(
            data["streamSession"]
        )
    return out


def redact_sensitive(value: GetStreamSessionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "stream_session" in value:
        import capo_ivs.types.stream_session

        out["stream_session"] = capo_ivs.types.stream_session.redact_sensitive(
            value["stream_session"]
        )
    return out
