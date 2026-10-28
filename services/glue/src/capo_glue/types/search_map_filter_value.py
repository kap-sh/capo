"""Generated from Smithy shape ``com.amazonaws.glue#SearchMapFilterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError, SerializationError
from capo_glue.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_glue.types.search_filter_string_value


class SearchMapFilterValueStringValueMember(TypedDict, closed=True):
    StringValue: "capo_glue.types.search_filter_string_value.SearchFilterStringValue"


SearchMapFilterValue: TypeAlias = (
    SearchMapFilterValueStringValueMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchMapFilterValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SearchMapFilterValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    else:
        raise SerializationError("SearchMapFilterValue: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SearchMapFilterValue:
    if data.get("StringValue") is not None:
        return {"StringValue": data["StringValue"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SearchMapFilterValue: no recognized variant key")
