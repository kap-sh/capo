"""Generated from Smithy shape ``com.amazonaws.gamelift#GetComputeAuthTokenOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_arn
    import capo_gamelift.types.compute_auth_token
    import capo_gamelift.types.compute_name_or_arn
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.timestamp


class GetComputeAuthTokenOutput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that the compute is registered to.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    compute_name: NotRequired[
        "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
    ]
    """<p>The name of the compute resource that the authentication token is issued to.</p>"""
    compute_arn: NotRequired["capo_gamelift.types.compute_arn.ComputeArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to an Amazon GameLift Servers compute resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::compute/compute-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    auth_token: NotRequired["capo_gamelift.types.compute_auth_token.ComputeAuthToken"]
    """<p>A valid temporary authentication token.</p>"""
    expiration_timestamp: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>The amount of time until the authentication token is no longer valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComputeAuthTokenOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "compute_arn" in value:
        out["ComputeArn"] = value["compute_arn"]
    if "auth_token" in value:
        out["AuthToken"] = value["auth_token"]
    if "expiration_timestamp" in value:
        import capo_gamelift.types.timestamp

        out["ExpirationTimestamp"] = (
            capo_gamelift.types.timestamp.serialize_aws_json_1_1(
                value["expiration_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComputeAuthTokenOutput:
    out: GetComputeAuthTokenOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    if data.get("ComputeArn") is not None:
        out["compute_arn"] = data["ComputeArn"]
    if data.get("AuthToken") is not None:
        out["auth_token"] = data["AuthToken"]
    if data.get("ExpirationTimestamp") is not None:
        import capo_gamelift.types.timestamp

        out["expiration_timestamp"] = (
            capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTimestamp"]
            )
        )
    return out
