"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentState``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents
    import capo_proton.types.template_version_part


class EnvironmentState(TypedDict, closed=True):
    spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>The environment spec that was used to create the environment.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template that was used to create the environment.</p>"""
    template_major_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The major version of the environment template that was used to create the environment.</p>"""
    template_minor_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The minor version of the environment template that was used to create the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentState) -> dict:
    out: dict = {}
    if "spec" in value:
        out["spec"] = value["spec"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    out["templateMinorVersion"] = value["template_minor_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnvironmentState:
    out: EnvironmentState = {}  # type: ignore[typeddict-item]
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        out["template_name"] = ""
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        out["template_major_version"] = ""
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    else:
        out["template_minor_version"] = ""
    return out


def redact_sensitive(value: EnvironmentState) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spec" in value:
        out["spec"] = "*** Sensitive Data Redacted ***"
    return out
