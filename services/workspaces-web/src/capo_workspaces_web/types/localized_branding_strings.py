"""Generated from Smithy shape ``com.amazonaws.workspacesweb#LocalizedBrandingStrings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.branding_safe_string_type
    import capo_workspaces_web.types.contact_link_url


class LocalizedBrandingStrings(TypedDict, closed=True):
    browser_tab_title: (
        "capo_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    )
    """<p>The text displayed in the browser tab title.</p>"""
    welcome_text: (
        "capo_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    )
    """<p>The welcome text displayed on the sign-in page.</p>"""
    login_title: NotRequired[
        "capo_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    """<p>The title text for the login section. This field is optional and defaults to "Sign In".</p>"""
    login_description: NotRequired[
        "capo_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    """<p>The description text for the login section. This field is optional and defaults to "Sign in to your session".</p>"""
    login_button_text: NotRequired[
        "capo_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    """<p>The text displayed on the login button. This field is optional and defaults to "Sign In".</p>"""
    contact_link: NotRequired[
        "capo_workspaces_web.types.contact_link_url.ContactLinkUrl"
    ]
    """<p>A contact link URL. The URL must start with <code>https://</code> or <code>mailto:</code>. If not provided, the contact button will be hidden from the web portal screen.</p>"""
    contact_button_text: NotRequired[
        "capo_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    """<p>The text displayed on the contact button. This field is optional and defaults to "Contact us".</p>"""
    loading_text: NotRequired[
        "capo_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    """<p>The text displayed during session loading. This field is optional and defaults to "Loading your session".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalizedBrandingStrings) -> dict:
    out: dict = {}
    out["browserTabTitle"] = value["browser_tab_title"]
    out["welcomeText"] = value["welcome_text"]
    if "login_title" in value:
        out["loginTitle"] = value["login_title"]
    if "login_description" in value:
        out["loginDescription"] = value["login_description"]
    if "login_button_text" in value:
        out["loginButtonText"] = value["login_button_text"]
    if "contact_link" in value:
        out["contactLink"] = value["contact_link"]
    if "contact_button_text" in value:
        out["contactButtonText"] = value["contact_button_text"]
    if "loading_text" in value:
        out["loadingText"] = value["loading_text"]
    return out


def deserialize_json(data: dict) -> LocalizedBrandingStrings:
    out: LocalizedBrandingStrings = {}  # type: ignore[typeddict-item]
    if data.get("browserTabTitle") is not None:
        out["browser_tab_title"] = data["browserTabTitle"]
    else:
        raise DeserializationError(
            "LocalizedBrandingStrings.browser_tab_title required"
        )
    if data.get("welcomeText") is not None:
        out["welcome_text"] = data["welcomeText"]
    else:
        raise DeserializationError("LocalizedBrandingStrings.welcome_text required")
    if data.get("loginTitle") is not None:
        out["login_title"] = data["loginTitle"]
    if data.get("loginDescription") is not None:
        out["login_description"] = data["loginDescription"]
    if data.get("loginButtonText") is not None:
        out["login_button_text"] = data["loginButtonText"]
    if data.get("contactLink") is not None:
        out["contact_link"] = data["contactLink"]
    if data.get("contactButtonText") is not None:
        out["contact_button_text"] = data["contactButtonText"]
    if data.get("loadingText") is not None:
        out["loading_text"] = data["loadingText"]
    return out
