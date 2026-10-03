"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionQueue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.filter_configuration
    import capo_gamelift.types.game_session_queue_arn
    import capo_gamelift.types.game_session_queue_destination_list
    import capo_gamelift.types.game_session_queue_name
    import capo_gamelift.types.player_latency_policy_list
    import capo_gamelift.types.priority_configuration
    import capo_gamelift.types.queue_custom_event_data
    import capo_gamelift.types.queue_sns_arn_string_model
    import capo_gamelift.types.whole_number


class GameSessionQueue(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.game_session_queue_name.GameSessionQueueName"
    ]
    """<p>A descriptive label that is associated with game session queue. Queue names must be unique within each Region.</p>"""
    game_session_queue_arn: NotRequired[
        "capo_gamelift.types.game_session_queue_arn.GameSessionQueueArn"
    ]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::gamesessionqueue/<queue name></code>. In a Amazon GameLift Servers game session queue ARN, the resource ID matches the <i>Name</i> value.</p>"""
    timeout_in_seconds: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p>The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a <code>TIMED_OUT</code> status.</p> <note> <p>The minimum value is 10 and the maximum value is 600.</p> </note>"""
    player_latency_policies: NotRequired[
        "capo_gamelift.types.player_latency_policy_list.PlayerLatencyPolicyList"
    ]
    """<p>A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value. </p>"""
    destinations: NotRequired[
        "capo_gamelift.types.game_session_queue_destination_list.GameSessionQueueDestinationList"
    ]
    """<p>A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.</p>"""
    filter_configuration: NotRequired[
        "capo_gamelift.types.filter_configuration.FilterConfiguration"
    ]
    """<p>A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of Amazon Web Services Region codes, such as <code>us-west-2</code>. If this parameter is not set, game sessions can be placed in any queue location. </p>"""
    priority_configuration: NotRequired[
        "capo_gamelift.types.priority_configuration.PriorityConfiguration"
    ]
    """<p>Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process. </p>"""
    custom_event_data: NotRequired[
        "capo_gamelift.types.queue_custom_event_data.QueueCustomEventData"
    ]
    """<p> Information that is added to all events that are related to this game session queue.</p>"""
    notification_target: NotRequired[
        "capo_gamelift.types.queue_sns_arn_string_model.QueueSnsArnStringModel"
    ]
    """<p>An SNS topic ARN that is set up to receive game session placement notifications. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html"> Setting up notifications for game session placement</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionQueue) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "game_session_queue_arn" in value:
        out["GameSessionQueueArn"] = value["game_session_queue_arn"]
    if "timeout_in_seconds" in value:
        out["TimeoutInSeconds"] = value["timeout_in_seconds"]
    if "player_latency_policies" in value:
        import capo_gamelift.types.player_latency_policy_list

        out["PlayerLatencyPolicies"] = (
            capo_gamelift.types.player_latency_policy_list.serialize_aws_json_1_1(
                value["player_latency_policies"]
            )
        )
    if "destinations" in value:
        import capo_gamelift.types.game_session_queue_destination_list

        out["Destinations"] = (
            capo_gamelift.types.game_session_queue_destination_list.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "filter_configuration" in value:
        import capo_gamelift.types.filter_configuration

        out["FilterConfiguration"] = (
            capo_gamelift.types.filter_configuration.serialize_aws_json_1_1(
                value["filter_configuration"]
            )
        )
    if "priority_configuration" in value:
        import capo_gamelift.types.priority_configuration

        out["PriorityConfiguration"] = (
            capo_gamelift.types.priority_configuration.serialize_aws_json_1_1(
                value["priority_configuration"]
            )
        )
    if "custom_event_data" in value:
        out["CustomEventData"] = value["custom_event_data"]
    if "notification_target" in value:
        out["NotificationTarget"] = value["notification_target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSessionQueue:
    out: GameSessionQueue = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("GameSessionQueueArn") is not None:
        out["game_session_queue_arn"] = data["GameSessionQueueArn"]
    if data.get("TimeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["TimeoutInSeconds"]
    if data.get("PlayerLatencyPolicies") is not None:
        import capo_gamelift.types.player_latency_policy_list

        out["player_latency_policies"] = (
            capo_gamelift.types.player_latency_policy_list.deserialize_aws_json_1_1(
                data["PlayerLatencyPolicies"]
            )
        )
    if data.get("Destinations") is not None:
        import capo_gamelift.types.game_session_queue_destination_list

        out["destinations"] = (
            capo_gamelift.types.game_session_queue_destination_list.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    if data.get("FilterConfiguration") is not None:
        import capo_gamelift.types.filter_configuration

        out["filter_configuration"] = (
            capo_gamelift.types.filter_configuration.deserialize_aws_json_1_1(
                data["FilterConfiguration"]
            )
        )
    if data.get("PriorityConfiguration") is not None:
        import capo_gamelift.types.priority_configuration

        out["priority_configuration"] = (
            capo_gamelift.types.priority_configuration.deserialize_aws_json_1_1(
                data["PriorityConfiguration"]
            )
        )
    if data.get("CustomEventData") is not None:
        out["custom_event_data"] = data["CustomEventData"]
    if data.get("NotificationTarget") is not None:
        out["notification_target"] = data["NotificationTarget"]
    return out
