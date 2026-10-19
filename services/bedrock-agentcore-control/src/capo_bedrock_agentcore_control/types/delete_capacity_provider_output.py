"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteCapacityProviderOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_id
    import capo_bedrock_agentcore_control.types.capacity_provider_status


class DeleteCapacityProviderOutput(TypedDict, closed=True):
    capacity_provider_id: (
        "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId"
    )
    """<p>The unique identifier of the deleted capacity provider.</p>"""
    status: "capo_bedrock_agentcore_control.types.capacity_provider_status.CapacityProviderStatus"
    """<p>The current status of the capacity provider. For possible values, see <code>CapacityProviderStatus</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCapacityProviderOutput) -> dict:
    out: dict = {}
    out["capacityProviderId"] = value["capacity_provider_id"]
    import capo_bedrock_agentcore_control.types.capacity_provider_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.capacity_provider_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteCapacityProviderOutput:
    out: DeleteCapacityProviderOutput = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviderId") is not None:
        out["capacity_provider_id"] = data["capacityProviderId"]
    else:
        out["capacity_provider_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.capacity_provider_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.capacity_provider_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.capacity_provider_status.CapacityProviderStatus",
            "",
        )
    return out
