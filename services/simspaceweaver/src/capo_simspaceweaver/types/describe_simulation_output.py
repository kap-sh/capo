"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#DescribeSimulationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.description
    import capo_simspaceweaver.types.live_simulation_state
    import capo_simspaceweaver.types.logging_configuration
    import capo_simspaceweaver.types.optional_string
    import capo_simspaceweaver.types.role_arn
    import capo_simspaceweaver.types.s3_location
    import capo_simspaceweaver.types.sim_space_weaver_arn
    import capo_simspaceweaver.types.sim_space_weaver_resource_name
    import capo_simspaceweaver.types.simulation_status
    import capo_simspaceweaver.types.simulation_target_status
    import capo_simspaceweaver.types.time_to_live_string
    import capo_simspaceweaver.types.timestamp
    import capo_simspaceweaver.types.uuid


class DescribeSimulationOutput(TypedDict, closed=True):
    name: NotRequired[
        "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the simulation.</p>"""
    execution_id: NotRequired["capo_simspaceweaver.types.uuid.UUID"]
    """<p>A universally unique identifier (UUID) for this simulation.</p>"""
    arn: NotRequired["capo_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn"]
    """<p>The Amazon Resource Name (ARN) of the simulation. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    description: NotRequired["capo_simspaceweaver.types.description.Description"]
    """<p>The description of the simulation.</p>"""
    role_arn: NotRequired["capo_simspaceweaver.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the simulation assumes to perform actions. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>. For more information about IAM roles, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM roles</a> in the <i>Identity and Access Management User Guide</i>.</p>"""
    creation_time: NotRequired["capo_simspaceweaver.types.timestamp.Timestamp"]
    """<p>The time when the simulation was created, expressed as the number of seconds and milliseconds in UTC since the Unix epoch (0:0:0.000, January 1, 1970).</p>"""
    status: NotRequired["capo_simspaceweaver.types.simulation_status.SimulationStatus"]
    """<p>The current lifecycle state of the simulation.</p>"""
    target_status: NotRequired[
        "capo_simspaceweaver.types.simulation_target_status.SimulationTargetStatus"
    ]
    """<p>The desired lifecycle state of the simulation.</p>"""
    schema_s3_location: NotRequired["capo_simspaceweaver.types.s3_location.S3Location"]
    """<p>The location of the simulation schema in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"> <i>Amazon Simple Storage Service User Guide</i> </a>.</p>"""
    schema_error: NotRequired[
        "capo_simspaceweaver.types.optional_string.OptionalString"
    ]
    """<p>An error message that SimSpace Weaver returns only if there is a problem with the simulation schema.</p>"""
    logging_configuration: NotRequired[
        "capo_simspaceweaver.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>Settings that control how SimSpace Weaver handles your simulation log data.</p>"""
    live_simulation_state: NotRequired[
        "capo_simspaceweaver.types.live_simulation_state.LiveSimulationState"
    ]
    """<p>A collection of additional state information, such as domain and clock configuration.</p>"""
    maximum_duration: NotRequired[
        "capo_simspaceweaver.types.time_to_live_string.TimeToLiveString"
    ]
    """<p>The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is <code>14D</code>, or its equivalent in the other units. The default value is <code>14D</code>. A value equivalent to <code>0</code> makes the simulation immediately transition to <code>Stopping</code> as soon as it reaches <code>Started</code>.</p>"""
    snapshot_s3_location: NotRequired[
        "capo_simspaceweaver.types.s3_location.S3Location"
    ]
    start_error: NotRequired["capo_simspaceweaver.types.optional_string.OptionalString"]
    """<p>An error message that SimSpace Weaver returns only if a problem occurs when the simulation is in the <code>STARTING</code> state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSimulationOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "creation_time" in value:
        import capo_simspaceweaver.types.timestamp

        out["CreationTime"] = capo_simspaceweaver.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "target_status" in value:
        out["TargetStatus"] = value["target_status"]
    if "schema_s3_location" in value:
        import capo_simspaceweaver.types.s3_location

        out["SchemaS3Location"] = capo_simspaceweaver.types.s3_location.serialize_json(
            value["schema_s3_location"]
        )
    if "schema_error" in value:
        out["SchemaError"] = value["schema_error"]
    if "logging_configuration" in value:
        import capo_simspaceweaver.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_simspaceweaver.types.logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "live_simulation_state" in value:
        import capo_simspaceweaver.types.live_simulation_state

        out["LiveSimulationState"] = (
            capo_simspaceweaver.types.live_simulation_state.serialize_json(
                value["live_simulation_state"]
            )
        )
    if "maximum_duration" in value:
        out["MaximumDuration"] = value["maximum_duration"]
    if "snapshot_s3_location" in value:
        import capo_simspaceweaver.types.s3_location

        out["SnapshotS3Location"] = (
            capo_simspaceweaver.types.s3_location.serialize_json(
                value["snapshot_s3_location"]
            )
        )
    if "start_error" in value:
        out["StartError"] = value["start_error"]
    return out


def deserialize_json(data: dict) -> DescribeSimulationOutput:
    out: DescribeSimulationOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ExecutionId") is not None:
        out["execution_id"] = data["ExecutionId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("CreationTime") is not None:
        import capo_simspaceweaver.types.timestamp

        out["creation_time"] = capo_simspaceweaver.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("TargetStatus") is not None:
        out["target_status"] = data["TargetStatus"]
    if data.get("SchemaS3Location") is not None:
        import capo_simspaceweaver.types.s3_location

        out["schema_s3_location"] = (
            capo_simspaceweaver.types.s3_location.deserialize_json(
                data["SchemaS3Location"]
            )
        )
    if data.get("SchemaError") is not None:
        out["schema_error"] = data["SchemaError"]
    if data.get("LoggingConfiguration") is not None:
        import capo_simspaceweaver.types.logging_configuration

        out["logging_configuration"] = (
            capo_simspaceweaver.types.logging_configuration.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    if data.get("LiveSimulationState") is not None:
        import capo_simspaceweaver.types.live_simulation_state

        out["live_simulation_state"] = (
            capo_simspaceweaver.types.live_simulation_state.deserialize_json(
                data["LiveSimulationState"]
            )
        )
    if data.get("MaximumDuration") is not None:
        out["maximum_duration"] = data["MaximumDuration"]
    if data.get("SnapshotS3Location") is not None:
        import capo_simspaceweaver.types.s3_location

        out["snapshot_s3_location"] = (
            capo_simspaceweaver.types.s3_location.deserialize_json(
                data["SnapshotS3Location"]
            )
        )
    if data.get("StartError") is not None:
        out["start_error"] = data["StartError"]
    return out
