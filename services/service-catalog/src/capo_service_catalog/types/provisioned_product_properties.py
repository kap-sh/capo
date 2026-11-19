"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.property_key
    import capo_service_catalog.types.property_value

ProvisionedProductProperties: TypeAlias = dict[
    "capo_service_catalog.types.property_key.PropertyKey",
    "capo_service_catalog.types.property_value.PropertyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ProvisionedProductProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_catalog.types.property_key

        out[capo_service_catalog.types.property_key.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedProductProperties:
    out: ProvisionedProductProperties = {}
    for key, value in data.items():
        import capo_service_catalog.types.property_key

        if value is None:
            continue
        out[capo_service_catalog.types.property_key.deserialize_aws_json_1_1(key)] = (
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ProvisionedProductProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_catalog.types.property_key

        out[capo_service_catalog.types.property_key.serialize_cbor(key)] = value
    return out


def deserialize_cbor(data: dict) -> ProvisionedProductProperties:
    out: ProvisionedProductProperties = {}
    for key, value in data.items():
        import capo_service_catalog.types.property_key

        if value is None:
            continue
        out[capo_service_catalog.types.property_key.deserialize_cbor(key)] = value
    return out
