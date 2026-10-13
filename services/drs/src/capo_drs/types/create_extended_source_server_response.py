"""Generated from Smithy shape ``com.amazonaws.drs#CreateExtendedSourceServerResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.source_server


class CreateExtendedSourceServerResponse(TypedDict, closed=True):
    source_server: NotRequired["capo_drs.types.source_server.SourceServer"]
    """<p>Created extended source server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExtendedSourceServerResponse) -> dict:
    out: dict = {}
    if "source_server" in value:
        import capo_drs.types.source_server

        out["sourceServer"] = capo_drs.types.source_server.serialize_json(
            value["source_server"]
        )
    return out


def deserialize_json(data: dict) -> CreateExtendedSourceServerResponse:
    out: CreateExtendedSourceServerResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceServer") is not None:
        import capo_drs.types.source_server

        out["source_server"] = capo_drs.types.source_server.deserialize_json(
            data["sourceServer"]
        )
    return out


def redact_sensitive(value: CreateExtendedSourceServerResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_server" in value:
        import capo_drs.types.source_server

        out["source_server"] = capo_drs.types.source_server.redact_sensitive(
            value["source_server"]
        )
    return out
