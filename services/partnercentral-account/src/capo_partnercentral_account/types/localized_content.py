"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#LocalizedContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.locale
    import capo_partnercentral_account.types.unicode_string
    import capo_partnercentral_account.types.url


class LocalizedContent(TypedDict, closed=True):
    display_name: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The localized display name for the partner.</p>"""
    description: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The localized description of the partner's business and services.</p>"""
    website_url: "capo_partnercentral_account.types.url.Url"
    """<p>The localized website URL for the partner.</p>"""
    logo_url: "capo_partnercentral_account.types.url.Url"
    """<p>The URL to the partner's logo image for this locale.</p>"""
    locale: "capo_partnercentral_account.types.locale.Locale"
    """<p>The locale or language code for the localized content.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LocalizedContent) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    out["Description"] = value["description"]
    out["WebsiteUrl"] = value["website_url"]
    out["LogoUrl"] = value["logo_url"]
    out["Locale"] = value["locale"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LocalizedContent:
    out: LocalizedContent = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    else:
        out["website_url"] = ""
    if data.get("LogoUrl") is not None:
        out["logo_url"] = data["LogoUrl"]
    else:
        out["logo_url"] = ""
    if data.get("Locale") is not None:
        out["locale"] = data["Locale"]
    else:
        out["locale"] = ""
    return out
