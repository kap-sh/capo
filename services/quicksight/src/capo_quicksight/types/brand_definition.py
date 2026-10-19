"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.application_theme
    import capo_quicksight.types.description
    import capo_quicksight.types.logo_configuration
    import capo_quicksight.types.name


class BrandDefinition(TypedDict, closed=True):
    brand_name: "capo_quicksight.types.name.Name"
    """<p>The name of the brand.</p>"""
    description: NotRequired["capo_quicksight.types.description.Description"]
    """<p>The description of the brand.</p>"""
    application_theme: NotRequired[
        "capo_quicksight.types.application_theme.ApplicationTheme"
    ]
    """<p>The application theme of the brand.</p>"""
    logo_configuration: NotRequired[
        "capo_quicksight.types.logo_configuration.LogoConfiguration"
    ]
    """<p>The logo configuration of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandDefinition) -> dict:
    out: dict = {}
    out["BrandName"] = value["brand_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "application_theme" in value:
        import capo_quicksight.types.application_theme

        out["ApplicationTheme"] = (
            capo_quicksight.types.application_theme.serialize_json(
                value["application_theme"]
            )
        )
    if "logo_configuration" in value:
        import capo_quicksight.types.logo_configuration

        out["LogoConfiguration"] = (
            capo_quicksight.types.logo_configuration.serialize_json(
                value["logo_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrandDefinition:
    out: BrandDefinition = {}  # type: ignore[typeddict-item]
    if data.get("BrandName") is not None:
        out["brand_name"] = data["BrandName"]
    else:
        out["brand_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ApplicationTheme") is not None:
        import capo_quicksight.types.application_theme

        out["application_theme"] = (
            capo_quicksight.types.application_theme.deserialize_json(
                data["ApplicationTheme"]
            )
        )
    if data.get("LogoConfiguration") is not None:
        import capo_quicksight.types.logo_configuration

        out["logo_configuration"] = (
            capo_quicksight.types.logo_configuration.deserialize_json(
                data["LogoConfiguration"]
            )
        )
    return out
