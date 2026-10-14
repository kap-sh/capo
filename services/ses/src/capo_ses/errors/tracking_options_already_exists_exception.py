"""Generated from Smithy shape ``com.amazonaws.ses#TrackingOptionsAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name
    import capo_ses.types.error_message


class TrackingOptionsAlreadyExistsException_(TypedDict, closed=True):
    configuration_set_name: NotRequired[
        "capo_ses.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>Indicates that a TrackingOptions object already exists in the specified configuration set.</p>"""
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrackingOptionsAlreadyExistsException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "configuration_set_name" in value:
        pairs.append(
            (f"{key_prefix}ConfigurationSetName", str(value["configuration_set_name"]))
        )
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> TrackingOptionsAlreadyExistsException_:
    out: TrackingOptionsAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TrackingOptionsAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#TrackingOptionsAlreadyExistsException``."""

    code: str | None = "TrackingOptionsAlreadyExistsException"

    def __init__(
        self,
        data: TrackingOptionsAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TrackingOptionsAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "TrackingOptionsAlreadyExistsException":
        return cls(deserialize_query(el), message, response=response)
