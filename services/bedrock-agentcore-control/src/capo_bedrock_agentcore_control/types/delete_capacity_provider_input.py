"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteCapacityProviderInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_id
    import capo_bedrock_agentcore_control.types.client_token


class DeleteCapacityProviderInput(TypedDict, closed=True):
    capacity_provider_id: (
        "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId"
    )
    """<p>The unique identifier of the capacity provider to delete.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCapacityProviderInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCapacityProviderInput:
    out: DeleteCapacityProviderInput = {}  # type: ignore[typeddict-item]
    return out
