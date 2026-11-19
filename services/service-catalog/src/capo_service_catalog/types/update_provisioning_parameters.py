"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisioningParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.update_provisioning_parameter

UpdateProvisioningParameters: TypeAlias = list[
    "capo_service_catalog.types.update_provisioning_parameter.UpdateProvisioningParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisioningParameters) -> list:
    import capo_service_catalog.types.update_provisioning_parameter

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.update_provisioning_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateProvisioningParameters:
    import capo_service_catalog.types.update_provisioning_parameter

    out: UpdateProvisioningParameters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.update_provisioning_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProvisioningParameters) -> list:
    import capo_service_catalog.types.update_provisioning_parameter

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.update_provisioning_parameter.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> UpdateProvisioningParameters:
    import capo_service_catalog.types.update_provisioning_parameter

    out: UpdateProvisioningParameters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.update_provisioning_parameter.deserialize_cbor(
                item
            )
        )
    return out
