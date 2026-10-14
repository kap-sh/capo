"""Generated from Smithy shape ``com.amazonaws.ses#ConfigurationSetSendingPausedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name
    import capo_ses.types.error_message


class ConfigurationSetSendingPausedException_(TypedDict, closed=True):
    configuration_set_name: NotRequired[
        "capo_ses.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set for which email sending is disabled.</p>"""
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationSetSendingPausedException_,
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


def deserialize_query(el: Element) -> ConfigurationSetSendingPausedException_:
    out: ConfigurationSetSendingPausedException_ = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ConfigurationSetSendingPausedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#ConfigurationSetSendingPausedException``."""

    code: str | None = "ConfigurationSetSendingPausedException"

    def __init__(
        self,
        data: ConfigurationSetSendingPausedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConfigurationSetSendingPausedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "ConfigurationSetSendingPausedException":
        return cls(deserialize_query(el), message, response=response)
