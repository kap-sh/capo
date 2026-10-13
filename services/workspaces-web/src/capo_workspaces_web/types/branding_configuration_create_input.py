"""Generated from Smithy shape ``com.amazonaws.workspacesweb#BrandingConfigurationCreateInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.color_theme
    import capo_workspaces_web.types.icon_image_input
    import capo_workspaces_web.types.localized_branding_string_map
    import capo_workspaces_web.types.markdown
    import capo_workspaces_web.types.wallpaper_image_input


class BrandingConfigurationCreateInput(TypedDict, closed=True):
    logo: "capo_workspaces_web.types.icon_image_input.IconImageInput"
    """<p>The logo image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 100 KB in JPEG, PNG, or ICO format.</p>"""
    wallpaper: NotRequired[
        "capo_workspaces_web.types.wallpaper_image_input.WallpaperImageInput"
    ]
    """<p>The wallpaper image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 5 MB in JPEG or PNG format. If not provided, a default wallpaper will be used as the background image.</p>"""
    favicon: "capo_workspaces_web.types.icon_image_input.IconImageInput"
    """<p>The favicon image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 100 KB in JPEG, PNG, or ICO format.</p>"""
    localized_strings: "capo_workspaces_web.types.localized_branding_string_map.LocalizedBrandingStringMap"
    """<p>A map of localized text strings for different supported languages. Each locale must provide the required fields <code>browserTabTitle</code> and <code>welcomeText</code>.</p>"""
    color_theme: "capo_workspaces_web.types.color_theme.ColorTheme"
    """<p>The color theme for components on the web portal. Choose <code>Light</code> if you upload a dark wallpaper, or <code>Dark</code> for a light wallpaper.</p>"""
    terms_of_service: NotRequired["capo_workspaces_web.types.markdown.Markdown"]
    """<p>The terms of service text in Markdown format. Users will be presented with the terms of service after successfully signing in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandingConfigurationCreateInput) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.icon_image_input

    out["logo"] = capo_workspaces_web.types.icon_image_input.serialize_json(
        value["logo"]
    )
    if "wallpaper" in value:
        import capo_workspaces_web.types.wallpaper_image_input

        out["wallpaper"] = (
            capo_workspaces_web.types.wallpaper_image_input.serialize_json(
                value["wallpaper"]
            )
        )
    import capo_workspaces_web.types.icon_image_input

    out["favicon"] = capo_workspaces_web.types.icon_image_input.serialize_json(
        value["favicon"]
    )
    import capo_workspaces_web.types.localized_branding_string_map

    out["localizedStrings"] = (
        capo_workspaces_web.types.localized_branding_string_map.serialize_json(
            value["localized_strings"]
        )
    )
    import capo_workspaces_web.types.color_theme

    out["colorTheme"] = capo_workspaces_web.types.color_theme.serialize_json(
        value["color_theme"]
    )
    if "terms_of_service" in value:
        out["termsOfService"] = value["terms_of_service"]
    return out


def deserialize_json(data: dict) -> BrandingConfigurationCreateInput:
    out: BrandingConfigurationCreateInput = {}  # type: ignore[typeddict-item]
    if data.get("logo") is not None:
        import capo_workspaces_web.types.icon_image_input

        out["logo"] = capo_workspaces_web.types.icon_image_input.deserialize_json(
            data["logo"]
        )
    else:
        raise DeserializationError("BrandingConfigurationCreateInput.logo required")
    if data.get("wallpaper") is not None:
        import capo_workspaces_web.types.wallpaper_image_input

        out["wallpaper"] = (
            capo_workspaces_web.types.wallpaper_image_input.deserialize_json(
                data["wallpaper"]
            )
        )
    if data.get("favicon") is not None:
        import capo_workspaces_web.types.icon_image_input

        out["favicon"] = capo_workspaces_web.types.icon_image_input.deserialize_json(
            data["favicon"]
        )
    else:
        raise DeserializationError("BrandingConfigurationCreateInput.favicon required")
    if data.get("localizedStrings") is not None:
        import capo_workspaces_web.types.localized_branding_string_map

        out["localized_strings"] = (
            capo_workspaces_web.types.localized_branding_string_map.deserialize_json(
                data["localizedStrings"]
            )
        )
    else:
        raise DeserializationError(
            "BrandingConfigurationCreateInput.localized_strings required"
        )
    if data.get("colorTheme") is not None:
        import capo_workspaces_web.types.color_theme

        out["color_theme"] = capo_workspaces_web.types.color_theme.deserialize_json(
            data["colorTheme"]
        )
    else:
        raise DeserializationError(
            "BrandingConfigurationCreateInput.color_theme required"
        )
    if data.get("termsOfService") is not None:
        out["terms_of_service"] = data["termsOfService"]
    return out


def redact_sensitive(value: BrandingConfigurationCreateInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "terms_of_service" in value:
        out["terms_of_service"] = "*** Sensitive Data Redacted ***"
    return out
