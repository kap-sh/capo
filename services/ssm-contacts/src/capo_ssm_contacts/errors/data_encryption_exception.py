"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DataEncryptionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ssm_contacts.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.string


class DataEncryptionException_(TypedDict, closed=True):
    message: "capo_ssm_contacts.types.string.String"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataEncryptionException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataEncryptionException_:
    out: DataEncryptionException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("DataEncryptionException_.message required")
    return out


class DataEncryptionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmcontacts#DataEncryptionException``."""

    code: str | None = "DataEncryptionException"

    def __init__(
        self,
        data: DataEncryptionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DataEncryptionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DataEncryptionException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
