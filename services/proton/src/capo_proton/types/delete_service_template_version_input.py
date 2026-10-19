"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceTemplateVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name
    import capo_proton.types.template_version_part


class DeleteServiceTemplateVersionInput(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    major_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The service template major version to delete.</p>"""
    minor_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The service template minor version to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceTemplateVersionInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceTemplateVersionInput:
    out: DeleteServiceTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        out["template_name"] = ""
    if data.get("majorVersion") is not None:
        out["major_version"] = data["majorVersion"]
    else:
        out["major_version"] = ""
    if data.get("minorVersion") is not None:
        out["minor_version"] = data["minorVersion"]
    else:
        out["minor_version"] = ""
    return out
