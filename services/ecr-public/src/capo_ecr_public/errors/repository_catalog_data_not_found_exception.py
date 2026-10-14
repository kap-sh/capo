"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RepositoryCatalogDataNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr_public.types.exception_message


class RepositoryCatalogDataNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr_public.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryCatalogDataNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryCatalogDataNotFoundException_:
    out: RepositoryCatalogDataNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class RepositoryCatalogDataNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#RepositoryCatalogDataNotFoundException``."""

    code: str | None = "RepositoryCatalogDataNotFoundException"

    def __init__(
        self,
        data: RepositoryCatalogDataNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RepositoryCatalogDataNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RepositoryCatalogDataNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
