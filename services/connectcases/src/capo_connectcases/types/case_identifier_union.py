"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseIdentifierUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.reference_id


class CaseIdentifierUnionCaseIdMember(TypedDict, closed=True):
    caseId: "capo_connectcases.types.case_id.CaseId"


class CaseIdentifierUnionReferenceIdMember(TypedDict, closed=True):
    referenceId: "capo_connectcases.types.reference_id.ReferenceId"


CaseIdentifierUnion: TypeAlias = (
    CaseIdentifierUnionCaseIdMember
    | CaseIdentifierUnionReferenceIdMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CaseIdentifierUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CaseIdentifierUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "caseId" in value:
        return {"caseId": value["caseId"]}
    elif "referenceId" in value:
        return {"referenceId": value["referenceId"]}
    else:
        raise SerializationError("CaseIdentifierUnion: no variant present")


def deserialize_json(data: dict) -> CaseIdentifierUnion:
    if data.get("caseId") is not None:
        return {"caseId": data["caseId"]}
    elif data.get("referenceId") is not None:
        return {"referenceId": data["referenceId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CaseIdentifierUnion: no recognized variant key")
