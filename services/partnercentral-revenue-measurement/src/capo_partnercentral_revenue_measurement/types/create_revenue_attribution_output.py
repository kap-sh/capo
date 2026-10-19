"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#CreateRevenueAttributionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.marketplace_product_summary
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_id
    import capo_partnercentral_revenue_measurement.types.revision_token
    import capo_partnercentral_revenue_measurement.types.tenancy_model


class CreateRevenueAttributionOutput(TypedDict, closed=True):
    id: "capo_partnercentral_revenue_measurement.types.revenue_attribution_id.RevenueAttributionId"
    """<p>The unique identifier of the newly created revenue attribution.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the newly created revenue attribution.</p>"""
    name: NotRequired["str"]
    """<p>The name of the revenue attribution.</p>"""
    description: NotRequired["str"]
    """<p>The description of the revenue attribution.</p>"""
    tenancy_model: (
        "capo_partnercentral_revenue_measurement.types.tenancy_model.TenancyModel"
    )
    """<p>The tenancy model for this revenue attribution.</p>"""
    marketplace_product: NotRequired[
        "capo_partnercentral_revenue_measurement.types.marketplace_product_summary.MarketplaceProductSummary"
    ]
    """<p>The associated AWS Marketplace product listing, if set at creation.</p>"""
    revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>The revision of the newly created attribution resource.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateRevenueAttributionOutput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_partnercentral_revenue_measurement.types.tenancy_model

    out["TenancyModel"] = (
        capo_partnercentral_revenue_measurement.types.tenancy_model.serialize_cbor(
            value["tenancy_model"]
        )
    )
    if "marketplace_product" in value:
        import capo_partnercentral_revenue_measurement.types.marketplace_product_summary

        out["MarketplaceProduct"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_product_summary.serialize_cbor(
                value["marketplace_product"]
            )
        )
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_cbor(data: dict) -> CreateRevenueAttributionOutput:
    out: CreateRevenueAttributionOutput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("TenancyModel") is not None:
        import capo_partnercentral_revenue_measurement.types.tenancy_model

        out["tenancy_model"] = (
            capo_partnercentral_revenue_measurement.types.tenancy_model.deserialize_cbor(
                data["TenancyModel"]
            )
        )
    else:
        import typing

        out["tenancy_model"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.tenancy_model.TenancyModel",
            "",
        )
    if data.get("MarketplaceProduct") is not None:
        import capo_partnercentral_revenue_measurement.types.marketplace_product_summary

        out["marketplace_product"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_product_summary.deserialize_cbor(
                data["MarketplaceProduct"]
            )
        )
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    return out
