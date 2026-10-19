"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateThemeAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.version_number


class UpdateThemeAliasRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme alias that you're updating.</p>"""
    theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the theme.</p>"""
    alias_name: "capo_quicksight.types.alias_name.AliasName"
    """<p>The name of the theme alias that you want to update.</p>"""
    theme_version_number: "capo_quicksight.types.version_number.VersionNumber"
    """<p>The version number of the theme that the alias should reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeAliasRequest) -> dict:
    out: dict = {}
    out["ThemeVersionNumber"] = value["theme_version_number"]
    return out


def deserialize_json(data: dict) -> UpdateThemeAliasRequest:
    out: UpdateThemeAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("ThemeVersionNumber") is not None:
        out["theme_version_number"] = data["ThemeVersionNumber"]
    else:
        out["theme_version_number"] = 0
    return out
