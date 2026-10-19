"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#CreateSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_simspaceweaver.types.s3_destination
    import capo_simspaceweaver.types.sim_space_weaver_resource_name


class CreateSnapshotInput(TypedDict, closed=True):
    simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation.</p>"""
    destination: "capo_simspaceweaver.types.s3_destination.S3Destination"
    """<p>The Amazon S3 bucket and optional folder (object key prefix) where SimSpace Weaver creates the snapshot file.</p> <p>The Amazon S3 bucket must be in the same Amazon Web Services Region as the simulation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSnapshotInput) -> dict:
    out: dict = {}
    out["Simulation"] = value["simulation"]
    import capo_simspaceweaver.types.s3_destination

    out["Destination"] = capo_simspaceweaver.types.s3_destination.serialize_json(
        value["destination"]
    )
    return out


def deserialize_json(data: dict) -> CreateSnapshotInput:
    out: CreateSnapshotInput = {}  # type: ignore[typeddict-item]
    if data.get("Simulation") is not None:
        out["simulation"] = data["Simulation"]
    else:
        out["simulation"] = ""
    if data.get("Destination") is not None:
        import capo_simspaceweaver.types.s3_destination

        out["destination"] = capo_simspaceweaver.types.s3_destination.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError("CreateSnapshotInput.destination required")
    return out
