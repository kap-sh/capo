"""Generated from Smithy shape ``com.amazonaws.b2bi#UpdateCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_configuration
    import capo_b2bi.types.capability_id
    import capo_b2bi.types.capability_name
    import capo_b2bi.types.instructions_documents


class UpdateCapabilityRequest(TypedDict, closed=True):
    capability_id: "capo_b2bi.types.capability_id.CapabilityId"
    """<p>Specifies a system-assigned unique identifier for the capability.</p>"""
    name: NotRequired["capo_b2bi.types.capability_name.CapabilityName"]
    """<p>Specifies a new name for the capability, to replace the existing name.</p>"""
    configuration: NotRequired[
        "capo_b2bi.types.capability_configuration.CapabilityConfiguration"
    ]
    """<p>Specifies a structure that contains the details for a capability.</p>"""
    instructions_documents: NotRequired[
        "capo_b2bi.types.instructions_documents.InstructionsDocuments"
    ]
    """<p>Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCapabilityRequest) -> dict:
    out: dict = {}
    out["capabilityId"] = value["capability_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "configuration" in value:
        import capo_b2bi.types.capability_configuration

        out["configuration"] = (
            capo_b2bi.types.capability_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "instructions_documents" in value:
        import capo_b2bi.types.instructions_documents

        out["instructionsDocuments"] = (
            capo_b2bi.types.instructions_documents.serialize_aws_json_1_0(
                value["instructions_documents"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCapabilityRequest:
    out: UpdateCapabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("capabilityId") is not None:
        out["capability_id"] = data["capabilityId"]
    else:
        out["capability_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("configuration") is not None:
        import capo_b2bi.types.capability_configuration

        out["configuration"] = (
            capo_b2bi.types.capability_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if data.get("instructionsDocuments") is not None:
        import capo_b2bi.types.instructions_documents

        out["instructions_documents"] = (
            capo_b2bi.types.instructions_documents.deserialize_aws_json_1_0(
                data["instructionsDocuments"]
            )
        )
    return out
