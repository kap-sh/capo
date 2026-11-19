"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioned_product_attribute

ProvisionedProductAttributes: TypeAlias = list[
    "capo_service_catalog.types.provisioned_product_attribute.ProvisionedProductAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductAttributes) -> list:
    import capo_service_catalog.types.provisioned_product_attribute

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioned_product_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisionedProductAttributes:
    import capo_service_catalog.types.provisioned_product_attribute

    out: ProvisionedProductAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioned_product_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionedProductAttributes) -> list:
    import capo_service_catalog.types.provisioned_product_attribute

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioned_product_attribute.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ProvisionedProductAttributes:
    import capo_service_catalog.types.provisioned_product_attribute

    out: ProvisionedProductAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioned_product_attribute.deserialize_cbor(
                item
            )
        )
    return out
