"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceTemplateInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.description
    import capo_proton.types.display_name
    import capo_proton.types.resource_name


class UpdateServiceTemplateInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template to update.</p>"""
    display_name: NotRequired["capo_proton.types.display_name.DisplayName"]
    """<p>The name of the service template to update that's displayed in the developer interface.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the service template update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceTemplateInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceTemplateInput:
    out: UpdateServiceTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateServiceTemplateInput.name required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: UpdateServiceTemplateInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
