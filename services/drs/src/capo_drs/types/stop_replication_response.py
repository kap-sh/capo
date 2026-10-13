"""Generated from Smithy shape ``com.amazonaws.drs#StopReplicationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.source_server


class StopReplicationResponse(TypedDict, closed=True):
    source_server: NotRequired["capo_drs.types.source_server.SourceServer"]
    """<p>The Source Server that this action was targeted on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopReplicationResponse) -> dict:
    out: dict = {}
    if "source_server" in value:
        import capo_drs.types.source_server

        out["sourceServer"] = capo_drs.types.source_server.serialize_json(
            value["source_server"]
        )
    return out


def deserialize_json(data: dict) -> StopReplicationResponse:
    out: StopReplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceServer") is not None:
        import capo_drs.types.source_server

        out["source_server"] = capo_drs.types.source_server.deserialize_json(
            data["sourceServer"]
        )
    return out


def redact_sensitive(value: StopReplicationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_server" in value:
        import capo_drs.types.source_server

        out["source_server"] = capo_drs.types.source_server.redact_sensitive(
            value["source_server"]
        )
    return out
