"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Charge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.charge_revision
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.purchase_order_reference
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.timestamp


class Charge(TypedDict, closed=True):
    id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the charge.</p>"""
    revision: NotRequired[
        "capo_marketplace_agreement.types.charge_revision.ChargeRevision"
    ]
    """<p>The revision number of the charge.</p>"""
    agreement_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the agreement that resulted in this charge.</p>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>The type of agreement that resulted in this charge (for example, <code>PurchaseAgreement</code>).</p>"""
    purchase_order_reference: NotRequired[
        "capo_marketplace_agreement.types.purchase_order_reference.PurchaseOrderReference"
    ]
    """<p>The purchase order reference associated with the charge, if any.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>The currency code for the charge amount.</p>"""
    amount: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>The amount of the charge.</p>"""
    time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the charge will be incurred. This is available only when the charge date is known.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Charge) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "purchase_order_reference" in value:
        out["purchaseOrderReference"] = value["purchase_order_reference"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "amount" in value:
        out["amount"] = value["amount"]
    if "time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["time"] = capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
            value["time"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Charge:
    out: Charge = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("purchaseOrderReference") is not None:
        out["purchase_order_reference"] = data["purchaseOrderReference"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("time") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["time"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Charge) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "purchase_order_reference" in value:
        out["purchaseOrderReference"] = value["purchase_order_reference"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "amount" in value:
        out["amount"] = value["amount"]
    if "time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["time"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
            value["time"]
        )
    return out


def deserialize_cbor(data: dict) -> Charge:
    out: Charge = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("purchaseOrderReference") is not None:
        out["purchase_order_reference"] = data["purchaseOrderReference"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("time") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["time"] = capo_marketplace_agreement.types.timestamp.deserialize_cbor(
            data["time"]
        )
    return out
