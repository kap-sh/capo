"""Generated from Smithy shape ``com.amazonaws.fms#CustomerPolicyScopeIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.customer_policy_scope_id

CustomerPolicyScopeIdList: TypeAlias = list[
    "capo_fms.types.customer_policy_scope_id.CustomerPolicyScopeId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerPolicyScopeIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomerPolicyScopeIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomerPolicyScopeIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CustomerPolicyScopeIdList:
    return [item for item in data if item is not None]
