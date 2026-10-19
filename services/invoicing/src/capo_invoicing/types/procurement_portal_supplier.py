"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalSupplier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.country_code
    import capo_invoicing.types.procurement_portal_env
    import capo_invoicing.types.supplier_id_string


class ProcurementPortalSupplier(TypedDict, closed=True):
    supplier_identifier: "capo_invoicing.types.supplier_id_string.SupplierIdString"
    """<p>The unique identifier of the supplier within the procurement portal.</p>"""
    seller_of_record: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The Amazon Web Services seller of record associated with the supplier—the Amazon Web Services legal entity that issues invoices for the account (for example, <code>AWS_INC</code> or <code>AWS_EUROPE</code>).</p>"""
    country_code: NotRequired["capo_invoicing.types.country_code.CountryCode"]
    """<p>The two-letter ISO 3166-1 alpha-2 country code associated with the supplier.</p>"""
    environment: NotRequired[
        "capo_invoicing.types.procurement_portal_env.ProcurementPortalEnv"
    ]
    """<p>The environment identifier for the supplier in the procurement portal. PROD for production env, or TEST for sandbox/test env.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalSupplier) -> dict:
    out: dict = {}
    out["SupplierIdentifier"] = value["supplier_identifier"]
    if "seller_of_record" in value:
        out["SellerOfRecord"] = value["seller_of_record"]
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "environment" in value:
        import capo_invoicing.types.procurement_portal_env

        out["Environment"] = (
            capo_invoicing.types.procurement_portal_env.serialize_aws_json_1_0(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProcurementPortalSupplier:
    out: ProcurementPortalSupplier = {}  # type: ignore[typeddict-item]
    if data.get("SupplierIdentifier") is not None:
        out["supplier_identifier"] = data["SupplierIdentifier"]
    else:
        out["supplier_identifier"] = ""
    if data.get("SellerOfRecord") is not None:
        out["seller_of_record"] = data["SellerOfRecord"]
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    if data.get("Environment") is not None:
        import capo_invoicing.types.procurement_portal_env

        out["environment"] = (
            capo_invoicing.types.procurement_portal_env.deserialize_aws_json_1_0(
                data["Environment"]
            )
        )
    return out
