"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListMetadataTransferJobsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError, SerializationError
from capo_iottwinmaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.metadata_transfer_job_state


class _ListMetadataTransferJobsFilter_workspaceId(TypedDict, closed=True):
    workspaceId: "capo_iottwinmaker.types.id.Id"


class _ListMetadataTransferJobsFilter_state(TypedDict, closed=True):
    state: (
        "capo_iottwinmaker.types.metadata_transfer_job_state.MetadataTransferJobState"
    )


ListMetadataTransferJobsFilter: TypeAlias = (
    _ListMetadataTransferJobsFilter_workspaceId
    | _ListMetadataTransferJobsFilter_state
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataTransferJobsFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ListMetadataTransferJobsFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "workspaceId" in value:
        return {"workspaceId": value["workspaceId"]}
    elif "state" in value:
        return {"state": value["state"]}
    else:
        raise SerializationError("ListMetadataTransferJobsFilter: no variant present")


def deserialize_json(data: dict) -> ListMetadataTransferJobsFilter:
    if data.get("workspaceId") is not None:
        return {"workspaceId": data["workspaceId"]}
    elif data.get("state") is not None:
        return {"state": data["state"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ListMetadataTransferJobsFilter: no recognized variant key"
        )
