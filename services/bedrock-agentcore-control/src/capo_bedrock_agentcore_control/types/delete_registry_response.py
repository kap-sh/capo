"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.registry_status


class DeleteRegistryResponse(TypedDict, closed=True):
    status: "capo_bedrock_agentcore_control.types.registry_status.RegistryStatus"
    """<p>The current status of the registry, set to <code>DELETING</code> when deletion is initiated. For a list of all possible registry statuses, see the <code>RegistryStatus</code> data type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRegistryResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.registry_status

    out["status"] = capo_bedrock_agentcore_control.types.registry_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteRegistryResponse:
    out: DeleteRegistryResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.registry_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.registry_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.registry_status.RegistryStatus", ""
        )
    return out
