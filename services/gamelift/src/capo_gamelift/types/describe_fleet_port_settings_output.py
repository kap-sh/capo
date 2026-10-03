"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetPortSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.ip_permissions_list
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.location_update_status


class DescribeFleetPortSettingsOutput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that was requested. </p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    inbound_permissions: NotRequired[
        "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
    ]
    """<p>The port settings for the requested fleet ID.</p>"""
    update_status: NotRequired[
        "capo_gamelift.types.location_update_status.LocationUpdateStatus"
    ]
    """<p>The current status of updates to the fleet's port settings in the requested fleet location. A status of <code>PENDING_UPDATE</code> indicates that an update was requested for the fleet but has not yet been completed for the location.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The requested fleet location, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetPortSettingsOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "inbound_permissions" in value:
        import capo_gamelift.types.ip_permissions_list

        out["InboundPermissions"] = (
            capo_gamelift.types.ip_permissions_list.serialize_aws_json_1_1(
                value["inbound_permissions"]
            )
        )
    if "update_status" in value:
        import capo_gamelift.types.location_update_status

        out["UpdateStatus"] = (
            capo_gamelift.types.location_update_status.serialize_aws_json_1_1(
                value["update_status"]
            )
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetPortSettingsOutput:
    out: DescribeFleetPortSettingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("InboundPermissions") is not None:
        import capo_gamelift.types.ip_permissions_list

        out["inbound_permissions"] = (
            capo_gamelift.types.ip_permissions_list.deserialize_aws_json_1_1(
                data["InboundPermissions"]
            )
        )
    if data.get("UpdateStatus") is not None:
        import capo_gamelift.types.location_update_status

        out["update_status"] = (
            capo_gamelift.types.location_update_status.deserialize_aws_json_1_1(
                data["UpdateStatus"]
            )
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
