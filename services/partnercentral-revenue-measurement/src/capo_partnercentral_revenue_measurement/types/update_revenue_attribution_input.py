"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#UpdateRevenueAttributionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.client_token
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier
    import capo_partnercentral_revenue_measurement.types.revision_token


class UpdateRevenueAttributionInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog that the revenue attribution belongs to.</p>"""
    identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier"
    """<p>The unique identifier of the revenue attribution to update. Accepts a direct ID or ARN.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
    ]
    """<p>A unique token to ensure idempotency of the update request.</p>"""
    description: NotRequired["str"]
    """<p>The updated description of the revenue attribution.</p>"""
    revision: (
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    )
    """<p>The current revision of the revenue attribution. Must match the server's current value.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateRevenueAttributionInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Revision"] = value["revision"]
    return out


def deserialize_cbor(data: dict) -> UpdateRevenueAttributionInput:
    out: UpdateRevenueAttributionInput = {}  # type: ignore[typeddict-item]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    else:
        out["revision"] = ""
    return out
