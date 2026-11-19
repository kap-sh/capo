"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListProvisioningArtifactsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.provisioning_artifact_details


class ListProvisioningArtifactsOutput(TypedDict, closed=True):
    provisioning_artifact_details: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_details.ProvisioningArtifactDetails"
    ]
    """<p>Information about the provisioning artifacts.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProvisioningArtifactsOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_details" in value:
        import capo_service_catalog.types.provisioning_artifact_details

        out["ProvisioningArtifactDetails"] = (
            capo_service_catalog.types.provisioning_artifact_details.serialize_aws_json_1_1(
                value["provisioning_artifact_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProvisioningArtifactsOutput:
    out: ListProvisioningArtifactsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningArtifactDetails") is not None:
        import capo_service_catalog.types.provisioning_artifact_details

        out["provisioning_artifact_details"] = (
            capo_service_catalog.types.provisioning_artifact_details.deserialize_aws_json_1_1(
                data["ProvisioningArtifactDetails"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProvisioningArtifactsOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_details" in value:
        import capo_service_catalog.types.provisioning_artifact_details

        out["ProvisioningArtifactDetails"] = (
            capo_service_catalog.types.provisioning_artifact_details.serialize_cbor(
                value["provisioning_artifact_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListProvisioningArtifactsOutput:
    out: ListProvisioningArtifactsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningArtifactDetails") is not None:
        import capo_service_catalog.types.provisioning_artifact_details

        out["provisioning_artifact_details"] = (
            capo_service_catalog.types.provisioning_artifact_details.deserialize_cbor(
                data["ProvisioningArtifactDetails"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
