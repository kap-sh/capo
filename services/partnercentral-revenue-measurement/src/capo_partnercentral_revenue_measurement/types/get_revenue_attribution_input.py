"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#GetRevenueAttributionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier
    import capo_partnercentral_revenue_measurement.types.revision_token


class GetRevenueAttributionInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog that the revenue attribution belongs to.</p>"""
    identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier"
    """<p>The unique identifier of the revenue attribution to retrieve. Accepts a direct ID or ARN.</p>"""
    revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>The revision of the attribution to retrieve. Omit to return the latest revision.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRevenueAttributionInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["Identifier"] = value["identifier"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_cbor(data: dict) -> GetRevenueAttributionInput:
    out: GetRevenueAttributionInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.deserialize_cbor(
                data["Catalog"]
            )
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName", ""
        )
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    return out
