"""Generated from Smithy shape ``com.amazonaws.invoicing#TestEnvPreferenceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.buyer_domain
    import capo_invoicing.types.supplier_domain


class TestEnvPreferenceInput(TypedDict, closed=True):
    buyer_domain: "capo_invoicing.types.buyer_domain.BuyerDomain"
    """<p>The domain identifier to use for the buyer in the test environment.</p>"""
    buyer_identifier: (
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier to use for the buyer in the test environment.</p>"""
    supplier_domain: "capo_invoicing.types.supplier_domain.SupplierDomain"
    """<p>The domain identifier to use for the supplier in the test environment.</p>"""
    supplier_identifier: (
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier to use for the supplier in the test environment.</p>"""
    procurement_portal_shared_secret: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The shared secret or authentication credential to use for secure communication in the test environment.</p>"""
    procurement_portal_instance_endpoint: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The endpoint URL where e-invoices will be delivered in the test environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestEnvPreferenceInput) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> TestEnvPreferenceInput:
    out: TestEnvPreferenceInput = {}  # type: ignore[typeddict-item]
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
    return out
