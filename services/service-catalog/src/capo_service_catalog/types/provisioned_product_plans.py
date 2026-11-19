"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioned_product_plan_summary

ProvisionedProductPlans: TypeAlias = list[
    "capo_service_catalog.types.provisioned_product_plan_summary.ProvisionedProductPlanSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductPlans) -> list:
    import capo_service_catalog.types.provisioned_product_plan_summary

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioned_product_plan_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisionedProductPlans:
    import capo_service_catalog.types.provisioned_product_plan_summary

    out: ProvisionedProductPlans = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioned_product_plan_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionedProductPlans) -> list:
    import capo_service_catalog.types.provisioned_product_plan_summary

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioned_product_plan_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ProvisionedProductPlans:
    import capo_service_catalog.types.provisioned_product_plan_summary

    out: ProvisionedProductPlans = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioned_product_plan_summary.deserialize_cbor(
                item
            )
        )
    return out
