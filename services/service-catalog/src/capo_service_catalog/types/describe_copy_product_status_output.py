"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeCopyProductStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.copy_product_status
    import capo_service_catalog.types.id
    import capo_service_catalog.types.status_detail


class DescribeCopyProductStatusOutput(TypedDict, closed=True):
    copy_product_status: NotRequired[
        "capo_service_catalog.types.copy_product_status.CopyProductStatus"
    ]
    """<p>The status of the copy product operation.</p>"""
    target_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the copied product.</p>"""
    status_detail: NotRequired["capo_service_catalog.types.status_detail.StatusDetail"]
    """<p>The status message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCopyProductStatusOutput) -> dict:
    out: dict = {}
    if "copy_product_status" in value:
        import capo_service_catalog.types.copy_product_status

        out["CopyProductStatus"] = (
            capo_service_catalog.types.copy_product_status.serialize_aws_json_1_1(
                value["copy_product_status"]
            )
        )
    if "target_product_id" in value:
        out["TargetProductId"] = value["target_product_id"]
    if "status_detail" in value:
        out["StatusDetail"] = value["status_detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCopyProductStatusOutput:
    out: DescribeCopyProductStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("CopyProductStatus") is not None:
        import capo_service_catalog.types.copy_product_status

        out["copy_product_status"] = (
            capo_service_catalog.types.copy_product_status.deserialize_aws_json_1_1(
                data["CopyProductStatus"]
            )
        )
    if data.get("TargetProductId") is not None:
        out["target_product_id"] = data["TargetProductId"]
    if data.get("StatusDetail") is not None:
        out["status_detail"] = data["StatusDetail"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeCopyProductStatusOutput) -> dict:
    out: dict = {}
    if "copy_product_status" in value:
        import capo_service_catalog.types.copy_product_status

        out["CopyProductStatus"] = (
            capo_service_catalog.types.copy_product_status.serialize_cbor(
                value["copy_product_status"]
            )
        )
    if "target_product_id" in value:
        out["TargetProductId"] = value["target_product_id"]
    if "status_detail" in value:
        out["StatusDetail"] = value["status_detail"]
    return out


def deserialize_cbor(data: dict) -> DescribeCopyProductStatusOutput:
    out: DescribeCopyProductStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("CopyProductStatus") is not None:
        import capo_service_catalog.types.copy_product_status

        out["copy_product_status"] = (
            capo_service_catalog.types.copy_product_status.deserialize_cbor(
                data["CopyProductStatus"]
            )
        )
    if data.get("TargetProductId") is not None:
        out["target_product_id"] = data["TargetProductId"]
    if data.get("StatusDetail") is not None:
        out["status_detail"] = data["StatusDetail"]
    return out
