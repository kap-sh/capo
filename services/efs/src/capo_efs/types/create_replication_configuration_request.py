"""Generated from Smithy shape ``com.amazonaws.efs#CreateReplicationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.destinations_to_create
    import capo_efs.types.file_system_id


class CreateReplicationConfigurationRequest(TypedDict, closed=True):
    source_file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>Specifies the Amazon EFS file system that you want to replicate. This file system cannot already be a source or destination file system in another replication configuration.</p>"""
    destinations: "capo_efs.types.destinations_to_create.DestinationsToCreate"
    """<p>An array of destination configuration objects. Only one destination configuration object is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReplicationConfigurationRequest) -> dict:
    out: dict = {}
    import capo_efs.types.destinations_to_create

    out["Destinations"] = capo_efs.types.destinations_to_create.serialize_json(
        value["destinations"]
    )
    return out


def deserialize_json(data: dict) -> CreateReplicationConfigurationRequest:
    out: CreateReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Destinations") is not None:
        import capo_efs.types.destinations_to_create

        out["destinations"] = capo_efs.types.destinations_to_create.deserialize_json(
            data["Destinations"]
        )
    else:
        out["destinations"] = []
    return out
