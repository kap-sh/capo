"""Generated from Smithy shape ``com.amazonaws.drs#GetReplicationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.source_server_id


class GetReplicationConfigurationRequest(TypedDict, closed=True):
    source_server_id: "capo_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Serve for this Replication Configuration.r</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReplicationConfigurationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    return out


def deserialize_json(data: dict) -> GetReplicationConfigurationRequest:
    out: GetReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    return out
