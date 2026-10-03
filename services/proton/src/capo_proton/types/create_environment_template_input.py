"""Generated from Smithy shape ``com.amazonaws.proton#CreateEnvironmentTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.description
    import capo_proton.types.display_name
    import capo_proton.types.provisioning
    import capo_proton.types.resource_name
    import capo_proton.types.tag_list


class CreateEnvironmentTemplateInput(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template.</p>"""
    display_name: NotRequired["capo_proton.types.display_name.DisplayName"]
    """<p>The environment template name as displayed in the developer interface.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the environment template.</p>"""
    encryption_key: NotRequired["capo_proton.types.arn.Arn"]
    """<p>A customer provided encryption key that Proton uses to encrypt data.</p>"""
    provisioning: NotRequired["capo_proton.types.provisioning.Provisioning"]
    """<p>When included, indicates that the environment template is for customer provisioned and managed infrastructure.</p>"""
    tags: NotRequired["capo_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentTemplateInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "provisioning" in value:
        out["provisioning"] = value["provisioning"]
    if "tags" in value:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentTemplateInput:
    out: CreateEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentTemplateInput.name required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("provisioning") is not None:
        out["provisioning"] = data["provisioning"]
    if data.get("tags") is not None:
        import capo_proton.types.tag_list

        out["tags"] = capo_proton.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    return out
