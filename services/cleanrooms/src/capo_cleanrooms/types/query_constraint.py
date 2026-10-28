"""Generated from Smithy shape ``com.amazonaws.cleanrooms#QueryConstraint``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.query_constraint_require_overlap


class QueryConstraintRequireOverlapMember(TypedDict, closed=True):
    requireOverlap: "capo_cleanrooms.types.query_constraint_require_overlap.QueryConstraintRequireOverlap"


QueryConstraint: TypeAlias = QueryConstraintRequireOverlapMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: QueryConstraint) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"QueryConstraint: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "requireOverlap" in value:
        import capo_cleanrooms.types.query_constraint_require_overlap

        return {
            "requireOverlap": capo_cleanrooms.types.query_constraint_require_overlap.serialize_json(
                value["requireOverlap"]
            )
        }
    else:
        raise SerializationError("QueryConstraint: no variant present")


def deserialize_json(data: dict) -> QueryConstraint:
    if data.get("requireOverlap") is not None:
        import capo_cleanrooms.types.query_constraint_require_overlap

        return {
            "requireOverlap": capo_cleanrooms.types.query_constraint_require_overlap.deserialize_json(
                data["requireOverlap"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("QueryConstraint: no recognized variant key")
