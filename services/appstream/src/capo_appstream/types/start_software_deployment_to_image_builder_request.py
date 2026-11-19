"""Generated from Smithy shape ``com.amazonaws.appstream#StartSoftwareDeploymentToImageBuilderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.boolean
    import capo_appstream.types.name


class StartSoftwareDeploymentToImageBuilderRequest(TypedDict, closed=True):
    image_builder_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the target image builder instance.</p>"""
    retry_failed_deployments: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Whether to retry previously failed license included application deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSoftwareDeploymentToImageBuilderRequest) -> dict:
    out: dict = {}
    if "image_builder_name" in value:
        out["ImageBuilderName"] = value["image_builder_name"]
    if "retry_failed_deployments" in value:
        out["RetryFailedDeployments"] = value["retry_failed_deployments"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> StartSoftwareDeploymentToImageBuilderRequest:
    out: StartSoftwareDeploymentToImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilderName") is not None:
        out["image_builder_name"] = data["ImageBuilderName"]
    if data.get("RetryFailedDeployments") is not None:
        out["retry_failed_deployments"] = data["RetryFailedDeployments"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartSoftwareDeploymentToImageBuilderRequest) -> dict:
    out: dict = {}
    if "image_builder_name" in value:
        out["ImageBuilderName"] = value["image_builder_name"]
    if "retry_failed_deployments" in value:
        out["RetryFailedDeployments"] = value["retry_failed_deployments"]
    return out


def deserialize_cbor(data: dict) -> StartSoftwareDeploymentToImageBuilderRequest:
    out: StartSoftwareDeploymentToImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilderName") is not None:
        out["image_builder_name"] = data["ImageBuilderName"]
    if data.get("RetryFailedDeployments") is not None:
        out["retry_failed_deployments"] = data["RetryFailedDeployments"]
    return out
