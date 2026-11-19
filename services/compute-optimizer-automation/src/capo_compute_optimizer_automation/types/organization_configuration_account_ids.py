"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#OrganizationConfigurationAccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.account_id

OrganizationConfigurationAccountIds: TypeAlias = list[
    "capo_compute_optimizer_automation.types.account_id.AccountId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OrganizationConfigurationAccountIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> OrganizationConfigurationAccountIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationConfigurationAccountIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> OrganizationConfigurationAccountIds:
    return [item for item in data if item is not None]
