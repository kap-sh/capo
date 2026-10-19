"""Generated from Smithy shape ``com.amazonaws.iot#CreateProvisioningTemplateVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.set_as_default
    import capo_iot.types.template_body
    import capo_iot.types.template_name


class CreateProvisioningTemplateVersionRequest(TypedDict, closed=True):
    template_name: "capo_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template.</p>"""
    template_body: "capo_iot.types.template_body.TemplateBody"
    """<p>The JSON formatted contents of the provisioning template.</p>"""
    set_as_default: NotRequired["capo_iot.types.set_as_default.SetAsDefault"]
    """<p>Sets a fleet provision template version as the default version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningTemplateVersionRequest) -> dict:
    out: dict = {}
    out["templateBody"] = value["template_body"]
    return out


def deserialize_json(data: dict) -> CreateProvisioningTemplateVersionRequest:
    out: CreateProvisioningTemplateVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("templateBody") is not None:
        out["template_body"] = data["templateBody"]
    else:
        out["template_body"] = ""
    return out
