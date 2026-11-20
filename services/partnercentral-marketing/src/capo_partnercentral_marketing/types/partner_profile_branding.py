"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#PartnerProfileBranding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.partner_logo_url
    import capo_partnercentral_marketing.types.timestamp


class PartnerProfileBranding(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """The profile's display name."""
    website_url: NotRequired["str"]
    """The profile's website."""
    logo_url: NotRequired[
        "capo_partnercentral_marketing.types.partner_logo_url.PartnerLogoUrl"
    ]
    """The profile's logo URL, as AWS Partner Central serves it — the image every asset of the campaign shows. Absent when the profile names none. <p>Partner Central Marketing keeps no copy: the same URL is written into a published landing page and email, and fetched when a document is composed, so what a client renders from it is what is sent. Only a document fetches the image: one it cannot fetch and draw fails that asset with `INTERNAL_ERROR`, which a retry can clear. A landing page or email links the URL as given, so a logo that does not load shows as a broken image."""
    refreshed_at: "capo_partnercentral_marketing.types.timestamp.Timestamp"
    """When this branding was last read from Partner Central. Earlier than the request when Partner Central could not be reached and Partner Central Marketing answered from its last copy."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartnerProfileBranding) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    if "logo_url" in value:
        out["LogoUrl"] = value["logo_url"]
    import capo_partnercentral_marketing.types.timestamp

    out["RefreshedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
        value["refreshed_at"]
    )
    return out


def deserialize_cbor(data: dict) -> PartnerProfileBranding:
    out: PartnerProfileBranding = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    if data.get("LogoUrl") is not None:
        out["logo_url"] = data["LogoUrl"]
    if data.get("RefreshedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["refreshed_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["RefreshedAt"]
            )
        )
    else:
        import datetime

        out["refreshed_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
