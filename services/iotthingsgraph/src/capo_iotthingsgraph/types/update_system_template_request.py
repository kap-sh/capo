"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UpdateSystemTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.definition_document
    import capo_iotthingsgraph.types.urn
    import capo_iotthingsgraph.types.version


class UpdateSystemTemplateRequest(TypedDict, closed=True):
    id: "capo_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the system to be updated.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME</code> </p>"""
    definition: "capo_iotthingsgraph.types.definition_document.DefinitionDocument"
    """<p>The <code>DefinitionDocument</code> that contains the updated system definition.</p>"""
    compatible_namespace_version: NotRequired[
        "capo_iotthingsgraph.types.version.Version"
    ]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p> <p>If no value is specified, the latest version is used by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSystemTemplateRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_iotthingsgraph.types.definition_document

    out["definition"] = (
        capo_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
            value["definition"]
        )
    )
    if "compatible_namespace_version" in value:
        out["compatibleNamespaceVersion"] = value["compatible_namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSystemTemplateRequest:
    out: UpdateSystemTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("definition") is not None:
        import capo_iotthingsgraph.types.definition_document

        out["definition"] = (
            capo_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("UpdateSystemTemplateRequest.definition required")
    if data.get("compatibleNamespaceVersion") is not None:
        out["compatible_namespace_version"] = data["compatibleNamespaceVersion"]
    return out
