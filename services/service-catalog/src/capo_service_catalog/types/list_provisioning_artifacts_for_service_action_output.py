"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListProvisioningArtifactsForServiceActionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.provisioning_artifact_views


class ListProvisioningArtifactsForServiceActionOutput(TypedDict, closed=True):
    provisioning_artifact_views: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_views.ProvisioningArtifactViews"
    ]
    """<p>An array of objects with information about product views and provisioning artifacts.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListProvisioningArtifactsForServiceActionOutput,
) -> dict:
    out: dict = {}
    if "provisioning_artifact_views" in value:
        import capo_service_catalog.types.provisioning_artifact_views

        out["ProvisioningArtifactViews"] = (
            capo_service_catalog.types.provisioning_artifact_views.serialize_aws_json_1_1(
                value["provisioning_artifact_views"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListProvisioningArtifactsForServiceActionOutput:
    out: ListProvisioningArtifactsForServiceActionOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningArtifactViews") is not None:
        import capo_service_catalog.types.provisioning_artifact_views

        out["provisioning_artifact_views"] = (
            capo_service_catalog.types.provisioning_artifact_views.deserialize_aws_json_1_1(
                data["ProvisioningArtifactViews"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProvisioningArtifactsForServiceActionOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_views" in value:
        import capo_service_catalog.types.provisioning_artifact_views

        out["ProvisioningArtifactViews"] = (
            capo_service_catalog.types.provisioning_artifact_views.serialize_cbor(
                value["provisioning_artifact_views"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListProvisioningArtifactsForServiceActionOutput:
    out: ListProvisioningArtifactsForServiceActionOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningArtifactViews") is not None:
        import capo_service_catalog.types.provisioning_artifact_views

        out["provisioning_artifact_views"] = (
            capo_service_catalog.types.provisioning_artifact_views.deserialize_cbor(
                data["ProvisioningArtifactViews"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
