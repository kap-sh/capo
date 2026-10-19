"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateThemeAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.version_number


class CreateThemeAliasRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme for the new theme alias.</p>"""
    theme_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An ID for the theme alias.</p>"""
    alias_name: "capo_quicksight.types.alias_name.AliasName"
    """<p>The name that you want to give to the theme alias that you are creating. The alias name can't begin with a <code>$</code>. Alias names that start with <code>$</code> are reserved by Amazon Quick Sight. </p>"""
    theme_version_number: "capo_quicksight.types.version_number.VersionNumber"
    """<p>The version number of the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThemeAliasRequest) -> dict:
    out: dict = {}
    out["ThemeVersionNumber"] = value["theme_version_number"]
    return out


def deserialize_json(data: dict) -> CreateThemeAliasRequest:
    out: CreateThemeAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("ThemeVersionNumber") is not None:
        out["theme_version_number"] = data["ThemeVersionNumber"]
    else:
        out["theme_version_number"] = 0
    return out
