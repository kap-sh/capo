"""Generated from Smithy shape ``com.amazonaws.sts#RegionDisabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import ServiceError

if TYPE_CHECKING:
    import capo_sts.types.region_disabled_message


class RegionDisabledException_(TypedDict, closed=True):
    message: NotRequired["capo_sts.types.region_disabled_message.regionDisabledMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RegionDisabledException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> RegionDisabledException_:
    out: RegionDisabledException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class RegionDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#RegionDisabledException``."""

    code: str | None = "RegionDisabledException"

    def __init__(
        self,
        data: RegionDisabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RegionDisabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "RegionDisabledException":
        return cls(deserialize_query(el), message, response=response)
