"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisionedProductPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.provisioned_product_plan_details
    import capo_service_catalog.types.resource_changes


class DescribeProvisionedProductPlanOutput(TypedDict, closed=True):
    provisioned_product_plan_details: NotRequired[
        "capo_service_catalog.types.provisioned_product_plan_details.ProvisionedProductPlanDetails"
    ]
    """<p>Information about the plan.</p>"""
    resource_changes: NotRequired[
        "capo_service_catalog.types.resource_changes.ResourceChanges"
    ]
    """<p>Information about the resource changes that will occur when the plan is executed.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisionedProductPlanOutput) -> dict:
    out: dict = {}
    if "provisioned_product_plan_details" in value:
        import capo_service_catalog.types.provisioned_product_plan_details

        out["ProvisionedProductPlanDetails"] = (
            capo_service_catalog.types.provisioned_product_plan_details.serialize_aws_json_1_1(
                value["provisioned_product_plan_details"]
            )
        )
    if "resource_changes" in value:
        import capo_service_catalog.types.resource_changes

        out["ResourceChanges"] = (
            capo_service_catalog.types.resource_changes.serialize_aws_json_1_1(
                value["resource_changes"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisionedProductPlanOutput:
    out: DescribeProvisionedProductPlanOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductPlanDetails") is not None:
        import capo_service_catalog.types.provisioned_product_plan_details

        out["provisioned_product_plan_details"] = (
            capo_service_catalog.types.provisioned_product_plan_details.deserialize_aws_json_1_1(
                data["ProvisionedProductPlanDetails"]
            )
        )
    if data.get("ResourceChanges") is not None:
        import capo_service_catalog.types.resource_changes

        out["resource_changes"] = (
            capo_service_catalog.types.resource_changes.deserialize_aws_json_1_1(
                data["ResourceChanges"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProvisionedProductPlanOutput) -> dict:
    out: dict = {}
    if "provisioned_product_plan_details" in value:
        import capo_service_catalog.types.provisioned_product_plan_details

        out["ProvisionedProductPlanDetails"] = (
            capo_service_catalog.types.provisioned_product_plan_details.serialize_cbor(
                value["provisioned_product_plan_details"]
            )
        )
    if "resource_changes" in value:
        import capo_service_catalog.types.resource_changes

        out["ResourceChanges"] = (
            capo_service_catalog.types.resource_changes.serialize_cbor(
                value["resource_changes"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeProvisionedProductPlanOutput:
    out: DescribeProvisionedProductPlanOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductPlanDetails") is not None:
        import capo_service_catalog.types.provisioned_product_plan_details

        out["provisioned_product_plan_details"] = (
            capo_service_catalog.types.provisioned_product_plan_details.deserialize_cbor(
                data["ProvisionedProductPlanDetails"]
            )
        )
    if data.get("ResourceChanges") is not None:
        import capo_service_catalog.types.resource_changes

        out["resource_changes"] = (
            capo_service_catalog.types.resource_changes.deserialize_cbor(
                data["ResourceChanges"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
