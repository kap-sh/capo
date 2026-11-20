"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#StructuredDataSource``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError, SerializationError
from capo_opensearchmemory.types._unknown import UnknownUnionMember


class StructuredDataSourceJsonMember(TypedDict, closed=True):
    json: "object"


StructuredDataSource: TypeAlias = StructuredDataSourceJsonMember | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredDataSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"StructuredDataSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("StructuredDataSource: no variant present")


def deserialize_aws_json_1_0(data: dict) -> StructuredDataSource:
    if data.get("json") is not None:
        return {"json": data["json"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("StructuredDataSource: no recognized variant key")
