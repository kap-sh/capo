"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTemplateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.version_number


class CreateTemplateAliasRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the template that you creating an alias for.</p>"""
    template_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An ID for the template.</p>"""
    alias_name: "capo_quicksight.types.alias_name.AliasName"
    """<p>The name that you want to give to the template alias that you're creating. Don't start the alias name with the <code>$</code> character. Alias names that start with <code>$</code> are reserved by Quick Sight. </p>"""
    template_version_number: "capo_quicksight.types.version_number.VersionNumber"
    """<p>The version number of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateAliasRequest) -> dict:
    out: dict = {}
    out["TemplateVersionNumber"] = value["template_version_number"]
    return out


def deserialize_json(data: dict) -> CreateTemplateAliasRequest:
    out: CreateTemplateAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("TemplateVersionNumber") is not None:
        out["template_version_number"] = data["TemplateVersionNumber"]
    else:
        out["template_version_number"] = 0
    return out
