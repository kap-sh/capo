"""Generated from Smithy shape ``com.amazonaws.voiceid#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_voice_id.errors import ServiceError

if TYPE_CHECKING:
    import capo_voice_id.types.conflict_type
    import capo_voice_id.types.string


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_voice_id.types.string.String"]
    conflict_type: NotRequired["capo_voice_id.types.conflict_type.ConflictType"]
    """<p>The type of conflict which caused a ConflictException. Possible types and the corresponding error messages are as follows:</p> <ul> <li> <p> <code>DOMAIN_NOT_ACTIVE</code>: The domain is not active.</p> </li> <li> <p> <code>CANNOT_CHANGE_SPEAKER_AFTER_ENROLLMENT</code>: You cannot change the speaker ID after an enrollment has been requested.</p> </li> <li> <p> <code>ENROLLMENT_ALREADY_EXISTS</code>: There is already an enrollment for this session.</p> </li> <li> <p> <code>SPEAKER_NOT_SET</code>: You must set the speaker ID before requesting an enrollment.</p> </li> <li> <p> <code>SPEAKER_OPTED_OUT</code>: You cannot request an enrollment for an opted out speaker.</p> </li> <li> <p> <code>CONCURRENT_CHANGES</code>: The request could not be processed as the resource was modified by another request during execution.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "conflict_type" in value:
        out["ConflictType"] = value["conflict_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ConflictType") is not None:
        out["conflict_type"] = data["ConflictType"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.voiceid#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
