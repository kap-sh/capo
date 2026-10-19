"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.theme_configuration
    import capo_quicksight.types.theme_name
    import capo_quicksight.types.version_description


class UpdateThemeRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme that you're updating.</p>"""
    theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the theme.</p>"""
    name: NotRequired["capo_quicksight.types.theme_name.ThemeName"]
    """<p>The name for the theme.</p>"""
    base_theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The theme ID, defined by Amazon Quick Sight, that a custom theme inherits from. All themes initially inherit from a default Quick Sight theme.</p>"""
    version_description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>A description of the theme version that you're updating Every time that you call <code>UpdateTheme</code>, you create a new version of the theme. Each version of the theme maintains a description of the version in <code>VersionDescription</code>.</p>"""
    configuration: NotRequired[
        "capo_quicksight.types.theme_configuration.ThemeConfiguration"
    ]
    """<p>The theme configuration, which contains the theme display properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["BaseThemeId"] = value["base_theme_id"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "configuration" in value:
        import capo_quicksight.types.theme_configuration

        out["Configuration"] = capo_quicksight.types.theme_configuration.serialize_json(
            value["configuration"]
        )
    return out


def deserialize_json(data: dict) -> UpdateThemeRequest:
    out: UpdateThemeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("BaseThemeId") is not None:
        out["base_theme_id"] = data["BaseThemeId"]
    else:
        out["base_theme_id"] = ""
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("Configuration") is not None:
        import capo_quicksight.types.theme_configuration

        out["configuration"] = (
            capo_quicksight.types.theme_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    return out
