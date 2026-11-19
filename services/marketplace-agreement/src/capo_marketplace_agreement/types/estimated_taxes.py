"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EstimatedTaxes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.tax_breakdown


class EstimatedTaxes(TypedDict, closed=True):
    breakdown: NotRequired[
        "capo_marketplace_agreement.types.tax_breakdown.TaxBreakdown"
    ]
    """<p>A list of tax breakdown information.</p>"""
    total_amount: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The total amount of tax aggregated from the tax breakdown.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EstimatedTaxes) -> dict:
    out: dict = {}
    if "breakdown" in value:
        import capo_marketplace_agreement.types.tax_breakdown

        out["breakdown"] = (
            capo_marketplace_agreement.types.tax_breakdown.serialize_aws_json_1_0(
                value["breakdown"]
            )
        )
    if "total_amount" in value:
        out["totalAmount"] = value["total_amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EstimatedTaxes:
    out: EstimatedTaxes = {}  # type: ignore[typeddict-item]
    if data.get("breakdown") is not None:
        import capo_marketplace_agreement.types.tax_breakdown

        out["breakdown"] = (
            capo_marketplace_agreement.types.tax_breakdown.deserialize_aws_json_1_0(
                data["breakdown"]
            )
        )
    if data.get("totalAmount") is not None:
        out["total_amount"] = data["totalAmount"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EstimatedTaxes) -> dict:
    out: dict = {}
    if "breakdown" in value:
        import capo_marketplace_agreement.types.tax_breakdown

        out["breakdown"] = (
            capo_marketplace_agreement.types.tax_breakdown.serialize_cbor(
                value["breakdown"]
            )
        )
    if "total_amount" in value:
        out["totalAmount"] = value["total_amount"]
    return out


def deserialize_cbor(data: dict) -> EstimatedTaxes:
    out: EstimatedTaxes = {}  # type: ignore[typeddict-item]
    if data.get("breakdown") is not None:
        import capo_marketplace_agreement.types.tax_breakdown

        out["breakdown"] = (
            capo_marketplace_agreement.types.tax_breakdown.deserialize_cbor(
                data["breakdown"]
            )
        )
    if data.get("totalAmount") is not None:
        out["total_amount"] = data["totalAmount"]
    return out
