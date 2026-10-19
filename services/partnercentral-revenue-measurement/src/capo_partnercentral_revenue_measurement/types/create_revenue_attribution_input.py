"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#CreateRevenueAttributionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.client_token
    import capo_partnercentral_revenue_measurement.types.tag_list
    import capo_partnercentral_revenue_measurement.types.tenancy_model


class CreateRevenueAttributionInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog in which to create the revenue attribution.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
    ]
    """<p>A unique token to ensure idempotency of the create request.</p>"""
    name: "str"
    """<p>The name of the revenue attribution. Must be unique within the catalog and the partner's account.</p>"""
    description: NotRequired["str"]
    """<p>A description of the revenue attribution.</p>"""
    tenancy_model: (
        "capo_partnercentral_revenue_measurement.types.tenancy_model.TenancyModel"
    )
    """<p>The tenancy model for this revenue attribution.</p>"""
    product_identifier: NotRequired["str"]
    """<p>The unique product identifier in AWS Marketplace. Accepts a product entity ID (e.g., prod-abc123def4567) or a product ARN.</p>"""
    tags: NotRequired["capo_partnercentral_revenue_measurement.types.tag_list.TagList"]
    """<p>Tags to associate with the revenue attribution upon creation.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateRevenueAttributionInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_partnercentral_revenue_measurement.types.tenancy_model

    out["TenancyModel"] = (
        capo_partnercentral_revenue_measurement.types.tenancy_model.serialize_cbor(
            value["tenancy_model"]
        )
    )
    if "product_identifier" in value:
        out["ProductIdentifier"] = value["product_identifier"]
    if "tags" in value:
        import capo_partnercentral_revenue_measurement.types.tag_list

        out["Tags"] = (
            capo_partnercentral_revenue_measurement.types.tag_list.serialize_cbor(
                value["tags"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateRevenueAttributionInput:
    out: CreateRevenueAttributionInput = {}  # type: ignore[typeddict-item]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("ProductIdentifier") is not None:
        out["product_identifier"] = data["ProductIdentifier"]
    if data.get("Tags") is not None:
        import capo_partnercentral_revenue_measurement.types.tag_list

        out["tags"] = (
            capo_partnercentral_revenue_measurement.types.tag_list.deserialize_cbor(
                data["Tags"]
            )
        )
    return out
