"""Generated from Smithy shape ``com.amazonaws.drs#DeleteSourceNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.source_network_id


class DeleteSourceNetworkRequest(TypedDict, closed=True):
    source_network_id: "capo_drs.types.source_network_id.SourceNetworkID"
    """<p>ID of the Source Network to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSourceNetworkRequest) -> dict:
    out: dict = {}
    out["sourceNetworkID"] = value["source_network_id"]
    return out


def deserialize_json(data: dict) -> DeleteSourceNetworkRequest:
    out: DeleteSourceNetworkRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceNetworkID") is not None:
        out["source_network_id"] = data["sourceNetworkID"]
    else:
        out["source_network_id"] = ""
    return out
