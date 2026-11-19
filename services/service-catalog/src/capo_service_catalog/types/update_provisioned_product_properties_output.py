"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisionedProductPropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id
    import capo_service_catalog.types.provisioned_product_properties
    import capo_service_catalog.types.record_status


class UpdateProvisionedProductPropertiesOutput(TypedDict, closed=True):
    provisioned_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The provisioned product identifier.</p>"""
    provisioned_product_properties: NotRequired[
        "capo_service_catalog.types.provisioned_product_properties.ProvisionedProductProperties"
    ]
    """<p>A map that contains the properties updated.</p>"""
    record_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the record.</p>"""
    status: NotRequired["capo_service_catalog.types.record_status.RecordStatus"]
    """<p>The status of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisionedProductPropertiesOutput) -> dict:
    out: dict = {}
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "provisioned_product_properties" in value:
        import capo_service_catalog.types.provisioned_product_properties

        out["ProvisionedProductProperties"] = (
            capo_service_catalog.types.provisioned_product_properties.serialize_aws_json_1_1(
                value["provisioned_product_properties"]
            )
        )
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "status" in value:
        import capo_service_catalog.types.record_status

        out["Status"] = capo_service_catalog.types.record_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisionedProductPropertiesOutput:
    out: UpdateProvisionedProductPropertiesOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if data.get("ProvisionedProductProperties") is not None:
        import capo_service_catalog.types.provisioned_product_properties

        out["provisioned_product_properties"] = (
            capo_service_catalog.types.provisioned_product_properties.deserialize_aws_json_1_1(
                data["ProvisionedProductProperties"]
            )
        )
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.record_status

        out["status"] = (
            capo_service_catalog.types.record_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProvisionedProductPropertiesOutput) -> dict:
    out: dict = {}
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "provisioned_product_properties" in value:
        import capo_service_catalog.types.provisioned_product_properties

        out["ProvisionedProductProperties"] = (
            capo_service_catalog.types.provisioned_product_properties.serialize_cbor(
                value["provisioned_product_properties"]
            )
        )
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "status" in value:
        import capo_service_catalog.types.record_status

        out["Status"] = capo_service_catalog.types.record_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateProvisionedProductPropertiesOutput:
    out: UpdateProvisionedProductPropertiesOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if data.get("ProvisionedProductProperties") is not None:
        import capo_service_catalog.types.provisioned_product_properties

        out["provisioned_product_properties"] = (
            capo_service_catalog.types.provisioned_product_properties.deserialize_cbor(
                data["ProvisionedProductProperties"]
            )
        )
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.record_status

        out["status"] = capo_service_catalog.types.record_status.deserialize_cbor(
            data["Status"]
        )
    return out
