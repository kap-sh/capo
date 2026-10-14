"""Generated from Smithy shape ``com.amazonaws.neptune#SubnetAlreadyInUse``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element
from capo_neptune.errors import ServiceError

if TYPE_CHECKING:
    import capo_neptune.types.exception_message


class SubnetAlreadyInUse_(TypedDict, closed=True):
    message: NotRequired["capo_neptune.types.exception_message.ExceptionMessage"]
    """<p>A message describing the details of the problem.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetAlreadyInUse_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> SubnetAlreadyInUse_:
    out: SubnetAlreadyInUse_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class SubnetAlreadyInUse(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptune#SubnetAlreadyInUse``."""

    code: str | None = "SubnetAlreadyInUse"

    def __init__(
        self,
        data: SubnetAlreadyInUse_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubnetAlreadyInUse",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "SubnetAlreadyInUse":
        return cls(deserialize_query(el), message, response=response)
