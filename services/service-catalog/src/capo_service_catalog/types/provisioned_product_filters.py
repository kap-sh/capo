"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioned_product_view_filter_by
    import capo_service_catalog.types.provisioned_product_view_filter_values

ProvisionedProductFilters: TypeAlias = dict[
    "capo_service_catalog.types.provisioned_product_view_filter_by.ProvisionedProductViewFilterBy",
    "capo_service_catalog.types.provisioned_product_view_filter_values.ProvisionedProductViewFilterValues",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ProvisionedProductFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_catalog.types.provisioned_product_view_filter_by
        import capo_service_catalog.types.provisioned_product_view_filter_values

        out[
            capo_service_catalog.types.provisioned_product_view_filter_by.serialize_aws_json_1_1(
                key
            )
        ] = capo_service_catalog.types.provisioned_product_view_filter_values.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedProductFilters:
    out: ProvisionedProductFilters = {}
    for key, value in data.items():
        import capo_service_catalog.types.provisioned_product_view_filter_by

        if value is None:
            continue
        import capo_service_catalog.types.provisioned_product_view_filter_values

        out[
            capo_service_catalog.types.provisioned_product_view_filter_by.deserialize_aws_json_1_1(
                key
            )
        ] = capo_service_catalog.types.provisioned_product_view_filter_values.deserialize_aws_json_1_1(
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ProvisionedProductFilters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_catalog.types.provisioned_product_view_filter_by
        import capo_service_catalog.types.provisioned_product_view_filter_values

        out[
            capo_service_catalog.types.provisioned_product_view_filter_by.serialize_cbor(
                key
            )
        ] = capo_service_catalog.types.provisioned_product_view_filter_values.serialize_cbor(
            value
        )
    return out


def deserialize_cbor(data: dict) -> ProvisionedProductFilters:
    out: ProvisionedProductFilters = {}
    for key, value in data.items():
        import capo_service_catalog.types.provisioned_product_view_filter_by

        if value is None:
            continue
        import capo_service_catalog.types.provisioned_product_view_filter_values

        out[
            capo_service_catalog.types.provisioned_product_view_filter_by.deserialize_cbor(
                key
            )
        ] = capo_service_catalog.types.provisioned_product_view_filter_values.deserialize_cbor(
            value
        )
    return out
