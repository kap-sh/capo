"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents


class UpdateServiceInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service to edit.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>The edited service description.</p>"""
    spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. <i>Don't</i> include edits to the existing service instances or pipeline. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html">Edit a service</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "spec" in value:
        out["spec"] = value["spec"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceInput:
    out: UpdateServiceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateServiceInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    return out
