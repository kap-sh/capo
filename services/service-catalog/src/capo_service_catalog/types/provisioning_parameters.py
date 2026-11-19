"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_parameter

ProvisioningParameters: TypeAlias = list[
    "capo_service_catalog.types.provisioning_parameter.ProvisioningParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningParameters) -> list:
    import capo_service_catalog.types.provisioning_parameter

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningParameters:
    import capo_service_catalog.types.provisioning_parameter

    out: ProvisioningParameters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningParameters) -> list:
    import capo_service_catalog.types.provisioning_parameter

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_parameter.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ProvisioningParameters:
    import capo_service_catalog.types.provisioning_parameter

    out: ProvisioningParameters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_parameter.deserialize_cbor(item)
        )
    return out
