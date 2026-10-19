"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTemplateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.version_number


class UpdateTemplateAliasRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the template alias that you're updating.</p>"""
    template_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the template.</p>"""
    alias_name: "capo_quicksight.types.alias_name.AliasName"
    """<p>The alias of the template that you want to update. If you name a specific alias, you update the version that the alias points to. You can specify the latest version of the template by providing the keyword <code>$LATEST</code> in the <code>AliasName</code> parameter. The keyword <code>$PUBLISHED</code> doesn't apply to templates.</p>"""
    template_version_number: "capo_quicksight.types.version_number.VersionNumber"
    """<p>The version number of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateAliasRequest) -> dict:
    out: dict = {}
    out["TemplateVersionNumber"] = value["template_version_number"]
    return out


def deserialize_json(data: dict) -> UpdateTemplateAliasRequest:
    out: UpdateTemplateAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("TemplateVersionNumber") is not None:
        out["template_version_number"] = data["TemplateVersionNumber"]
    else:
        out["template_version_number"] = 0
    return out
