"""Generated from Smithy shape ``com.amazonaws.fms#CustomerPolicyScopeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.customer_policy_scope_id_list
    import capo_fms.types.customer_policy_scope_id_type

CustomerPolicyScopeMap: TypeAlias = dict[
    "capo_fms.types.customer_policy_scope_id_type.CustomerPolicyScopeIdType",
    "capo_fms.types.customer_policy_scope_id_list.CustomerPolicyScopeIdList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CustomerPolicyScopeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fms.types.customer_policy_scope_id_list
        import capo_fms.types.customer_policy_scope_id_type

        out[
            capo_fms.types.customer_policy_scope_id_type.serialize_aws_json_1_1(key)
        ] = capo_fms.types.customer_policy_scope_id_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerPolicyScopeMap:
    out: CustomerPolicyScopeMap = {}
    for key, value in data.items():
        import capo_fms.types.customer_policy_scope_id_type

        if value is None:
            continue
        import capo_fms.types.customer_policy_scope_id_list

        out[
            capo_fms.types.customer_policy_scope_id_type.deserialize_aws_json_1_1(key)
        ] = capo_fms.types.customer_policy_scope_id_list.deserialize_aws_json_1_1(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: CustomerPolicyScopeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fms.types.customer_policy_scope_id_list
        import capo_fms.types.customer_policy_scope_id_type

        out[capo_fms.types.customer_policy_scope_id_type.serialize_cbor(key)] = (
            capo_fms.types.customer_policy_scope_id_list.serialize_cbor(value)
        )
    return out


def deserialize_cbor(data: dict) -> CustomerPolicyScopeMap:
    out: CustomerPolicyScopeMap = {}
    for key, value in data.items():
        import capo_fms.types.customer_policy_scope_id_type

        if value is None:
            continue
        import capo_fms.types.customer_policy_scope_id_list

        out[capo_fms.types.customer_policy_scope_id_type.deserialize_cbor(key)] = (
            capo_fms.types.customer_policy_scope_id_list.deserialize_cbor(value)
        )
    return out
