"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_invoicing.types.connection_testing_method
    import capo_invoicing.types.einvoice_delivery_attachment_types
    import capo_invoicing.types.einvoice_delivery_document_types
    import capo_invoicing.types.protocol
    import capo_invoicing.types.purchase_order_data_sources


class EinvoiceDeliveryPreference(TypedDict, closed=True):
    einvoice_delivery_document_types: "capo_invoicing.types.einvoice_delivery_document_types.EinvoiceDeliveryDocumentTypes"
    """<p>The types of e-invoice documents to be delivered.</p>"""
    einvoice_delivery_attachment_types: NotRequired[
        "capo_invoicing.types.einvoice_delivery_attachment_types.EinvoiceDeliveryAttachmentTypes"
    ]
    """<p>The types of attachments to include with the e-invoice delivery.</p>"""
    protocol: "capo_invoicing.types.protocol.Protocol"
    """<p>The communication protocol to use for e-invoice delivery.</p>"""
    purchase_order_data_sources: (
        "capo_invoicing.types.purchase_order_data_sources.PurchaseOrderDataSources"
    )
    """<p>The sources of purchase order data to use for e-invoice generation and delivery.</p>"""
    connection_testing_method: (
        "capo_invoicing.types.connection_testing_method.ConnectionTestingMethod"
    )
    """<p>The method to use for testing the connection to the procurement portal.</p>"""
    einvoice_delivery_activation_date: "datetime.datetime"
    """<p>The date when e-invoice delivery should be activated for this preference.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EinvoiceDeliveryPreference) -> dict:
    out: dict = {}
    import capo_invoicing.types.einvoice_delivery_document_types

    out["EinvoiceDeliveryDocumentTypes"] = (
        capo_invoicing.types.einvoice_delivery_document_types.serialize_aws_json_1_0(
            value["einvoice_delivery_document_types"]
        )
    )
    if "einvoice_delivery_attachment_types" in value:
        import capo_invoicing.types.einvoice_delivery_attachment_types

        out["EinvoiceDeliveryAttachmentTypes"] = (
            capo_invoicing.types.einvoice_delivery_attachment_types.serialize_aws_json_1_0(
                value["einvoice_delivery_attachment_types"]
            )
        )
    import capo_invoicing.types.protocol

    out["Protocol"] = capo_invoicing.types.protocol.serialize_aws_json_1_0(
        value["protocol"]
    )
    import capo_invoicing.types.purchase_order_data_sources

    out["PurchaseOrderDataSources"] = (
        capo_invoicing.types.purchase_order_data_sources.serialize_aws_json_1_0(
            value["purchase_order_data_sources"]
        )
    )
    import capo_invoicing.types.connection_testing_method

    out["ConnectionTestingMethod"] = (
        capo_invoicing.types.connection_testing_method.serialize_aws_json_1_0(
            value["connection_testing_method"]
        )
    )
    import capo_invoicing.types._prelude.timestamp

    out["EinvoiceDeliveryActivationDate"] = (
        capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["einvoice_delivery_activation_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EinvoiceDeliveryPreference:
    out: EinvoiceDeliveryPreference = {}  # type: ignore[typeddict-item]
    if data.get("EinvoiceDeliveryDocumentTypes") is not None:
        import capo_invoicing.types.einvoice_delivery_document_types

        out["einvoice_delivery_document_types"] = (
            capo_invoicing.types.einvoice_delivery_document_types.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryDocumentTypes"]
            )
        )
    else:
        out["einvoice_delivery_document_types"] = []
    if data.get("EinvoiceDeliveryAttachmentTypes") is not None:
        import capo_invoicing.types.einvoice_delivery_attachment_types

        out["einvoice_delivery_attachment_types"] = (
            capo_invoicing.types.einvoice_delivery_attachment_types.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryAttachmentTypes"]
            )
        )
    if data.get("Protocol") is not None:
        import capo_invoicing.types.protocol

        out["protocol"] = capo_invoicing.types.protocol.deserialize_aws_json_1_0(
            data["Protocol"]
        )
    else:
        import typing

        out["protocol"] = typing.cast("capo_invoicing.types.protocol.Protocol", "")
    if data.get("PurchaseOrderDataSources") is not None:
        import capo_invoicing.types.purchase_order_data_sources

        out["purchase_order_data_sources"] = (
            capo_invoicing.types.purchase_order_data_sources.deserialize_aws_json_1_0(
                data["PurchaseOrderDataSources"]
            )
        )
    else:
        out["purchase_order_data_sources"] = []
    if data.get("ConnectionTestingMethod") is not None:
        import capo_invoicing.types.connection_testing_method

        out["connection_testing_method"] = (
            capo_invoicing.types.connection_testing_method.deserialize_aws_json_1_0(
                data["ConnectionTestingMethod"]
            )
        )
    else:
        import typing

        out["connection_testing_method"] = typing.cast(
            "capo_invoicing.types.connection_testing_method.ConnectionTestingMethod", ""
        )
    if data.get("EinvoiceDeliveryActivationDate") is not None:
        import capo_invoicing.types._prelude.timestamp

        out["einvoice_delivery_activation_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryActivationDate"]
            )
        )
    else:
        import datetime

        out["einvoice_delivery_activation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
