"""Generated from Smithy shape ``com.amazonaws.workspacesweb#BrandingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.color_theme
    import capo_workspaces_web.types.image_metadata
    import capo_workspaces_web.types.localized_branding_string_map
    import capo_workspaces_web.types.markdown


class BrandingConfiguration(TypedDict, closed=True):
    logo: "capo_workspaces_web.types.image_metadata.ImageMetadata"
    """<p>Metadata for the logo image file, including the MIME type, file extension, and upload timestamp.</p>"""
    wallpaper: NotRequired["capo_workspaces_web.types.image_metadata.ImageMetadata"]
    """<p>Metadata for the wallpaper image file, including the MIME type, file extension, and upload timestamp.</p>"""
    favicon: "capo_workspaces_web.types.image_metadata.ImageMetadata"
    """<p>Metadata for the favicon image file, including the MIME type, file extension, and upload timestamp.</p>"""
    localized_strings: "capo_workspaces_web.types.localized_branding_string_map.LocalizedBrandingStringMap"
    """<p>A map of localized text strings for different languages, allowing the portal to display content in the user's preferred language.</p>"""
    color_theme: "capo_workspaces_web.types.color_theme.ColorTheme"
    """<p>The color theme for components on the web portal.</p>"""
    terms_of_service: NotRequired["capo_workspaces_web.types.markdown.Markdown"]
    """<p>The terms of service text in Markdown format that users must accept before accessing the portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandingConfiguration) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.image_metadata

    out["logo"] = capo_workspaces_web.types.image_metadata.serialize_json(value["logo"])
    if "wallpaper" in value:
        import capo_workspaces_web.types.image_metadata

        out["wallpaper"] = capo_workspaces_web.types.image_metadata.serialize_json(
            value["wallpaper"]
        )
    import capo_workspaces_web.types.image_metadata

    out["favicon"] = capo_workspaces_web.types.image_metadata.serialize_json(
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


def deserialize_json(data: dict) -> BrandingConfiguration:
    out: BrandingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("logo") is not None:
        import capo_workspaces_web.types.image_metadata

        out["logo"] = capo_workspaces_web.types.image_metadata.deserialize_json(
            data["logo"]
        )
    else:
        raise DeserializationError("BrandingConfiguration.logo required")
    if data.get("wallpaper") is not None:
        import capo_workspaces_web.types.image_metadata

        out["wallpaper"] = capo_workspaces_web.types.image_metadata.deserialize_json(
            data["wallpaper"]
        )
    if data.get("favicon") is not None:
        import capo_workspaces_web.types.image_metadata

        out["favicon"] = capo_workspaces_web.types.image_metadata.deserialize_json(
            data["favicon"]
        )
    else:
        raise DeserializationError("BrandingConfiguration.favicon required")
    if data.get("localizedStrings") is not None:
        import capo_workspaces_web.types.localized_branding_string_map

        out["localized_strings"] = (
            capo_workspaces_web.types.localized_branding_string_map.deserialize_json(
                data["localizedStrings"]
            )
        )
    else:
        raise DeserializationError("BrandingConfiguration.localized_strings required")
    if data.get("colorTheme") is not None:
        import capo_workspaces_web.types.color_theme

        out["color_theme"] = capo_workspaces_web.types.color_theme.deserialize_json(
            data["colorTheme"]
        )
    else:
        raise DeserializationError("BrandingConfiguration.color_theme required")
    if data.get("termsOfService") is not None:
        out["terms_of_service"] = data["termsOfService"]
    return out


def redact_sensitive(value: BrandingConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "terms_of_service" in value:
        out["terms_of_service"] = "*** Sensitive Data Redacted ***"
    return out
