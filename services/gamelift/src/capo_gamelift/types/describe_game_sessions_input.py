"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.alias_id_or_arn
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer


class DescribeGameSessionsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to retrieve game sessions for. You can use either the fleet ID or ARN value. </p>"""
    game_session_id: NotRequired["capo_gamelift.types.arn_string_model.ArnStringModel"]
    """<p>An identifier for the game session that is unique across all regions to retrieve. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>"""
    alias_id: NotRequired["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"]
    """<p>A unique identifier for the alias associated with the fleet to retrieve game sessions for. You can use either the alias ID or ARN value.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>A fleet location to get game sessions for. You can specify a fleet's home Region or a remote location. Use the Amazon Web Services Region code format, such as <code>us-west-2</code>. </p>"""
    status_filter: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Game session status to filter results on. You can filter on the following states: <code>ACTIVE</code>, <code>TERMINATED</code>, <code>ACTIVATING</code>, and <code>TERMINATING</code>. The last two are transitory and used for only very brief periods of time. </p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "location" in value:
        out["Location"] = value["location"]
    if "status_filter" in value:
        out["StatusFilter"] = value["status_filter"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionsInput:
    out: DescribeGameSessionsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("StatusFilter") is not None:
        out["status_filter"] = data["StatusFilter"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeGameSessionsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "game_session_id" in value:
        out["GameSessionId"] = value["game_session_id"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "location" in value:
        out["Location"] = value["location"]
    if "status_filter" in value:
        out["StatusFilter"] = value["status_filter"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeGameSessionsInput:
    out: DescribeGameSessionsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("GameSessionId") is not None:
        out["game_session_id"] = data["GameSessionId"]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("StatusFilter") is not None:
        out["status_filter"] = data["StatusFilter"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
