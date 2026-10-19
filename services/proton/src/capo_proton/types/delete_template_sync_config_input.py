"""Generated from Smithy shape ``com.amazonaws.proton#DeleteTemplateSyncConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name
    import capo_proton.types.template_type


class DeleteTemplateSyncConfigInput(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The template name.</p>"""
    template_type: "capo_proton.types.template_type.TemplateType"
    """<p>The template type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTemplateSyncConfigInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["templateType"] = value["template_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTemplateSyncConfigInput:
    out: DeleteTemplateSyncConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        out["template_name"] = ""
    if data.get("templateType") is not None:
        out["template_type"] = data["templateType"]
    else:
        out["template_type"] = ""
    return out
