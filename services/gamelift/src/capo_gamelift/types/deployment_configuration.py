"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.deployment_impairment_strategy
    import capo_gamelift.types.deployment_protection_strategy
    import capo_gamelift.types.minimum_healthy_percentage


class DeploymentConfiguration(TypedDict, closed=True):
    protection_strategy: NotRequired[
        "capo_gamelift.types.deployment_protection_strategy.DeploymentProtectionStrategy"
    ]
    """<p>Determines how fleet deployment activity affects active game sessions on the fleet. A protected game session can't be terminated while it's active; a fleet sets the default protection for its new game sessions with <code>NewGameSessionProtectionPolicy</code>.</p> <ul> <li> <p> <code>WITH_PROTECTION</code> -- The deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends.</p> </li> <li> <p> <code>IGNORE_PROTECTION</code> -- The deployment replaces containers regardless of game session activity, including active game sessions. This option is useful during development and testing.</p> </li> </ul> <p>This setting also affects how long deployment validation can take. When the fleet's <code>NewGameSessionProtectionPolicy</code> is <code>FullProtection</code> and the deployment uses <code>WITH_PROTECTION</code>, validation waits for protected game sessions to end.</p> <p>Default value: <code>WITH_PROTECTION</code> </p>"""
    minimum_healthy_percentage: NotRequired[
        "capo_gamelift.types.minimum_healthy_percentage.MinimumHealthyPercentage"
    ]
    """<p>Sets the minimum percentage of the fleet's game server container groups to keep healthy during deployment activity. A low value favors deployment speed; a high value favors game server availability. For example, if the fleet runs 20 game server container groups and this value is 75, Amazon GameLift Servers keeps at least 15 of them healthy, so it replaces no more than 5 at a time.</p> <p>Default value: 75</p>"""
    impairment_strategy: NotRequired[
        "capo_gamelift.types.deployment_impairment_strategy.DeploymentImpairmentStrategy"
    ]
    """<p>Determines what actions to take if a deployment fails validation. If the fleet is multi-location, this strategy applies across all fleet locations.</p> <ul> <li> <p> <code>ROLLBACK</code> -- Returns all of the fleet's containers to the last successful deployment.</p> </li> <li> <p> <code>MAINTAIN</code> -- Keeps the containers that failed validation in place so that you can inspect them, and returns all other containers to the last successful deployment. Use this option when you're deploying a container image that you want to be able to debug on failure.</p> </li> </ul> <p>Default value: <code>MAINTAIN</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentConfiguration) -> dict:
    out: dict = {}
    if "protection_strategy" in value:
        import capo_gamelift.types.deployment_protection_strategy

        out["ProtectionStrategy"] = (
            capo_gamelift.types.deployment_protection_strategy.serialize_aws_json_1_1(
                value["protection_strategy"]
            )
        )
    if "minimum_healthy_percentage" in value:
        out["MinimumHealthyPercentage"] = value["minimum_healthy_percentage"]
    if "impairment_strategy" in value:
        import capo_gamelift.types.deployment_impairment_strategy

        out["ImpairmentStrategy"] = (
            capo_gamelift.types.deployment_impairment_strategy.serialize_aws_json_1_1(
                value["impairment_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentConfiguration:
    out: DeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionStrategy") is not None:
        import capo_gamelift.types.deployment_protection_strategy

        out["protection_strategy"] = (
            capo_gamelift.types.deployment_protection_strategy.deserialize_aws_json_1_1(
                data["ProtectionStrategy"]
            )
        )
    if data.get("MinimumHealthyPercentage") is not None:
        out["minimum_healthy_percentage"] = data["MinimumHealthyPercentage"]
    if data.get("ImpairmentStrategy") is not None:
        import capo_gamelift.types.deployment_impairment_strategy

        out["impairment_strategy"] = (
            capo_gamelift.types.deployment_impairment_strategy.deserialize_aws_json_1_1(
                data["ImpairmentStrategy"]
            )
        )
    return out
