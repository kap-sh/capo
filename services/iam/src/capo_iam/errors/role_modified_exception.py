"""Generated from Smithy shape ``com.amazonaws.iam#RoleModifiedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import ServiceError

if TYPE_CHECKING:
    import capo_iam.types.role_modified_message


class RoleModifiedException_(TypedDict, closed=True):
    message: NotRequired["capo_iam.types.role_modified_message.roleModifiedMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RoleModifiedException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> RoleModifiedException_:
    out: RoleModifiedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class RoleModifiedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#RoleModifiedException``."""

    code: str | None = "RoleModifiedException"

    def __init__(
        self,
        data: RoleModifiedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RoleModifiedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "RoleModifiedException":
        return cls(deserialize_query(el), message, response=response)
