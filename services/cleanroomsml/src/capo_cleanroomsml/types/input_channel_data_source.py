"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InputChannelDataSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError, SerializationError
from capo_cleanroomsml.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanroomsml.types.protected_query_input_parameters


class _InputChannelDataSource_protectedQueryInputParameters(TypedDict, closed=True):
    protectedQueryInputParameters: "capo_cleanroomsml.types.protected_query_input_parameters.ProtectedQueryInputParameters"


InputChannelDataSource: TypeAlias = (
    _InputChannelDataSource_protectedQueryInputParameters | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: InputChannelDataSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"InputChannelDataSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "protectedQueryInputParameters" in value:
        import capo_cleanroomsml.types.protected_query_input_parameters

        return {
            "protectedQueryInputParameters": capo_cleanroomsml.types.protected_query_input_parameters.serialize_json(
                value["protectedQueryInputParameters"]
            )
        }
    else:
        raise SerializationError("InputChannelDataSource: no variant present")


def deserialize_json(data: dict) -> InputChannelDataSource:
    if data.get("protectedQueryInputParameters") is not None:
        import capo_cleanroomsml.types.protected_query_input_parameters

        return {
            "protectedQueryInputParameters": capo_cleanroomsml.types.protected_query_input_parameters.deserialize_json(
                data["protectedQueryInputParameters"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("InputChannelDataSource: no recognized variant key")


def redact_sensitive(value: InputChannelDataSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "protectedQueryInputParameters" in value:
        import capo_cleanroomsml.types.protected_query_input_parameters

        out["protectedQueryInputParameters"] = (
            capo_cleanroomsml.types.protected_query_input_parameters.redact_sensitive(
                value["protectedQueryInputParameters"]
            )
        )
    return out
