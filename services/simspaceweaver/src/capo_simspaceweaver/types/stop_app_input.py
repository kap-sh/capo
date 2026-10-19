"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StopAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_resource_name


class StopAppInput(TypedDict, closed=True):
    simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation of the app.</p>"""
    domain: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the domain of the app.</p>"""
    app: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopAppInput) -> dict:
    out: dict = {}
    out["Simulation"] = value["simulation"]
    out["Domain"] = value["domain"]
    out["App"] = value["app"]
    return out


def deserialize_json(data: dict) -> StopAppInput:
    out: StopAppInput = {}  # type: ignore[typeddict-item]
    if data.get("Simulation") is not None:
        out["simulation"] = data["Simulation"]
    else:
        out["simulation"] = ""
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        out["domain"] = ""
    if data.get("App") is not None:
        out["app"] = data["App"]
    else:
        out["app"] = ""
    return out
