"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.tag_list
    import capo_quicksight.types.theme_configuration
    import capo_quicksight.types.theme_name
    import capo_quicksight.types.version_description


class CreateThemeRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account where you want to store the new theme. </p>"""
    theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An ID for the theme that you want to create. The theme ID is unique per Amazon Web Services Region in each Amazon Web Services account.</p>"""
    name: "capo_quicksight.types.theme_name.ThemeName"
    """<p>A display name for the theme.</p>"""
    base_theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of the starting themes defined by Amazon Quick Sight. For a list of the starting themes, use <code>ListThemes</code> or choose <b>Themes</b> from within an analysis. </p>"""
    version_description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>A description of the first version of the theme that you're creating. Every time <code>UpdateTheme</code> is called, a new version is created. Each version of the theme has a description of the version in the <code>VersionDescription</code> field.</p>"""
    configuration: "capo_quicksight.types.theme_configuration.ThemeConfiguration"
    """<p>The theme configuration, which contains the theme display properties.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A valid grouping of resource permissions to apply to the new theme. </p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>A map of the key-value pairs for the resource tag or tags that you want to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThemeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["BaseThemeId"] = value["base_theme_id"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    import capo_quicksight.types.theme_configuration

    out["Configuration"] = capo_quicksight.types.theme_configuration.serialize_json(
        value["configuration"]
    )
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateThemeRequest:
    out: CreateThemeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    else:
        raise DeserializationError("CreateThemeRequest.configuration required")
    if data.get("Permissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out
