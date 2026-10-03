"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_arn
    import capo_simspaceweaver.types.sim_space_weaver_resource_name
    import capo_simspaceweaver.types.simulation_status
    import capo_simspaceweaver.types.simulation_target_status
    import capo_simspaceweaver.types.timestamp


class SimulationMetadata(TypedDict, closed=True):
    name: NotRequired[
        "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the simulation.</p>"""
    arn: NotRequired["capo_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn"]
    """<p>The Amazon Resource Name (ARN) of the simulation. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    creation_time: NotRequired["capo_simspaceweaver.types.timestamp.Timestamp"]
    """<p>The time when the simulation was created, expressed as the number of seconds and milliseconds in UTC since the Unix epoch (0:0:0.000, January 1, 1970).</p>"""
    status: NotRequired["capo_simspaceweaver.types.simulation_status.SimulationStatus"]
    """<p>The current status of the simulation.</p>"""
    target_status: NotRequired[
        "capo_simspaceweaver.types.simulation_target_status.SimulationTargetStatus"
    ]
    """<p>The desired status of the simulation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimulationMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_time" in value:
        import capo_simspaceweaver.types.timestamp

        out["CreationTime"] = capo_simspaceweaver.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "target_status" in value:
        out["TargetStatus"] = value["target_status"]
    return out


def deserialize_json(data: dict) -> SimulationMetadata:
    out: SimulationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreationTime") is not None:
        import capo_simspaceweaver.types.timestamp

        out["creation_time"] = capo_simspaceweaver.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("TargetStatus") is not None:
        out["target_status"] = data["TargetStatus"]
    return out
