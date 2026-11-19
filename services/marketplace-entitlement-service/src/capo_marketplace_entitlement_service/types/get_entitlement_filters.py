"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#GetEntitlementFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_entitlement_service.types.filter_value_list
    import capo_marketplace_entitlement_service.types.get_entitlement_filter_name

GetEntitlementFilters: TypeAlias = dict[
    "capo_marketplace_entitlement_service.types.get_entitlement_filter_name.GetEntitlementFilterName",
    "capo_marketplace_entitlement_service.types.filter_value_list.FilterValueList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: GetEntitlementFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_marketplace_entitlement_service.types.filter_value_list
        import capo_marketplace_entitlement_service.types.get_entitlement_filter_name

        out[
            capo_marketplace_entitlement_service.types.get_entitlement_filter_name.serialize_aws_json_1_1(
                key
            )
        ] = capo_marketplace_entitlement_service.types.filter_value_list.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntitlementFilters:
    out: GetEntitlementFilters = {}
    for key, value in data.items():
        import capo_marketplace_entitlement_service.types.get_entitlement_filter_name

        if value is None:
            continue
        import capo_marketplace_entitlement_service.types.filter_value_list

        out[
            capo_marketplace_entitlement_service.types.get_entitlement_filter_name.deserialize_aws_json_1_1(
                key
            )
        ] = capo_marketplace_entitlement_service.types.filter_value_list.deserialize_aws_json_1_1(
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: GetEntitlementFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_marketplace_entitlement_service.types.filter_value_list
        import capo_marketplace_entitlement_service.types.get_entitlement_filter_name

        out[
            capo_marketplace_entitlement_service.types.get_entitlement_filter_name.serialize_cbor(
                key
            )
        ] = capo_marketplace_entitlement_service.types.filter_value_list.serialize_cbor(
            value
        )
    return out


def deserialize_cbor(data: dict) -> GetEntitlementFilters:
    out: GetEntitlementFilters = {}
    for key, value in data.items():
        import capo_marketplace_entitlement_service.types.get_entitlement_filter_name

        if value is None:
            continue
        import capo_marketplace_entitlement_service.types.filter_value_list

        out[
            capo_marketplace_entitlement_service.types.get_entitlement_filter_name.deserialize_cbor(
                key
            )
        ] = capo_marketplace_entitlement_service.types.filter_value_list.deserialize_cbor(
            value
        )
    return out
