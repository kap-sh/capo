"""Generated from Smithy shape ``com.amazonaws.invoicing#UpdateProcurementPortalPreferenceStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.procurement_portal_preference_arn_string
    import capo_invoicing.types.procurement_portal_preference_status


class UpdateProcurementPortalPreferenceStatusRequest(TypedDict, closed=True):
    procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the procurement portal preference to update.</p>"""
    einvoice_delivery_preference_status: NotRequired[
        "capo_invoicing.types.procurement_portal_preference_status.ProcurementPortalPreferenceStatus"
    ]
    """<p>The updated status of the e-invoice delivery preference.</p>"""
    einvoice_delivery_preference_status_reason: NotRequired[
        "capo_invoicing.types.basic_string.BasicString"
    ]
    """<p>The reason for the e-invoice delivery preference status update, providing context for the change.</p>"""
    purchase_order_retrieval_preference_status: NotRequired[
        "capo_invoicing.types.procurement_portal_preference_status.ProcurementPortalPreferenceStatus"
    ]
    """<p>The updated status of the purchase order retrieval preference.</p>"""
    purchase_order_retrieval_preference_status_reason: NotRequired[
        "capo_invoicing.types.basic_string.BasicString"
    ]
    """<p>The reason for the purchase order retrieval preference status update, providing context for the change.</p>"""
    client_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateProcurementPortalPreferenceStatusRequest,
) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    if "einvoice_delivery_preference_status" in value:
        import capo_invoicing.types.procurement_portal_preference_status

        out["EinvoiceDeliveryPreferenceStatus"] = (
            capo_invoicing.types.procurement_portal_preference_status.serialize_aws_json_1_0(
                value["einvoice_delivery_preference_status"]
            )
        )
    if "einvoice_delivery_preference_status_reason" in value:
        out["EinvoiceDeliveryPreferenceStatusReason"] = value[
            "einvoice_delivery_preference_status_reason"
        ]
    if "purchase_order_retrieval_preference_status" in value:
        import capo_invoicing.types.procurement_portal_preference_status

        out["PurchaseOrderRetrievalPreferenceStatus"] = (
            capo_invoicing.types.procurement_portal_preference_status.serialize_aws_json_1_0(
                value["purchase_order_retrieval_preference_status"]
            )
        )
    if "purchase_order_retrieval_preference_status_reason" in value:
        out["PurchaseOrderRetrievalPreferenceStatusReason"] = value[
            "purchase_order_retrieval_preference_status_reason"
        ]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateProcurementPortalPreferenceStatusRequest:
    out: UpdateProcurementPortalPreferenceStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProcurementPortalPreferenceArn") is not None:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        out["procurement_portal_preference_arn"] = ""
    if data.get("EinvoiceDeliveryPreferenceStatus") is not None:
        import capo_invoicing.types.procurement_portal_preference_status

        out["einvoice_delivery_preference_status"] = (
            capo_invoicing.types.procurement_portal_preference_status.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryPreferenceStatus"]
            )
        )
    if data.get("EinvoiceDeliveryPreferenceStatusReason") is not None:
        out["einvoice_delivery_preference_status_reason"] = data[
            "EinvoiceDeliveryPreferenceStatusReason"
        ]
    if data.get("PurchaseOrderRetrievalPreferenceStatus") is not None:
        import capo_invoicing.types.procurement_portal_preference_status

        out["purchase_order_retrieval_preference_status"] = (
            capo_invoicing.types.procurement_portal_preference_status.deserialize_aws_json_1_0(
                data["PurchaseOrderRetrievalPreferenceStatus"]
            )
        )
    if data.get("PurchaseOrderRetrievalPreferenceStatusReason") is not None:
        out["purchase_order_retrieval_preference_status_reason"] = data[
            "PurchaseOrderRetrievalPreferenceStatusReason"
        ]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
