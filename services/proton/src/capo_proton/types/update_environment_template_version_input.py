"""Generated from Smithy shape ``com.amazonaws.proton#UpdateEnvironmentTemplateVersionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_status


class UpdateEnvironmentTemplateVersionInput(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template.</p>"""
    major_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>To update a major version of an environment template, include <code>major Version</code>.</p>"""
    minor_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>To update a minor version of an environment template, include <code>minorVersion</code>.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of environment template version to update.</p>"""
    status: NotRequired[
        "capo_proton.types.template_version_status.TemplateVersionStatus"
    ]
    """<p>The status of the environment template minor version to update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentTemplateVersionInput) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentTemplateVersionInput:
    out: UpdateEnvironmentTemplateVersionInput = {}  # type: ignore[typeddict-item]
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
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out


def redact_sensitive(value: UpdateEnvironmentTemplateVersionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
