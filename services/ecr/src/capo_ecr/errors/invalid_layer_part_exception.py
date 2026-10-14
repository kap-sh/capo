"""Generated from Smithy shape ``com.amazonaws.ecr#InvalidLayerPartException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message
    import capo_ecr.types.part_size
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name
    import capo_ecr.types.upload_id


class InvalidLayerPartException_(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the exception.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the exception.</p>"""
    upload_id: NotRequired["capo_ecr.types.upload_id.UploadId"]
    """<p>The upload ID associated with the exception.</p>"""
    last_valid_byte_received: NotRequired["capo_ecr.types.part_size.PartSize"]
    """<p>The last valid byte received from the layer part upload that is associated with the exception.</p>"""
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]
    """<p>The error message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidLayerPartException_) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "upload_id" in value:
        out["uploadId"] = value["upload_id"]
    if "last_valid_byte_received" in value:
        out["lastValidByteReceived"] = value["last_valid_byte_received"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidLayerPartException_:
    out: InvalidLayerPartException_ = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    if data.get("lastValidByteReceived") is not None:
        out["last_valid_byte_received"] = data["lastValidByteReceived"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidLayerPartException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#InvalidLayerPartException``."""

    code: str | None = "InvalidLayerPartException"

    def __init__(
        self,
        data: InvalidLayerPartException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidLayerPartException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidLayerPartException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
