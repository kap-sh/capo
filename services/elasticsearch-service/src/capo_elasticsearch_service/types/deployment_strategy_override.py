"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeploymentStrategyOverride``."""

from typing import Literal, TypeAlias, cast

"""<p>The deployment strategy override for an operation. The only valid value is <code>ClonedBlueGreen</code>.</p>"""
DeploymentStrategyOverride: TypeAlias = Literal["ClonedBlueGreen",]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategyOverride) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStrategyOverride:
    return cast(DeploymentStrategyOverride, data)
