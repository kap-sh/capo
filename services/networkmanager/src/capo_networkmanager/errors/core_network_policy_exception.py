"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_policy_error_list
    import capo_networkmanager.types.server_side_string


class CoreNetworkPolicyException_(TypedDict, closed=True):
    message: "capo_networkmanager.types.server_side_string.ServerSideString"
    errors: NotRequired[
        "capo_networkmanager.types.core_network_policy_error_list.CoreNetworkPolicyErrorList"
    ]
    """<p>Describes a core network policy exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "errors" in value:
        import capo_networkmanager.types.core_network_policy_error_list

        out["Errors"] = (
            capo_networkmanager.types.core_network_policy_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkPolicyException_:
    out: CoreNetworkPolicyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("CoreNetworkPolicyException_.message required")
    if data.get("Errors") is not None:
        import capo_networkmanager.types.core_network_policy_error_list

        out["errors"] = (
            capo_networkmanager.types.core_network_policy_error_list.deserialize_json(
                data["Errors"]
            )
        )
    return out


class CoreNetworkPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyException``."""

    code: str | None = "CoreNetworkPolicyException"

    def __init__(
        self,
        data: CoreNetworkPolicyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CoreNetworkPolicyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CoreNetworkPolicyException":
        return cls(deserialize_json(data), message, response=response)
