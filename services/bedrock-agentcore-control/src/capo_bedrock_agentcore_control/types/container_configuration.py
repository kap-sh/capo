"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ContainerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.runtime_container_uri


class ContainerConfiguration(TypedDict, closed=True):
    container_uri: (
        "capo_bedrock_agentcore_control.types.runtime_container_uri.RuntimeContainerUri"
    )
    """<p>The ECR URI of the container.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerConfiguration) -> dict:
    out: dict = {}
    out["containerUri"] = value["container_uri"]
    return out


def deserialize_json(data: dict) -> ContainerConfiguration:
    out: ContainerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("containerUri") is not None:
        out["container_uri"] = data["containerUri"]
    else:
        out["container_uri"] = ""
    return out
