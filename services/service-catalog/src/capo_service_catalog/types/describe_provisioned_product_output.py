"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisionedProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.cloud_watch_dashboards
    import capo_service_catalog.types.provisioned_product_detail


class DescribeProvisionedProductOutput(TypedDict, closed=True):
    provisioned_product_detail: NotRequired[
        "capo_service_catalog.types.provisioned_product_detail.ProvisionedProductDetail"
    ]
    """<p>Information about the provisioned product.</p>"""
    cloud_watch_dashboards: NotRequired[
        "capo_service_catalog.types.cloud_watch_dashboards.CloudWatchDashboards"
    ]
    """<p>Any CloudWatch dashboards that were created when provisioning the product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisionedProductOutput) -> dict:
    out: dict = {}
    if "provisioned_product_detail" in value:
        import capo_service_catalog.types.provisioned_product_detail

        out["ProvisionedProductDetail"] = (
            capo_service_catalog.types.provisioned_product_detail.serialize_aws_json_1_1(
                value["provisioned_product_detail"]
            )
        )
    if "cloud_watch_dashboards" in value:
        import capo_service_catalog.types.cloud_watch_dashboards

        out["CloudWatchDashboards"] = (
            capo_service_catalog.types.cloud_watch_dashboards.serialize_aws_json_1_1(
                value["cloud_watch_dashboards"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisionedProductOutput:
    out: DescribeProvisionedProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductDetail") is not None:
        import capo_service_catalog.types.provisioned_product_detail

        out["provisioned_product_detail"] = (
            capo_service_catalog.types.provisioned_product_detail.deserialize_aws_json_1_1(
                data["ProvisionedProductDetail"]
            )
        )
    if data.get("CloudWatchDashboards") is not None:
        import capo_service_catalog.types.cloud_watch_dashboards

        out["cloud_watch_dashboards"] = (
            capo_service_catalog.types.cloud_watch_dashboards.deserialize_aws_json_1_1(
                data["CloudWatchDashboards"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProvisionedProductOutput) -> dict:
    out: dict = {}
    if "provisioned_product_detail" in value:
        import capo_service_catalog.types.provisioned_product_detail

        out["ProvisionedProductDetail"] = (
            capo_service_catalog.types.provisioned_product_detail.serialize_cbor(
                value["provisioned_product_detail"]
            )
        )
    if "cloud_watch_dashboards" in value:
        import capo_service_catalog.types.cloud_watch_dashboards

        out["CloudWatchDashboards"] = (
            capo_service_catalog.types.cloud_watch_dashboards.serialize_cbor(
                value["cloud_watch_dashboards"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeProvisionedProductOutput:
    out: DescribeProvisionedProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductDetail") is not None:
        import capo_service_catalog.types.provisioned_product_detail

        out["provisioned_product_detail"] = (
            capo_service_catalog.types.provisioned_product_detail.deserialize_cbor(
                data["ProvisionedProductDetail"]
            )
        )
    if data.get("CloudWatchDashboards") is not None:
        import capo_service_catalog.types.cloud_watch_dashboards

        out["cloud_watch_dashboards"] = (
            capo_service_catalog.types.cloud_watch_dashboards.deserialize_cbor(
                data["CloudWatchDashboards"]
            )
        )
    return out
