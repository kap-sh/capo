"""Generated from Smithy shape ``com.amazonaws.iam#EntityTemporarilyUnmodifiableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import ServiceError

if TYPE_CHECKING:
    import capo_iam.types.entity_temporarily_unmodifiable_message


class EntityTemporarilyUnmodifiableException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_iam.types.entity_temporarily_unmodifiable_message.entityTemporarilyUnmodifiableMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: EntityTemporarilyUnmodifiableException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> EntityTemporarilyUnmodifiableException_:
    out: EntityTemporarilyUnmodifiableException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class EntityTemporarilyUnmodifiableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#EntityTemporarilyUnmodifiableException``."""

    code: str | None = "EntityTemporarilyUnmodifiableException"

    def __init__(
        self,
        data: EntityTemporarilyUnmodifiableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntityTemporarilyUnmodifiableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "EntityTemporarilyUnmodifiableException":
        return cls(deserialize_query(el), message, response=response)
