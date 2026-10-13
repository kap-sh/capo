"""Generated from Smithy shape ``com.amazonaws.drs#StopSourceNetworkReplicationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.source_network


class StopSourceNetworkReplicationResponse(TypedDict, closed=True):
    source_network: NotRequired["capo_drs.types.source_network.SourceNetwork"]
    """<p>Source Network which was requested to stop replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopSourceNetworkReplicationResponse) -> dict:
    out: dict = {}
    if "source_network" in value:
        import capo_drs.types.source_network

        out["sourceNetwork"] = capo_drs.types.source_network.serialize_json(
            value["source_network"]
        )
    return out


def deserialize_json(data: dict) -> StopSourceNetworkReplicationResponse:
    out: StopSourceNetworkReplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceNetwork") is not None:
        import capo_drs.types.source_network

        out["source_network"] = capo_drs.types.source_network.deserialize_json(
            data["sourceNetwork"]
        )
    return out


def redact_sensitive(value: StopSourceNetworkReplicationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_network" in value:
        import capo_drs.types.source_network

        out["source_network"] = capo_drs.types.source_network.redact_sensitive(
            value["source_network"]
        )
    return out
