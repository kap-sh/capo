"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StopSimulationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_resource_name


class StopSimulationInput(TypedDict, closed=True):
    simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopSimulationInput) -> dict:
    out: dict = {}
    out["Simulation"] = value["simulation"]
    return out


def deserialize_json(data: dict) -> StopSimulationInput:
    out: StopSimulationInput = {}  # type: ignore[typeddict-item]
    if data.get("Simulation") is not None:
        out["simulation"] = data["Simulation"]
    else:
        out["simulation"] = ""
    return out
