"""Generated from Smithy shape ``com.amazonaws.continuum#GetResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.resource_policy_target_arn


class GetResourcePolicyInput(TypedDict, closed=True):
    arn: "capo_continuum.types.resource_policy_target_arn.ResourcePolicyTargetArn"
    """The ARN of a resource in the caller's account."""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyInput:
    out: GetResourcePolicyInput = {}  # type: ignore[typeddict-item]
    return out
