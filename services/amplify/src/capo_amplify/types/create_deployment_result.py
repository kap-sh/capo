"""Generated from Smithy shape ``com.amazonaws.amplify#CreateDeploymentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.file_upload_urls
    import capo_amplify.types.job_id
    import capo_amplify.types.upload_url


class CreateDeploymentResult(TypedDict, closed=True):
    job_id: NotRequired["capo_amplify.types.job_id.JobId"]
    """<p> The job ID for this deployment. will supply to start deployment api. </p>"""
    file_upload_urls: "capo_amplify.types.file_upload_urls.FileUploadUrls"
    """<p> When the <code>fileMap</code> argument is provided in the request, <code>fileUploadUrls</code> will contain a map of file names to upload URLs. </p>"""
    zip_upload_url: "capo_amplify.types.upload_url.UploadUrl"
    """<p> When the <code>fileMap</code> argument is not provided in the request, this <code>zipUploadUrl</code> is returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentResult) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    import capo_amplify.types.file_upload_urls

    out["fileUploadUrls"] = capo_amplify.types.file_upload_urls.serialize_json(
        value["file_upload_urls"]
    )
    out["zipUploadUrl"] = value["zip_upload_url"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentResult:
    out: CreateDeploymentResult = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("fileUploadUrls") is not None:
        import capo_amplify.types.file_upload_urls

        out["file_upload_urls"] = capo_amplify.types.file_upload_urls.deserialize_json(
            data["fileUploadUrls"]
        )
    else:
        out["file_upload_urls"] = {}
    if data.get("zipUploadUrl") is not None:
        out["zip_upload_url"] = data["zipUploadUrl"]
    else:
        out["zip_upload_url"] = ""
    return out
