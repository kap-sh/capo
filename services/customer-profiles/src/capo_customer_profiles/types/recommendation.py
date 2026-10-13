"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Recommendation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.catalog_item
    import capo_customer_profiles.types.double0_to1


class Recommendation(TypedDict, closed=True):
    catalog_item: NotRequired["capo_customer_profiles.types.catalog_item.CatalogItem"]
    """<p>The catalog item being recommended, including its complete details and attributes.</p>"""
    score: NotRequired["capo_customer_profiles.types.double0_to1.Double0To1"]
    """<p>Recommendation Score between 0 and 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "catalog_item" in value:
        import capo_customer_profiles.types.catalog_item

        out["CatalogItem"] = capo_customer_profiles.types.catalog_item.serialize_json(
            value["catalog_item"]
        )
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if data.get("CatalogItem") is not None:
        import capo_customer_profiles.types.catalog_item

        out["catalog_item"] = (
            capo_customer_profiles.types.catalog_item.deserialize_json(
                data["CatalogItem"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


def redact_sensitive(value: Recommendation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "catalog_item" in value:
        import capo_customer_profiles.types.catalog_item

        out["catalog_item"] = (
            capo_customer_profiles.types.catalog_item.redact_sensitive(
                value["catalog_item"]
            )
        )
    return out
