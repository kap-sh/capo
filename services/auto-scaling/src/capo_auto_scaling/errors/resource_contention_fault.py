"""Generated from Smithy shape ``com.amazonaws.autoscaling#ResourceContentionFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element
from capo_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len255


class ResourceContentionFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceContentionFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> ResourceContentionFault_:
    out: ResourceContentionFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ResourceContentionFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.autoscaling#ResourceContentionFault``."""

    code: str | None = "ResourceContentionFault"

    def __init__(
        self,
        data: ResourceContentionFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceContentionFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceContentionFault":
        return cls(deserialize_query(el), message, response=response)
