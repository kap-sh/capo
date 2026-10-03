"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StartSimulationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_simspaceweaver.types.client_token
    import capo_simspaceweaver.types.description
    import capo_simspaceweaver.types.role_arn
    import capo_simspaceweaver.types.s3_location
    import capo_simspaceweaver.types.sim_space_weaver_resource_name
    import capo_simspaceweaver.types.tag_map
    import capo_simspaceweaver.types.time_to_live_string


class StartSimulationInput(TypedDict, closed=True):
    client_token: NotRequired["capo_simspaceweaver.types.client_token.ClientToken"]
    """<p>A value that you provide to ensure that repeated calls to this API operation using the same parameters complete only once. A <code>ClientToken</code> is also known as an <i>idempotency token</i>. A <code>ClientToken</code> expires after 24 hours.</p>"""
    name: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation.</p>"""
    description: NotRequired["capo_simspaceweaver.types.description.Description"]
    """<p>The description of the simulation.</p>"""
    role_arn: "capo_simspaceweaver.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the simulation assumes to perform actions. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>. For more information about IAM roles, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM roles</a> in the <i>Identity and Access Management User Guide</i>.</p>"""
    schema_s3_location: NotRequired["capo_simspaceweaver.types.s3_location.S3Location"]
    """<p>The location of the simulation schema in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"> <i>Amazon Simple Storage Service User Guide</i> </a>.</p> <p>Provide a <code>SchemaS3Location</code> to start your simulation from a schema.</p> <p>If you provide a <code>SchemaS3Location</code> then you can't provide a <code>SnapshotS3Location</code>.</p>"""
    maximum_duration: NotRequired[
        "capo_simspaceweaver.types.time_to_live_string.TimeToLiveString"
    ]
    """<p>The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is <code>14D</code>, or its equivalent in the other units. The default value is <code>14D</code>. A value equivalent to <code>0</code> makes the simulation immediately transition to <code>Stopping</code> as soon as it reaches <code>Started</code>.</p>"""
    tags: NotRequired["capo_simspaceweaver.types.tag_map.TagMap"]
    """<p>A list of tags for the simulation. For more information about tags, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    snapshot_s3_location: NotRequired[
        "capo_simspaceweaver.types.s3_location.S3Location"
    ]
    """<p>The location of the snapshot .zip file in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"> <i>Amazon Simple Storage Service User Guide</i> </a>.</p> <p>Provide a <code>SnapshotS3Location</code> to start your simulation from a snapshot.</p> <p>The Amazon S3 bucket must be in the same Amazon Web Services Region as the simulation.</p> <p>If you provide a <code>SnapshotS3Location</code> then you can't provide a <code>SchemaS3Location</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSimulationInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["RoleArn"] = value["role_arn"]
    if "schema_s3_location" in value:
        import capo_simspaceweaver.types.s3_location

        out["SchemaS3Location"] = capo_simspaceweaver.types.s3_location.serialize_json(
            value["schema_s3_location"]
        )
    if "maximum_duration" in value:
        out["MaximumDuration"] = value["maximum_duration"]
    if "tags" in value:
        import capo_simspaceweaver.types.tag_map

        out["Tags"] = capo_simspaceweaver.types.tag_map.serialize_json(value["tags"])
    if "snapshot_s3_location" in value:
        import capo_simspaceweaver.types.s3_location

        out["SnapshotS3Location"] = (
            capo_simspaceweaver.types.s3_location.serialize_json(
                value["snapshot_s3_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartSimulationInput:
    out: StartSimulationInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartSimulationInput.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("StartSimulationInput.role_arn required")
    if data.get("SchemaS3Location") is not None:
        import capo_simspaceweaver.types.s3_location

        out["schema_s3_location"] = (
            capo_simspaceweaver.types.s3_location.deserialize_json(
                data["SchemaS3Location"]
            )
        )
    if data.get("MaximumDuration") is not None:
        out["maximum_duration"] = data["MaximumDuration"]
    if data.get("Tags") is not None:
        import capo_simspaceweaver.types.tag_map

        out["tags"] = capo_simspaceweaver.types.tag_map.deserialize_json(data["Tags"])
    if data.get("SnapshotS3Location") is not None:
        import capo_simspaceweaver.types.s3_location

        out["snapshot_s3_location"] = (
            capo_simspaceweaver.types.s3_location.deserialize_json(
                data["SnapshotS3Location"]
            )
        )
    return out
