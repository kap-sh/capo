"""Generated from Smithy shape ``com.amazonaws.lightsail#RegionSetupInProgressException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import ServiceError

if TYPE_CHECKING:
    import capo_lightsail.types.string


class RegionSetupInProgressException_(TypedDict, closed=True):
    code: NotRequired["capo_lightsail.types.string.string"]
    docs: NotRequired["capo_lightsail.types.string.string"]
    """<p> <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html">Regions and Availability Zones for Lightsail</a> </p>"""
    message: NotRequired["capo_lightsail.types.string.string"]
    tip: NotRequired["capo_lightsail.types.string.string"]
    """<p>Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionSetupInProgressException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "docs" in value:
        out["docs"] = value["docs"]
    if "message" in value:
        out["message"] = value["message"]
    if "tip" in value:
        out["tip"] = value["tip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionSetupInProgressException_:
    out: RegionSetupInProgressException_ = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("docs") is not None:
        out["docs"] = data["docs"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("tip") is not None:
        out["tip"] = data["tip"]
    return out


class RegionSetupInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lightsail#RegionSetupInProgressException``."""

    code: str | None = "RegionSetupInProgressException"

    def __init__(
        self, data: RegionSetupInProgressException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RegionSetupInProgressException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "RegionSetupInProgressException":
        return cls(deserialize_aws_json_1_1(data), message)
