"""Generated from Smithy shape ``com.amazonaws.opensearch#DeploymentStrategyOverrideOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.cloned_blue_green_options
    import capo_opensearch.types.deployment_strategy_override


class DeploymentStrategyOverrideOptions(TypedDict, closed=True):
    deployment_strategy: (
        "capo_opensearch.types.deployment_strategy_override.DeploymentStrategyOverride"
    )
    """<p>The deployment strategy to use for this operation. The only valid value is <code>ClonedBlueGreen</code>, which creates a cloned cluster on the target version next to the primary cluster so that you can validate it and shift traffic to it before you cut over.</p>"""
    cloned_blue_green_options: NotRequired[
        "capo_opensearch.types.cloned_blue_green_options.ClonedBlueGreenOptions"
    ]
    """<p>Options that apply when <code>DeploymentStrategy</code> is <code>ClonedBlueGreen</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategyOverrideOptions) -> dict:
    out: dict = {}
    import capo_opensearch.types.deployment_strategy_override

    out["DeploymentStrategy"] = (
        capo_opensearch.types.deployment_strategy_override.serialize_json(
            value["deployment_strategy"]
        )
    )
    if "cloned_blue_green_options" in value:
        import capo_opensearch.types.cloned_blue_green_options

        out["ClonedBlueGreenOptions"] = (
            capo_opensearch.types.cloned_blue_green_options.serialize_json(
                value["cloned_blue_green_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentStrategyOverrideOptions:
    out: DeploymentStrategyOverrideOptions = {}  # type: ignore[typeddict-item]
    if data.get("DeploymentStrategy") is not None:
        import capo_opensearch.types.deployment_strategy_override

        out["deployment_strategy"] = (
            capo_opensearch.types.deployment_strategy_override.deserialize_json(
                data["DeploymentStrategy"]
            )
        )
    else:
        import typing

        out["deployment_strategy"] = typing.cast(
            "capo_opensearch.types.deployment_strategy_override.DeploymentStrategyOverride",
            "",
        )
    if data.get("ClonedBlueGreenOptions") is not None:
        import capo_opensearch.types.cloned_blue_green_options

        out["cloned_blue_green_options"] = (
            capo_opensearch.types.cloned_blue_green_options.deserialize_json(
                data["ClonedBlueGreenOptions"]
            )
        )
    return out
