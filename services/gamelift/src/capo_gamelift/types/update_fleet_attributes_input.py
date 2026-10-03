"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateFleetAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.anywhere_configuration
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.metric_group_list
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.protection_policy
    import capo_gamelift.types.resource_creation_limit_policy


class UpdateFleetAttributesInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to update attribute metadata for. You can use either the fleet ID or ARN value.</p>"""
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a fleet. Fleet names do not need to be unique.</p>"""
    description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A human-readable description of a fleet.</p>"""
    new_game_session_protection_policy: NotRequired[
        "capo_gamelift.types.protection_policy.ProtectionPolicy"
    ]
    """<p>The game session protection policy to apply to all new game sessions created in this fleet. Game sessions that already exist are not affected. You can set protection for individual game sessions using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html">UpdateGameSession</a> .</p> <ul> <li> <p> <b>NoProtection</b> -- The game session can be terminated during a scale-down event.</p> </li> <li> <p> <b>FullProtection</b> -- If the game session is in an <code>ACTIVE</code> status, it cannot be terminated during a scale-down event.</p> </li> </ul>"""
    resource_creation_limit_policy: NotRequired[
        "capo_gamelift.types.resource_creation_limit_policy.ResourceCreationLimitPolicy"
    ]
    """<p>Policy settings that limit the number of game sessions an individual player can create over a span of time. </p>"""
    metric_groups: NotRequired["capo_gamelift.types.metric_group_list.MetricGroupList"]
    """<p>The name of a metric group to add this fleet to. Use a metric group in Amazon CloudWatch to aggregate the metrics from multiple fleets. Provide an existing metric group name, or create a new metric group by providing a new name. A fleet can only be in one metric group at a time.</p>"""
    anywhere_configuration: NotRequired[
        "capo_gamelift.types.anywhere_configuration.AnywhereConfiguration"
    ]
    """<p>Amazon GameLift Servers Anywhere configuration options.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFleetAttributesInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "new_game_session_protection_policy" in value:
        import capo_gamelift.types.protection_policy

        out["NewGameSessionProtectionPolicy"] = (
            capo_gamelift.types.protection_policy.serialize_aws_json_1_1(
                value["new_game_session_protection_policy"]
            )
        )
    if "resource_creation_limit_policy" in value:
        import capo_gamelift.types.resource_creation_limit_policy

        out["ResourceCreationLimitPolicy"] = (
            capo_gamelift.types.resource_creation_limit_policy.serialize_aws_json_1_1(
                value["resource_creation_limit_policy"]
            )
        )
    if "metric_groups" in value:
        import capo_gamelift.types.metric_group_list

        out["MetricGroups"] = (
            capo_gamelift.types.metric_group_list.serialize_aws_json_1_1(
                value["metric_groups"]
            )
        )
    if "anywhere_configuration" in value:
        import capo_gamelift.types.anywhere_configuration

        out["AnywhereConfiguration"] = (
            capo_gamelift.types.anywhere_configuration.serialize_aws_json_1_1(
                value["anywhere_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFleetAttributesInput:
    out: UpdateFleetAttributesInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("NewGameSessionProtectionPolicy") is not None:
        import capo_gamelift.types.protection_policy

        out["new_game_session_protection_policy"] = (
            capo_gamelift.types.protection_policy.deserialize_aws_json_1_1(
                data["NewGameSessionProtectionPolicy"]
            )
        )
    if data.get("ResourceCreationLimitPolicy") is not None:
        import capo_gamelift.types.resource_creation_limit_policy

        out["resource_creation_limit_policy"] = (
            capo_gamelift.types.resource_creation_limit_policy.deserialize_aws_json_1_1(
                data["ResourceCreationLimitPolicy"]
            )
        )
    if data.get("MetricGroups") is not None:
        import capo_gamelift.types.metric_group_list

        out["metric_groups"] = (
            capo_gamelift.types.metric_group_list.deserialize_aws_json_1_1(
                data["MetricGroups"]
            )
        )
    if data.get("AnywhereConfiguration") is not None:
        import capo_gamelift.types.anywhere_configuration

        out["anywhere_configuration"] = (
            capo_gamelift.types.anywhere_configuration.deserialize_aws_json_1_1(
                data["AnywhereConfiguration"]
            )
        )
    return out
