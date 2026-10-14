"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationAlreadyExists``."""

import zapros
from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class AssociationAlreadyExists_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationAlreadyExists_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationAlreadyExists_:
    out: AssociationAlreadyExists_ = {}  # type: ignore[typeddict-item]
    return out


class AssociationAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AssociationAlreadyExists``."""

    code: str | None = "AssociationAlreadyExists"

    def __init__(
        self,
        data: AssociationAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AssociationAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AssociationAlreadyExists":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
