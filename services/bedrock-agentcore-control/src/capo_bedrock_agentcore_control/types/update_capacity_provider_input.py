"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateCapacityProviderInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_id
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.updated_description


class UpdateCapacityProviderInput(TypedDict, closed=True):
    capacity_provider_id: (
        "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId"
    )
    """<p>The unique identifier of the capacity provider to update.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
    ]
    """<p>The updated description of the capacity provider.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCapacityProviderInput) -> dict:
    out: dict = {}
    if "description" in value:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.serialize_json(
                value["description"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateCapacityProviderInput:
    out: UpdateCapacityProviderInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        import capo_bedrock_agentcore_control.types.updated_description

        out["description"] = (
            capo_bedrock_agentcore_control.types.updated_description.deserialize_json(
                data["description"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
