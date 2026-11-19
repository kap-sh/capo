"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ExecuteProvisionedProductPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.record_detail


class ExecuteProvisionedProductPlanOutput(TypedDict, closed=True):
    record_detail: NotRequired["capo_service_catalog.types.record_detail.RecordDetail"]
    """<p>Information about the result of provisioning the product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteProvisionedProductPlanOutput) -> dict:
    out: dict = {}
    if "record_detail" in value:
        import capo_service_catalog.types.record_detail

        out["RecordDetail"] = (
            capo_service_catalog.types.record_detail.serialize_aws_json_1_1(
                value["record_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteProvisionedProductPlanOutput:
    out: ExecuteProvisionedProductPlanOutput = {}  # type: ignore[typeddict-item]
    if data.get("RecordDetail") is not None:
        import capo_service_catalog.types.record_detail

        out["record_detail"] = (
            capo_service_catalog.types.record_detail.deserialize_aws_json_1_1(
                data["RecordDetail"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecuteProvisionedProductPlanOutput) -> dict:
    out: dict = {}
    if "record_detail" in value:
        import capo_service_catalog.types.record_detail

        out["RecordDetail"] = capo_service_catalog.types.record_detail.serialize_cbor(
            value["record_detail"]
        )
    return out


def deserialize_cbor(data: dict) -> ExecuteProvisionedProductPlanOutput:
    out: ExecuteProvisionedProductPlanOutput = {}  # type: ignore[typeddict-item]
    if data.get("RecordDetail") is not None:
        import capo_service_catalog.types.record_detail

        out["record_detail"] = (
            capo_service_catalog.types.record_detail.deserialize_cbor(
                data["RecordDetail"]
            )
        )
    return out
