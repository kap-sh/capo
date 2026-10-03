"""Generated from Smithy shape ``com.amazonaws.gamelift#GetComputeAccessOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.aws_credentials
    import capo_gamelift.types.compute_arn
    import capo_gamelift.types.compute_name_or_arn
    import capo_gamelift.types.container_identifier_list
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.session_target


class GetComputeAccessOutput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>The ID of the fleet that holds the compute resource to be accessed.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    compute_name: NotRequired[
        "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
    ]
    """<p>The identifier of the compute resource to be accessed. This value might be either a compute name or an instance ID.</p>"""
    compute_arn: NotRequired["capo_gamelift.types.compute_arn.ComputeArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to an Amazon GameLift Servers compute resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::compute/compute-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    credentials: NotRequired["capo_gamelift.types.aws_credentials.AwsCredentials"]
    """<p>A set of temporary Amazon Web Services credentials for use when connecting to the compute resource with Amazon EC2 Systems Manager (SSM).</p>"""
    target: NotRequired["capo_gamelift.types.session_target.SessionTarget"]
    """<p>The instance ID where the compute resource is running.</p>"""
    container_identifiers: NotRequired[
        "capo_gamelift.types.container_identifier_list.ContainerIdentifierList"
    ]
    """<p>For a managed container fleet, a list of containers on the compute. Use the container runtime ID with Docker commands to connect to a specific container. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComputeAccessOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "compute_arn" in value:
        out["ComputeArn"] = value["compute_arn"]
    if "credentials" in value:
        import capo_gamelift.types.aws_credentials

        out["Credentials"] = capo_gamelift.types.aws_credentials.serialize_aws_json_1_1(
            value["credentials"]
        )
    if "target" in value:
        out["Target"] = value["target"]
    if "container_identifiers" in value:
        import capo_gamelift.types.container_identifier_list

        out["ContainerIdentifiers"] = (
            capo_gamelift.types.container_identifier_list.serialize_aws_json_1_1(
                value["container_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComputeAccessOutput:
    out: GetComputeAccessOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    if data.get("ComputeArn") is not None:
        out["compute_arn"] = data["ComputeArn"]
    if data.get("Credentials") is not None:
        import capo_gamelift.types.aws_credentials

        out["credentials"] = (
            capo_gamelift.types.aws_credentials.deserialize_aws_json_1_1(
                data["Credentials"]
            )
        )
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    if data.get("ContainerIdentifiers") is not None:
        import capo_gamelift.types.container_identifier_list

        out["container_identifiers"] = (
            capo_gamelift.types.container_identifier_list.deserialize_aws_json_1_1(
                data["ContainerIdentifiers"]
            )
        )
    return out
