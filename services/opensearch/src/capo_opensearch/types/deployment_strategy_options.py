"""Generated from Smithy shape ``com.amazonaws.opensearch#DeploymentStrategyOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.deployment_strategy


class DeploymentStrategyOptions(TypedDict, closed=True):
    deployment_strategy: "capo_opensearch.types.deployment_strategy.DeploymentStrategy"
    """<p>Specifies the deployment strategy for the domain. Valid values are <code>Default</code> and <code>CapacityOptimized</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategyOptions) -> dict:
    out: dict = {}
    import capo_opensearch.types.deployment_strategy

    out["DeploymentStrategy"] = (
        capo_opensearch.types.deployment_strategy.serialize_json(
            value["deployment_strategy"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeploymentStrategyOptions:
    out: DeploymentStrategyOptions = {}  # type: ignore[typeddict-item]
    if data.get("DeploymentStrategy") is not None:
        import capo_opensearch.types.deployment_strategy

        out["deployment_strategy"] = (
            capo_opensearch.types.deployment_strategy.deserialize_json(
                data["DeploymentStrategy"]
            )
        )
    else:
        import typing

        out["deployment_strategy"] = typing.cast(
            "capo_opensearch.types.deployment_strategy.DeploymentStrategy", ""
        )
    return out
