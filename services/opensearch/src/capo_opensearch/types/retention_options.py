"""Generated from Smithy shape ``com.amazonaws.opensearch#RetentionOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError, SerializationError
from capo_opensearch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearch.types.integer_class
    import capo_opensearch.types.retention_action


class RetentionOptionsRetentionInHoursMember(TypedDict, closed=True):
    RetentionInHours: "capo_opensearch.types.integer_class.IntegerClass"


class RetentionOptionsRetentionActionMember(TypedDict, closed=True):
    RetentionAction: "capo_opensearch.types.retention_action.RetentionAction"


RetentionOptions: TypeAlias = (
    RetentionOptionsRetentionInHoursMember
    | RetentionOptionsRetentionActionMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RetentionOptions) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RetentionOptions: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "RetentionInHours" in value:
        return {"RetentionInHours": value["RetentionInHours"]}
    elif "RetentionAction" in value:
        import capo_opensearch.types.retention_action

        return {
            "RetentionAction": capo_opensearch.types.retention_action.serialize_json(
                value["RetentionAction"]
            )
        }
    else:
        raise SerializationError("RetentionOptions: no variant present")


def deserialize_json(data: dict) -> RetentionOptions:
    if data.get("RetentionInHours") is not None:
        return {"RetentionInHours": data["RetentionInHours"]}
    elif data.get("RetentionAction") is not None:
        import capo_opensearch.types.retention_action

        return {
            "RetentionAction": capo_opensearch.types.retention_action.deserialize_json(
                data["RetentionAction"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RetentionOptions: no recognized variant key")
