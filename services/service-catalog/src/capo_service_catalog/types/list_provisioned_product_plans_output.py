"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListProvisionedProductPlansOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.provisioned_product_plans


class ListProvisionedProductPlansOutput(TypedDict, closed=True):
    provisioned_product_plans: NotRequired[
        "capo_service_catalog.types.provisioned_product_plans.ProvisionedProductPlans"
    ]
    """<p>Information about the plans.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProvisionedProductPlansOutput) -> dict:
    out: dict = {}
    if "provisioned_product_plans" in value:
        import capo_service_catalog.types.provisioned_product_plans

        out["ProvisionedProductPlans"] = (
            capo_service_catalog.types.provisioned_product_plans.serialize_aws_json_1_1(
                value["provisioned_product_plans"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProvisionedProductPlansOutput:
    out: ListProvisionedProductPlansOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductPlans") is not None:
        import capo_service_catalog.types.provisioned_product_plans

        out["provisioned_product_plans"] = (
            capo_service_catalog.types.provisioned_product_plans.deserialize_aws_json_1_1(
                data["ProvisionedProductPlans"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProvisionedProductPlansOutput) -> dict:
    out: dict = {}
    if "provisioned_product_plans" in value:
        import capo_service_catalog.types.provisioned_product_plans

        out["ProvisionedProductPlans"] = (
            capo_service_catalog.types.provisioned_product_plans.serialize_cbor(
                value["provisioned_product_plans"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListProvisionedProductPlansOutput:
    out: ListProvisionedProductPlansOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductPlans") is not None:
        import capo_service_catalog.types.provisioned_product_plans

        out["provisioned_product_plans"] = (
            capo_service_catalog.types.provisioned_product_plans.deserialize_cbor(
                data["ProvisionedProductPlans"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
