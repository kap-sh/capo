"""Generated from Smithy shape ``com.amazonaws.redshiftdata#QueryRecords``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift_data.errors import DeserializationError, SerializationError
from capo_redshift_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_redshift_data.types.string


class _QueryRecords_CSVRecords(TypedDict, closed=True):
    CSVRecords: "capo_redshift_data.types.string.String"


QueryRecords: TypeAlias = _QueryRecords_CSVRecords | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryRecords) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"QueryRecords: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "CSVRecords" in value:
        return {"CSVRecords": value["CSVRecords"]}
    else:
        raise SerializationError("QueryRecords: no variant present")


def deserialize_aws_json_1_1(data: dict) -> QueryRecords:
    if data.get("CSVRecords") is not None:
        return {"CSVRecords": data["CSVRecords"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("QueryRecords: no recognized variant key")
