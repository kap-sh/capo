"""Generated from Smithy shape ``com.amazonaws.continuum#GetCollectorDataAccessAuthorizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.aws_account_id
    import capo_continuum.types.collector_id
    import capo_continuum.types.environment_arn


class GetCollectorDataAccessAuthorizationInput(TypedDict, closed=True):
    account_id: "capo_continuum.types.aws_account_id.AwsAccountId"
    """The AWS account that owns the Collector."""
    collector_id: "capo_continuum.types.collector_id.CollectorId"
    """The unique identifier of the Collector."""
    environment_arn: NotRequired["capo_continuum.types.environment_arn.EnvironmentArn"]
    """The full ARN of the Environment requesting the Collector's data. The Environment must be in the caller's account. Continuum supplies this value as the continuum:EnvironmentArn condition key."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollectorDataAccessAuthorizationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollectorDataAccessAuthorizationInput:
    out: GetCollectorDataAccessAuthorizationInput = {}  # type: ignore[typeddict-item]
    return out
