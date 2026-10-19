"""Generated from Smithy shape ``com.amazonaws.invoicing#TestEnvPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.buyer_domain
    import capo_invoicing.types.supplier_domain


class TestEnvPreference(TypedDict, closed=True):
    buyer_domain: "capo_invoicing.types.buyer_domain.BuyerDomain"
    """<p>The domain identifier for the buyer in the test environment of the procurement portal.</p>"""
    buyer_identifier: (
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the buyer in the test environment of the procurement portal.</p>"""
    supplier_domain: "capo_invoicing.types.supplier_domain.SupplierDomain"
    """<p>The domain identifier for the supplier in the test environment of the procurement portal.</p>"""
    supplier_identifier: (
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the supplier in the test environment of the procurement portal.</p>"""
    procurement_portal_shared_secret: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The shared secret or authentication credential used for secure communication with the test environment.</p>"""
    procurement_portal_instance_endpoint: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The endpoint URL where e-invoices are delivered in the test environment.</p>"""
    purchase_order_retrieval_endpoint: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The endpoint URL used for retrieving purchase orders in the test environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestEnvPreference) -> dict:
    out: dict = {}
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
    if "procurement_portal_shared_secret" in value:
        out["ProcurementPortalSharedSecret"] = value["procurement_portal_shared_secret"]
    if "procurement_portal_instance_endpoint" in value:
        out["ProcurementPortalInstanceEndpoint"] = value[
            "procurement_portal_instance_endpoint"
        ]
    if "purchase_order_retrieval_endpoint" in value:
        out["PurchaseOrderRetrievalEndpoint"] = value[
            "purchase_order_retrieval_endpoint"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> TestEnvPreference:
    out: TestEnvPreference = {}  # type: ignore[typeddict-item]
    if data.get("BuyerDomain") is not None:
        import capo_invoicing.types.buyer_domain

        out["buyer_domain"] = (
            capo_invoicing.types.buyer_domain.deserialize_aws_json_1_0(
                data["BuyerDomain"]
            )
        )
    else:
        import typing

        out["buyer_domain"] = typing.cast(
            "capo_invoicing.types.buyer_domain.BuyerDomain", ""
        )
    if data.get("BuyerIdentifier") is not None:
        out["buyer_identifier"] = data["BuyerIdentifier"]
    else:
        out["buyer_identifier"] = ""
    if data.get("SupplierDomain") is not None:
        import capo_invoicing.types.supplier_domain

        out["supplier_domain"] = (
            capo_invoicing.types.supplier_domain.deserialize_aws_json_1_0(
                data["SupplierDomain"]
            )
        )
    else:
        import typing

        out["supplier_domain"] = typing.cast(
            "capo_invoicing.types.supplier_domain.SupplierDomain", ""
        )
    if data.get("SupplierIdentifier") is not None:
        out["supplier_identifier"] = data["SupplierIdentifier"]
    else:
        out["supplier_identifier"] = ""
    if data.get("ProcurementPortalSharedSecret") is not None:
        out["procurement_portal_shared_secret"] = data["ProcurementPortalSharedSecret"]
    if data.get("ProcurementPortalInstanceEndpoint") is not None:
        out["procurement_portal_instance_endpoint"] = data[
            "ProcurementPortalInstanceEndpoint"
        ]
    if data.get("PurchaseOrderRetrievalEndpoint") is not None:
        out["purchase_order_retrieval_endpoint"] = data[
            "PurchaseOrderRetrievalEndpoint"
        ]
    return out
