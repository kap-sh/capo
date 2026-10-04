"""Generated from Smithy shape ``com.amazonaws.invoicing#CreateProcurementPortalPreferenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.buyer_domain
    import capo_invoicing.types.contacts
    import capo_invoicing.types.einvoice_delivery_preference
    import capo_invoicing.types.marketplace_punch_out_preference
    import capo_invoicing.types.procurement_portal_name
    import capo_invoicing.types.procurement_portal_preference_selector
    import capo_invoicing.types.resource_tag_list
    import capo_invoicing.types.sensitive_basic_string_without_space
    import capo_invoicing.types.supplier_domain
    import capo_invoicing.types.test_env_preference_input


class CreateProcurementPortalPreferenceRequest(TypedDict, closed=True):
    procurement_portal_name: (
        "capo_invoicing.types.procurement_portal_name.ProcurementPortalName"
    )
    """<p>The name of the procurement portal.</p>"""
    buyer_domain: "capo_invoicing.types.buyer_domain.BuyerDomain"
    """<p>The domain identifier for the buyer in the procurement portal.</p>"""
    buyer_identifier: (
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the buyer in the procurement portal. </p>"""
    supplier_domain: "capo_invoicing.types.supplier_domain.SupplierDomain"
    """<p>The domain identifier for the supplier in the procurement portal.</p>"""
    supplier_identifier: (
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the supplier in the procurement portal.</p>"""
    selector: NotRequired[
        "capo_invoicing.types.procurement_portal_preference_selector.ProcurementPortalPreferenceSelector"
    ]
    procurement_portal_shared_secret: NotRequired[
        "capo_invoicing.types.sensitive_basic_string_without_space.SensitiveBasicStringWithoutSpace"
    ]
    """<p>The shared secret or authentication credential used to establish secure communication with the procurement portal. This value must be encrypted at rest.</p>"""
    procurement_portal_instance_endpoint: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The endpoint URL where e-invoices will be delivered to the procurement portal. Must be a valid HTTPS URL.</p>"""
    test_env_preference: NotRequired[
        "capo_invoicing.types.test_env_preference_input.TestEnvPreferenceInput"
    ]
    """<p>Configuration settings for the test environment of the procurement portal. Includes test credentials and endpoints that are used for validation before production deployment.</p>"""
    einvoice_delivery_enabled: "bool"
    """<p>Indicates whether e-invoice delivery is enabled for this procurement portal preference. Set to true to enable e-invoice delivery, false to disable.</p>"""
    einvoice_delivery_preference: NotRequired[
        "capo_invoicing.types.einvoice_delivery_preference.EinvoiceDeliveryPreference"
    ]
    """<p>Specifies the e-invoice delivery configuration including document types, attachment types, and customization settings for the portal.</p>"""
    purchase_order_retrieval_enabled: "bool"
    """<p>Indicates whether purchase order retrieval is enabled for this procurement portal preference. Set to true to enable PO retrieval, false to disable.</p>"""
    marketplace_punch_out_enabled: NotRequired["bool"]
    """Defaults to false if not provided."""
    marketplace_punch_out_preference: NotRequired[
        "capo_invoicing.types.marketplace_punch_out_preference.MarketplacePunchOutPreference"
    ]
    """Required for Coupa when MarketplacePunchOutEnabled is true."""
    contacts: "capo_invoicing.types.contacts.Contacts"
    """<p>List of contact information for portal administrators and technical contacts responsible for the e-invoice integration.</p>"""
    resource_tags: NotRequired["capo_invoicing.types.resource_tag_list.ResourceTagList"]
    """<p>The tags to apply to this procurement portal preference resource. Each tag consists of a key and an optional value.</p>"""
    client_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProcurementPortalPreferenceRequest) -> dict:
    out: dict = {}
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
    if "procurement_portal_shared_secret" in value:
        out["ProcurementPortalSharedSecret"] = value["procurement_portal_shared_secret"]
    if "procurement_portal_instance_endpoint" in value:
        out["ProcurementPortalInstanceEndpoint"] = value[
            "procurement_portal_instance_endpoint"
        ]
    if "test_env_preference" in value:
        import capo_invoicing.types.test_env_preference_input

        out["TestEnvPreference"] = (
            capo_invoicing.types.test_env_preference_input.serialize_aws_json_1_0(
                value["test_env_preference"]
            )
        )
    out["EinvoiceDeliveryEnabled"] = value["einvoice_delivery_enabled"]
    if "einvoice_delivery_preference" in value:
        import capo_invoicing.types.einvoice_delivery_preference

        out["EinvoiceDeliveryPreference"] = (
            capo_invoicing.types.einvoice_delivery_preference.serialize_aws_json_1_0(
                value["einvoice_delivery_preference"]
            )
        )
    out["PurchaseOrderRetrievalEnabled"] = value["purchase_order_retrieval_enabled"]
    if "marketplace_punch_out_enabled" in value:
        out["MarketplacePunchOutEnabled"] = value["marketplace_punch_out_enabled"]
    if "marketplace_punch_out_preference" in value:
        import capo_invoicing.types.marketplace_punch_out_preference

        out["MarketplacePunchOutPreference"] = (
            capo_invoicing.types.marketplace_punch_out_preference.serialize_aws_json_1_0(
                value["marketplace_punch_out_preference"]
            )
        )
    import capo_invoicing.types.contacts

    out["Contacts"] = capo_invoicing.types.contacts.serialize_aws_json_1_0(
        value["contacts"]
    )
    if "resource_tags" in value:
        import capo_invoicing.types.resource_tag_list

        out["ResourceTags"] = (
            capo_invoicing.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProcurementPortalPreferenceRequest:
    out: CreateProcurementPortalPreferenceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProcurementPortalName") is not None:
        import capo_invoicing.types.procurement_portal_name

        out["procurement_portal_name"] = (
            capo_invoicing.types.procurement_portal_name.deserialize_aws_json_1_0(
                data["ProcurementPortalName"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProcurementPortalPreferenceRequest.procurement_portal_name required"
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
            "CreateProcurementPortalPreferenceRequest.buyer_domain required"
        )
    if data.get("BuyerIdentifier") is not None:
        out["buyer_identifier"] = data["BuyerIdentifier"]
    else:
        raise DeserializationError(
            "CreateProcurementPortalPreferenceRequest.buyer_identifier required"
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
            "CreateProcurementPortalPreferenceRequest.supplier_domain required"
        )
    if data.get("SupplierIdentifier") is not None:
        out["supplier_identifier"] = data["SupplierIdentifier"]
    else:
        raise DeserializationError(
            "CreateProcurementPortalPreferenceRequest.supplier_identifier required"
        )
    if data.get("Selector") is not None:
        import capo_invoicing.types.procurement_portal_preference_selector

        out["selector"] = (
            capo_invoicing.types.procurement_portal_preference_selector.deserialize_aws_json_1_0(
                data["Selector"]
            )
        )
    if data.get("ProcurementPortalSharedSecret") is not None:
        out["procurement_portal_shared_secret"] = data["ProcurementPortalSharedSecret"]
    if data.get("ProcurementPortalInstanceEndpoint") is not None:
        out["procurement_portal_instance_endpoint"] = data[
            "ProcurementPortalInstanceEndpoint"
        ]
    if data.get("TestEnvPreference") is not None:
        import capo_invoicing.types.test_env_preference_input

        out["test_env_preference"] = (
            capo_invoicing.types.test_env_preference_input.deserialize_aws_json_1_0(
                data["TestEnvPreference"]
            )
        )
    if data.get("EinvoiceDeliveryEnabled") is not None:
        out["einvoice_delivery_enabled"] = data["EinvoiceDeliveryEnabled"]
    else:
        raise DeserializationError(
            "CreateProcurementPortalPreferenceRequest.einvoice_delivery_enabled required"
        )
    if data.get("EinvoiceDeliveryPreference") is not None:
        import capo_invoicing.types.einvoice_delivery_preference

        out["einvoice_delivery_preference"] = (
            capo_invoicing.types.einvoice_delivery_preference.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryPreference"]
            )
        )
    if data.get("PurchaseOrderRetrievalEnabled") is not None:
        out["purchase_order_retrieval_enabled"] = data["PurchaseOrderRetrievalEnabled"]
    else:
        raise DeserializationError(
            "CreateProcurementPortalPreferenceRequest.purchase_order_retrieval_enabled required"
        )
    if data.get("MarketplacePunchOutEnabled") is not None:
        out["marketplace_punch_out_enabled"] = data["MarketplacePunchOutEnabled"]
    if data.get("MarketplacePunchOutPreference") is not None:
        import capo_invoicing.types.marketplace_punch_out_preference

        out["marketplace_punch_out_preference"] = (
            capo_invoicing.types.marketplace_punch_out_preference.deserialize_aws_json_1_0(
                data["MarketplacePunchOutPreference"]
            )
        )
    if data.get("Contacts") is not None:
        import capo_invoicing.types.contacts

        out["contacts"] = capo_invoicing.types.contacts.deserialize_aws_json_1_0(
            data["Contacts"]
        )
    else:
        raise DeserializationError(
            "CreateProcurementPortalPreferenceRequest.contacts required"
        )
    if data.get("ResourceTags") is not None:
        import capo_invoicing.types.resource_tag_list

        out["resource_tags"] = (
            capo_invoicing.types.resource_tag_list.deserialize_aws_json_1_0(
                data["ResourceTags"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
