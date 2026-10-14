"""Generated from Smithy shape ``com.amazonaws.workdocs#EntityNotExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import capo_workdocs.types.entity_id_list
    import capo_workdocs.types.error_message_type


class EntityNotExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_workdocs.types.error_message_type.ErrorMessageType"]
    entity_ids: NotRequired["capo_workdocs.types.entity_id_list.EntityIdList"]
    """<p>The IDs of the non-existent resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityNotExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "entity_ids" in value:
        import capo_workdocs.types.entity_id_list

        out["EntityIds"] = capo_workdocs.types.entity_id_list.serialize_json(
            value["entity_ids"]
        )
    return out


def deserialize_json(data: dict) -> EntityNotExistsException_:
    out: EntityNotExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("EntityIds") is not None:
        import capo_workdocs.types.entity_id_list

        out["entity_ids"] = capo_workdocs.types.entity_id_list.deserialize_json(
            data["EntityIds"]
        )
    return out


class EntityNotExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#EntityNotExistsException``."""

    code: str | None = "EntityNotExistsException"

    def __init__(
        self,
        data: EntityNotExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntityNotExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EntityNotExistsException":
        return cls(deserialize_json(data), message, response=response)
