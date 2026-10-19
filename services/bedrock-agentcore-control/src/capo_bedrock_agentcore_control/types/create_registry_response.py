"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.registry_arn


class CreateRegistryResponse(TypedDict, closed=True):
    registry_arn: "capo_bedrock_agentcore_control.types.registry_arn.RegistryArn"
    """<p>The Amazon Resource Name (ARN) of the created registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryResponse) -> dict:
    out: dict = {}
    out["registryArn"] = value["registry_arn"]
    return out


def deserialize_json(data: dict) -> CreateRegistryResponse:
    out: CreateRegistryResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    else:
        out["registry_arn"] = ""
    return out
