"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalPreferenceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_invoicing.types.account_id_string
    import capo_invoicing.types.basic_string
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.buyer_domain
    import capo_invoicing.types.procurement_portal_name
    import capo_invoicing.types.procurement_portal_preference_arn_string
    import capo_invoicing.types.procurement_portal_preference_selector
    import capo_invoicing.types.procurement_portal_preference_status
    import capo_invoicing.types.supplier_domain


class ProcurementPortalPreferenceSummary(TypedDict, closed=True):
    aws_account_id: "capo_invoicing.types.account_id_string.AccountIdString"
    """<p>The Amazon Web Services account ID associated with this procurement portal preference summary.</p>"""
    procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the procurement portal preference.</p>"""
    procurement_portal_name: (
        "capo_invoicing.types.procurement_portal_name.ProcurementPortalName"
    )
    """<p>The name of the procurement portal.</p>"""
    buyer_domain: "capo_invoicing.types.buyer_domain.BuyerDomain"
    """<p>The domain identifier for the buyer in the procurement portal.</p>"""
    buyer_identifier: (
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the buyer in the procurement portal.</p>"""
    supplier_domain: "capo_invoicing.types.supplier_domain.SupplierDomain"
    """<p>The domain identifier for the supplier in the procurement portal.</p>"""
    supplier_identifier: (
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the supplier in the procurement portal.</p>"""
    selector: NotRequired[
        "capo_invoicing.types.procurement_portal_preference_selector.ProcurementPortalPreferenceSelector"
    ]
    einvoice_delivery_enabled: "bool"
    """<p>Indicates whether e-invoice delivery is enabled for this procurement portal preference.</p>"""
    purchase_order_retrieval_enabled: "bool"
    """<p>Indicates whether purchase order retrieval is enabled for this procurement portal preference.</p>"""
    marketplace_punch_out_enabled: NotRequired["bool"]
    """<p>Indicates whether Marketplace PunchOut is enabled for this procurement portal preference. Defaults to <code>false</code>.</p>"""
    einvoice_delivery_preference_status: NotRequired[
        "capo_invoicing.types.procurement_portal_preference_status.ProcurementPortalPreferenceStatus"
    ]
    """<p>The current status of the e-invoice delivery preference in this summary.</p>"""
    einvoice_delivery_preference_status_reason: NotRequired[
        "capo_invoicing.types.basic_string.BasicString"
    ]
    """<p>The reason for the current e-invoice delivery preference status in this summary.</p>"""
    purchase_order_retrieval_preference_status: NotRequired[
        "capo_invoicing.types.procurement_portal_preference_status.ProcurementPortalPreferenceStatus"
    ]
    """<p>The current status of the purchase order retrieval preference in this summary.</p>"""
    purchase_order_retrieval_preference_status_reason: NotRequired[
        "capo_invoicing.types.basic_string.BasicString"
    ]
    """<p>The reason for the current purchase order retrieval preference status in this summary.</p>"""
    version: "int"
    """<p>The version number of the procurement portal preference configuration in this summary.</p>"""
    create_date: "datetime.datetime"
    """<p>The date and time when the procurement portal preference was created.</p>"""
    last_update_date: "datetime.datetime"
    """<p>The date and time when the procurement portal preference was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalPreferenceSummary) -> dict:
    out: dict = {}
    out["AwsAccountId"] = value["aws_account_id"]
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    import capo_invoicing.types.procurement_portal_name

    out["ProcurementPortalName"] = (
        capo_invoicing.types.procurement_portal_name.serialize_aws_json_1_0(
            value["procurement_portal_name"]
        )
    )
    import capo_invoicing.types.buyer_domain

    out["BuyerDomain"] = capo_invoicing.types.buyer_domain.serialize_aws_json_1_0(
        value["buyer_domain"]
    )
    out["BuyerIdentifier"] = value["buyer_identifier"]
    import capo_invoicing.types.supplier_domain

    out["SupplierDomain"] = capo_invoicing.types.supplier_domain.serialize_aws_json_1_0(
        value["supplier_domain"]
    )
    out["SupplierIdentifier"] = value["supplier_identifier"]
    if "selector" in value:
        import capo_invoicing.types.procurement_portal_preference_selector

        out["Selector"] = (
            capo_invoicing.types.procurement_portal_preference_selector.serialize_aws_json_1_0(
                value["selector"]
            )
        )
    out["EinvoiceDeliveryEnabled"] = value["einvoice_delivery_enabled"]
    out["PurchaseOrderRetrievalEnabled"] = value["purchase_order_retrieval_enabled"]
    if "marketplace_punch_out_enabled" in value:
        out["MarketplacePunchOutEnabled"] = value["marketplace_punch_out_enabled"]
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
    out["Version"] = value["version"]
    import capo_invoicing.types._prelude.timestamp

    out["CreateDate"] = capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["create_date"]
    )
    import capo_invoicing.types._prelude.timestamp

    out["LastUpdateDate"] = (
        capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_update_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProcurementPortalPreferenceSummary:
    out: ProcurementPortalPreferenceSummary = {}  # type: ignore[typeddict-item]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.aws_account_id required"
        )
    if data.get("ProcurementPortalPreferenceArn") is not None:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.procurement_portal_preference_arn required"
        )
    if data.get("ProcurementPortalName") is not None:
        import capo_invoicing.types.procurement_portal_name

        out["procurement_portal_name"] = (
            capo_invoicing.types.procurement_portal_name.deserialize_aws_json_1_0(
                data["ProcurementPortalName"]
            )
        )
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.procurement_portal_name required"
        )
    if data.get("BuyerDomain") is not None:
        import capo_invoicing.types.buyer_domain

        out["buyer_domain"] = (
            capo_invoicing.types.buyer_domain.deserialize_aws_json_1_0(
                data["BuyerDomain"]
            )
        )
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.buyer_domain required"
        )
    if data.get("BuyerIdentifier") is not None:
        out["buyer_identifier"] = data["BuyerIdentifier"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.buyer_identifier required"
        )
    if data.get("SupplierDomain") is not None:
        import capo_invoicing.types.supplier_domain

        out["supplier_domain"] = (
            capo_invoicing.types.supplier_domain.deserialize_aws_json_1_0(
                data["SupplierDomain"]
            )
        )
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.supplier_domain required"
        )
    if data.get("SupplierIdentifier") is not None:
        out["supplier_identifier"] = data["SupplierIdentifier"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.supplier_identifier required"
        )
    if data.get("Selector") is not None:
        import capo_invoicing.types.procurement_portal_preference_selector

        out["selector"] = (
            capo_invoicing.types.procurement_portal_preference_selector.deserialize_aws_json_1_0(
                data["Selector"]
            )
        )
    if data.get("EinvoiceDeliveryEnabled") is not None:
        out["einvoice_delivery_enabled"] = data["EinvoiceDeliveryEnabled"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.einvoice_delivery_enabled required"
        )
    if data.get("PurchaseOrderRetrievalEnabled") is not None:
        out["purchase_order_retrieval_enabled"] = data["PurchaseOrderRetrievalEnabled"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.purchase_order_retrieval_enabled required"
        )
    if data.get("MarketplacePunchOutEnabled") is not None:
        out["marketplace_punch_out_enabled"] = data["MarketplacePunchOutEnabled"]
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
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.version required"
        )
    if data.get("CreateDate") is not None:
        import capo_invoicing.types._prelude.timestamp

        out["create_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreateDate"]
            )
        )
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.create_date required"
        )
    if data.get("LastUpdateDate") is not None:
        import capo_invoicing.types._prelude.timestamp

        out["last_update_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "ProcurementPortalPreferenceSummary.last_update_date required"
        )
    return out
