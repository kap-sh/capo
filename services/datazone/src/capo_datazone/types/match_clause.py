"""Generated from Smithy shape ``com.amazonaws.datazone#MatchClause``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.entity_pattern
    import capo_datazone.types.relation_pattern


class _MatchClause_relationPattern(TypedDict, closed=True):
    relationPattern: "capo_datazone.types.relation_pattern.RelationPattern"


class _MatchClause_entityPattern(TypedDict, closed=True):
    entityPattern: "capo_datazone.types.entity_pattern.EntityPattern"


MatchClause: TypeAlias = (
    _MatchClause_relationPattern | _MatchClause_entityPattern | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MatchClause) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MatchClause: cannot serialize unknown variant {value.name!r}"
        )
    elif "relationPattern" in value:
        import capo_datazone.types.relation_pattern

        return {
            "relationPattern": capo_datazone.types.relation_pattern.serialize_json(
                value["relationPattern"]
            )
        }
    elif "entityPattern" in value:
        import capo_datazone.types.entity_pattern

        return {
            "entityPattern": capo_datazone.types.entity_pattern.serialize_json(
                value["entityPattern"]
            )
        }
    else:
        raise SerializationError("MatchClause: no variant present")


def deserialize_json(data: dict) -> MatchClause:
    if data.get("relationPattern") is not None:
        import capo_datazone.types.relation_pattern

        return {
            "relationPattern": capo_datazone.types.relation_pattern.deserialize_json(
                data["relationPattern"]
            )
        }
    elif data.get("entityPattern") is not None:
        import capo_datazone.types.entity_pattern

        return {
            "entityPattern": capo_datazone.types.entity_pattern.deserialize_json(
                data["entityPattern"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("MatchClause: no recognized variant key")
