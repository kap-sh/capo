"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionBadge``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.purchase_option_badge_type


class PurchaseOptionBadge(TypedDict, closed=True):
    display_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the badge.</p>"""
    badge_type: "capo_marketplace_discovery.types.purchase_option_badge_type.PurchaseOptionBadgeType"
    """<p>The machine-readable type of the badge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionBadge) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    import capo_marketplace_discovery.types.purchase_option_badge_type

    out["badgeType"] = (
        capo_marketplace_discovery.types.purchase_option_badge_type.serialize_json(
            value["badge_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> PurchaseOptionBadge:
    out: PurchaseOptionBadge = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("badgeType") is not None:
        import capo_marketplace_discovery.types.purchase_option_badge_type

        out["badge_type"] = (
            capo_marketplace_discovery.types.purchase_option_badge_type.deserialize_json(
                data["badgeType"]
            )
        )
    else:
        import typing

        out["badge_type"] = typing.cast(
            "capo_marketplace_discovery.types.purchase_option_badge_type.PurchaseOptionBadgeType",
            "",
        )
    return out
