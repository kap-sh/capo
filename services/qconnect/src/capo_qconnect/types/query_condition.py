"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.query_condition_item


class _QueryCondition_single(TypedDict, closed=True):
    single: "capo_qconnect.types.query_condition_item.QueryConditionItem"


QueryCondition: TypeAlias = _QueryCondition_single | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: QueryCondition) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"QueryCondition: cannot serialize unknown variant {value.name!r}"
        )
    elif "single" in value:
        import capo_qconnect.types.query_condition_item

        return {
            "single": capo_qconnect.types.query_condition_item.serialize_json(
                value["single"]
            )
        }
    else:
        raise SerializationError("QueryCondition: no variant present")


def deserialize_json(data: dict) -> QueryCondition:
    if data.get("single") is not None:
        import capo_qconnect.types.query_condition_item

        return {
            "single": capo_qconnect.types.query_condition_item.deserialize_json(
                data["single"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("QueryCondition: no recognized variant key")
