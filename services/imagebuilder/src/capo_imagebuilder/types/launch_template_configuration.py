"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LaunchTemplateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.account_id
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.launch_template_id


class LaunchTemplateConfiguration(TypedDict, closed=True):
    launch_template_id: "capo_imagebuilder.types.launch_template_id.LaunchTemplateId"
    """<p>Identifies the Amazon EC2 launch template to use.</p>"""
    account_id: NotRequired["capo_imagebuilder.types.account_id.AccountId"]
    """<p>The account ID that this configuration applies to.</p>"""
    set_default_version: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Specifies whether to make the new launch template version that Image Builder creates the default version of the launch template. If you don't set a value, Image Builder treats it as <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateConfiguration) -> dict:
    out: dict = {}
    out["launchTemplateId"] = value["launch_template_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    out["setDefaultVersion"] = value.get("set_default_version", False)
    return out


def deserialize_json(data: dict) -> LaunchTemplateConfiguration:
    out: LaunchTemplateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("launchTemplateId") is not None:
        out["launch_template_id"] = data["launchTemplateId"]
    else:
        out["launch_template_id"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("setDefaultVersion") is not None:
        out["set_default_version"] = data["setDefaultVersion"]
    else:
        out["set_default_version"] = False
    return out
