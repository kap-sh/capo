"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateMatchmakingConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.backfill_mode
    import capo_gamelift.types.boolean_model
    import capo_gamelift.types.custom_event_data
    import capo_gamelift.types.flex_match_mode
    import capo_gamelift.types.game_property_list
    import capo_gamelift.types.game_session_data
    import capo_gamelift.types.matchmaking_acceptance_timeout_integer
    import capo_gamelift.types.matchmaking_configuration_name
    import capo_gamelift.types.matchmaking_request_timeout_integer
    import capo_gamelift.types.matchmaking_rule_set_name
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.queue_arns_list
    import capo_gamelift.types.sns_arn_string_model
    import capo_gamelift.types.whole_number


class UpdateMatchmakingConfigurationInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
    ]
    """<p>A unique identifier for the matchmaking configuration to update. You can use either the configuration name or ARN value. </p>"""
    description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A description for the matchmaking configuration.</p>"""
    game_session_queue_arns: NotRequired[
        "capo_gamelift.types.queue_arns_list.QueueArnsList"
    ]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::gamesessionqueue/<queue name></code>. Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. A matchmaking configuration supports only one queue; if you specify more than one ARN, the request fails with an <code>InvalidRequestException</code>. If <code>FlexMatchMode</code> is set to <code>STANDALONE</code>, do not set this parameter.</p>"""
    request_timeout_seconds: NotRequired[
        "capo_gamelift.types.matchmaking_request_timeout_integer.MatchmakingRequestTimeoutInteger"
    ]
    """<p>The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.</p>"""
    acceptance_timeout_seconds: NotRequired[
        "capo_gamelift.types.matchmaking_acceptance_timeout_integer.MatchmakingAcceptanceTimeoutInteger"
    ]
    """<p>The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.</p>"""
    acceptance_required: NotRequired["capo_gamelift.types.boolean_model.BooleanModel"]
    """<p>A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE. With this option enabled, matchmaking tickets use the status <code>REQUIRES_ACCEPTANCE</code> to indicate when a completed potential match is waiting for player acceptance. </p>"""
    rule_set_name: NotRequired[
        "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
    ]
    """<p>A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.</p>"""
    notification_target: NotRequired[
        "capo_gamelift.types.sns_arn_string_model.SnsArnStringModel"
    ]
    """<p>An SNS topic ARN that is set up to receive matchmaking notifications. See <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html"> Setting up notifications for matchmaking</a> for more information.</p>"""
    additional_player_count: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p>The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>"""
    custom_event_data: NotRequired[
        "capo_gamelift.types.custom_event_data.CustomEventData"
    ]
    """<p>Information to add to all events related to the matchmaking configuration. </p>"""
    game_properties: NotRequired[
        "capo_gamelift.types.game_property_list.GamePropertyList"
    ]
    """<p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>. This information is added to the new <code>GameSession</code> object that is created for a successful match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>"""
    game_session_data: NotRequired[
        "capo_gamelift.types.game_session_data.GameSessionData"
    ]
    """<p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>. This information is added to the game session that is created for a successful match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>"""
    backfill_mode: NotRequired["capo_gamelift.types.backfill_mode.BackfillMode"]
    """<p>The method that is used to backfill game sessions created with this matchmaking configuration. Specify MANUAL when your game manages backfill requests manually or does not use the match backfill feature. Specify AUTOMATIC to have GameLift create a match backfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html">Backfill Existing Games with FlexMatch</a>. Automatic backfill is not available when <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>"""
    flex_match_mode: NotRequired["capo_gamelift.types.flex_match_mode.FlexMatchMode"]
    """<p>Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution. </p> <ul> <li> <p> <b>STANDALONE</b> - FlexMatch forms matches and returns match information, including players and team assignments, in a <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded"> MatchmakingSucceeded</a> event.</p> </li> <li> <p> <b>WITH_QUEUE</b> - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMatchmakingConfigurationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "game_session_queue_arns" in value:
        import capo_gamelift.types.queue_arns_list

        out["GameSessionQueueArns"] = (
            capo_gamelift.types.queue_arns_list.serialize_aws_json_1_1(
                value["game_session_queue_arns"]
            )
        )
    if "request_timeout_seconds" in value:
        out["RequestTimeoutSeconds"] = value["request_timeout_seconds"]
    if "acceptance_timeout_seconds" in value:
        out["AcceptanceTimeoutSeconds"] = value["acceptance_timeout_seconds"]
    if "acceptance_required" in value:
        out["AcceptanceRequired"] = value["acceptance_required"]
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "notification_target" in value:
        out["NotificationTarget"] = value["notification_target"]
    if "additional_player_count" in value:
        out["AdditionalPlayerCount"] = value["additional_player_count"]
    if "custom_event_data" in value:
        out["CustomEventData"] = value["custom_event_data"]
    if "game_properties" in value:
        import capo_gamelift.types.game_property_list

        out["GameProperties"] = (
            capo_gamelift.types.game_property_list.serialize_aws_json_1_1(
                value["game_properties"]
            )
        )
    if "game_session_data" in value:
        out["GameSessionData"] = value["game_session_data"]
    if "backfill_mode" in value:
        import capo_gamelift.types.backfill_mode

        out["BackfillMode"] = capo_gamelift.types.backfill_mode.serialize_aws_json_1_1(
            value["backfill_mode"]
        )
    if "flex_match_mode" in value:
        import capo_gamelift.types.flex_match_mode

        out["FlexMatchMode"] = (
            capo_gamelift.types.flex_match_mode.serialize_aws_json_1_1(
                value["flex_match_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMatchmakingConfigurationInput:
    out: UpdateMatchmakingConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("GameSessionQueueArns") is not None:
        import capo_gamelift.types.queue_arns_list

        out["game_session_queue_arns"] = (
            capo_gamelift.types.queue_arns_list.deserialize_aws_json_1_1(
                data["GameSessionQueueArns"]
            )
        )
    if data.get("RequestTimeoutSeconds") is not None:
        out["request_timeout_seconds"] = data["RequestTimeoutSeconds"]
    if data.get("AcceptanceTimeoutSeconds") is not None:
        out["acceptance_timeout_seconds"] = data["AcceptanceTimeoutSeconds"]
    if data.get("AcceptanceRequired") is not None:
        out["acceptance_required"] = data["AcceptanceRequired"]
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    if data.get("NotificationTarget") is not None:
        out["notification_target"] = data["NotificationTarget"]
    if data.get("AdditionalPlayerCount") is not None:
        out["additional_player_count"] = data["AdditionalPlayerCount"]
    if data.get("CustomEventData") is not None:
        out["custom_event_data"] = data["CustomEventData"]
    if data.get("GameProperties") is not None:
        import capo_gamelift.types.game_property_list

        out["game_properties"] = (
            capo_gamelift.types.game_property_list.deserialize_aws_json_1_1(
                data["GameProperties"]
            )
        )
    if data.get("GameSessionData") is not None:
        out["game_session_data"] = data["GameSessionData"]
    if data.get("BackfillMode") is not None:
        import capo_gamelift.types.backfill_mode

        out["backfill_mode"] = (
            capo_gamelift.types.backfill_mode.deserialize_aws_json_1_1(
                data["BackfillMode"]
            )
        )
    if data.get("FlexMatchMode") is not None:
        import capo_gamelift.types.flex_match_mode

        out["flex_match_mode"] = (
            capo_gamelift.types.flex_match_mode.deserialize_aws_json_1_1(
                data["FlexMatchMode"]
            )
        )
    return out
