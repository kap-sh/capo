"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerEngagement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.seller_engagement_content_type
    import capo_marketplace_discovery.types.seller_engagement_type


class SellerEngagement(TypedDict, closed=True):
    engagement_type: (
        "capo_marketplace_discovery.types.seller_engagement_type.SellerEngagementType"
    )
    """<p>The type of engagement, such as <code>REQUEST_FOR_PRIVATE_OFFER</code> or <code>REQUEST_FOR_DEMO</code>.</p>"""
    content_type: "capo_marketplace_discovery.types.seller_engagement_content_type.SellerEngagementContentType"
    """<p>The format of the engagement value, such as a URL.</p>"""
    value: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The engagement value, such as a URL to the engagement form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SellerEngagement) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.seller_engagement_type

    out["engagementType"] = (
        capo_marketplace_discovery.types.seller_engagement_type.serialize_json(
            value["engagement_type"]
        )
    )
    import capo_marketplace_discovery.types.seller_engagement_content_type

    out["contentType"] = (
        capo_marketplace_discovery.types.seller_engagement_content_type.serialize_json(
            value["content_type"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SellerEngagement:
    out: SellerEngagement = {}  # type: ignore[typeddict-item]
    if data.get("engagementType") is not None:
        import capo_marketplace_discovery.types.seller_engagement_type

        out["engagement_type"] = (
            capo_marketplace_discovery.types.seller_engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
    else:
        import typing

        out["engagement_type"] = typing.cast(
            "capo_marketplace_discovery.types.seller_engagement_type.SellerEngagementType",
            "",
        )
    if data.get("contentType") is not None:
        import capo_marketplace_discovery.types.seller_engagement_content_type

        out["content_type"] = (
            capo_marketplace_discovery.types.seller_engagement_content_type.deserialize_json(
                data["contentType"]
            )
        )
    else:
        import typing

        out["content_type"] = typing.cast(
            "capo_marketplace_discovery.types.seller_engagement_content_type.SellerEngagementContentType",
            "",
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
