"""Generated from Smithy shape ``com.amazonaws.ssm#HierarchyLevelLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class HierarchyLevelLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]
    """<p>A hierarchy can have a maximum of 15 levels. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html#sysman-parameter-name-constraints">About requirements and constraints for parameter names</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HierarchyLevelLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HierarchyLevelLimitExceededException_:
    out: HierarchyLevelLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class HierarchyLevelLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#HierarchyLevelLimitExceededException``."""

    code: str | None = "HierarchyLevelLimitExceededException"

    def __init__(
        self, data: HierarchyLevelLimitExceededException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HierarchyLevelLimitExceededException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "HierarchyLevelLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message)
