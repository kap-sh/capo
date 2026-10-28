"""Generated from Smithy shape ``com.amazonaws.lakeformation#RedshiftScopeUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError, SerializationError
from capo_lakeformation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_lakeformation.types.redshift_connect


class RedshiftScopeUnionRedshiftConnectMember(TypedDict, closed=True):
    RedshiftConnect: "capo_lakeformation.types.redshift_connect.RedshiftConnect"


RedshiftScopeUnion: TypeAlias = (
    RedshiftScopeUnionRedshiftConnectMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftScopeUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RedshiftScopeUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "RedshiftConnect" in value:
        import capo_lakeformation.types.redshift_connect

        return {
            "RedshiftConnect": capo_lakeformation.types.redshift_connect.serialize_json(
                value["RedshiftConnect"]
            )
        }
    else:
        raise SerializationError("RedshiftScopeUnion: no variant present")


def deserialize_json(data: dict) -> RedshiftScopeUnion:
    if data.get("RedshiftConnect") is not None:
        import capo_lakeformation.types.redshift_connect

        return {
            "RedshiftConnect": capo_lakeformation.types.redshift_connect.deserialize_json(
                data["RedshiftConnect"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RedshiftScopeUnion: no recognized variant key")
