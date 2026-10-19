"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BundleInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.pricing_bundles
    import capo_iottwinmaker.types.pricing_tier


class BundleInformation(TypedDict, closed=True):
    bundle_names: "capo_iottwinmaker.types.pricing_bundles.PricingBundles"
    """<p>The bundle names.</p>"""
    pricing_tier: NotRequired["capo_iottwinmaker.types.pricing_tier.PricingTier"]
    """<p>The pricing tier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BundleInformation) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.pricing_bundles

    out["bundleNames"] = capo_iottwinmaker.types.pricing_bundles.serialize_json(
        value["bundle_names"]
    )
    if "pricing_tier" in value:
        out["pricingTier"] = value["pricing_tier"]
    return out


def deserialize_json(data: dict) -> BundleInformation:
    out: BundleInformation = {}  # type: ignore[typeddict-item]
    if data.get("bundleNames") is not None:
        import capo_iottwinmaker.types.pricing_bundles

        out["bundle_names"] = capo_iottwinmaker.types.pricing_bundles.deserialize_json(
            data["bundleNames"]
        )
    else:
        out["bundle_names"] = []
    if data.get("pricingTier") is not None:
        out["pricing_tier"] = data["pricingTier"]
    return out
