"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.output_description
    import capo_service_catalog.types.provisioning_artifact_output_key


class ProvisioningArtifactOutput(TypedDict, closed=True):
    key: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_output_key.ProvisioningArtifactOutputKey"
    ]
    """<p>The provisioning artifact output key.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.output_description.OutputDescription"
    ]
    """<p>Description of the provisioning artifact output key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactOutput) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactOutput:
    out: ProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactOutput) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> ProvisioningArtifactOutput:
    out: ProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
