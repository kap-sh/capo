"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetUtilization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.whole_number


class FleetUtilization(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet associated with the location.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    active_server_process_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The number of server processes in <code>ACTIVE</code> status that are currently running across all instances in the fleet location. </p>"""
    active_game_session_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The number of active game sessions that are currently being hosted across all instances in the fleet location.</p>"""
    current_player_session_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The number of active player sessions that are currently being hosted across all instances in the fleet location.</p>"""
    maximum_player_session_count: NotRequired[
        "capo_gamelift.types.whole_number.WholeNumber"
    ]
    """<p>The maximum number of players allowed across all game sessions that are currently being hosted across all instances in the fleet location.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The fleet location for the fleet utilization information, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetUtilization) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "active_server_process_count" in value:
        out["ActiveServerProcessCount"] = value["active_server_process_count"]
    if "active_game_session_count" in value:
        out["ActiveGameSessionCount"] = value["active_game_session_count"]
    if "current_player_session_count" in value:
        out["CurrentPlayerSessionCount"] = value["current_player_session_count"]
    if "maximum_player_session_count" in value:
        out["MaximumPlayerSessionCount"] = value["maximum_player_session_count"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetUtilization:
    out: FleetUtilization = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("ActiveServerProcessCount") is not None:
        out["active_server_process_count"] = data["ActiveServerProcessCount"]
    if data.get("ActiveGameSessionCount") is not None:
        out["active_game_session_count"] = data["ActiveGameSessionCount"]
    if data.get("CurrentPlayerSessionCount") is not None:
        out["current_player_session_count"] = data["CurrentPlayerSessionCount"]
    if data.get("MaximumPlayerSessionCount") is not None:
        out["maximum_player_session_count"] = data["MaximumPlayerSessionCount"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
