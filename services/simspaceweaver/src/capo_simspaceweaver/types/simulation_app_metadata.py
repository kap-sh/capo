"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationAppMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_long_resource_name
    import capo_simspaceweaver.types.sim_space_weaver_resource_name
    import capo_simspaceweaver.types.simulation_app_status
    import capo_simspaceweaver.types.simulation_app_target_status


class SimulationAppMetadata(TypedDict, closed=True):
    name: NotRequired[
        "capo_simspaceweaver.types.sim_space_weaver_long_resource_name.SimSpaceWeaverLongResourceName"
    ]
    """<p>The name of the app.</p>"""
    simulation: NotRequired[
        "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the simulation of the app.</p>"""
    domain: NotRequired[
        "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The domain of the app. For more information about domains, see <a href="https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is_key-concepts.html#what-is_key-concepts_domains">Key concepts: Domains</a> in the <i>SimSpace Weaver User Guide</i>.</p>"""
    status: NotRequired[
        "capo_simspaceweaver.types.simulation_app_status.SimulationAppStatus"
    ]
    """<p>The current status of the app.</p>"""
    target_status: NotRequired[
        "capo_simspaceweaver.types.simulation_app_target_status.SimulationAppTargetStatus"
    ]
    """<p>The desired status of the app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimulationAppMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "simulation" in value:
        out["Simulation"] = value["simulation"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "status" in value:
        out["Status"] = value["status"]
    if "target_status" in value:
        out["TargetStatus"] = value["target_status"]
    return out


def deserialize_json(data: dict) -> SimulationAppMetadata:
    out: SimulationAppMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Simulation") is not None:
        out["simulation"] = data["Simulation"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("TargetStatus") is not None:
        out["target_status"] = data["TargetStatus"]
    return out
