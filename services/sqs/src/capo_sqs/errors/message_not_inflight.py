"""Generated from Smithy shape ``com.amazonaws.sqs#MessageNotInflight``."""

import zapros
from typing_extensions import TypedDict

from capo_sqs.errors import ServiceError


class MessageNotInflight_(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageNotInflight_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageNotInflight_:
    out: MessageNotInflight_ = {}  # type: ignore[typeddict-item]
    return out


class MessageNotInflight(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#MessageNotInflight``."""

    code: str | None = "MessageNotInflight"

    def __init__(
        self,
        data: MessageNotInflight_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MessageNotInflight",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MessageNotInflight":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
