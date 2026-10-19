"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentTemplateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name
    import capo_proton.types.template_version_part


class EnvironmentTemplateFilter(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>Include <code>templateName</code> to filter search for a template name.</p>"""
    major_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>Include <code>majorVersion</code> to filter search for a major version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentTemplateFilter) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnvironmentTemplateFilter:
    out: EnvironmentTemplateFilter = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        out["template_name"] = ""
    if data.get("majorVersion") is not None:
        out["major_version"] = data["majorVersion"]
    else:
        out["major_version"] = ""
    return out
