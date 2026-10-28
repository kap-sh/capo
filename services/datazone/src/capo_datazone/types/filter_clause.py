"""Generated from Smithy shape ``com.amazonaws.datazone#FilterClause``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.filter
    import capo_datazone.types.filter_list


class FilterClauseFilterMember(TypedDict, closed=True):
    filter: "capo_datazone.types.filter.Filter"


FilterClauseAndMember = TypedDict(
    "FilterClauseAndMember",
    {
        "and": "capo_datazone.types.filter_list.FilterList",
    },
    closed=True,
)
FilterClauseOrMember = TypedDict(
    "FilterClauseOrMember",
    {
        "or": "capo_datazone.types.filter_list.FilterList",
    },
    closed=True,
)

FilterClause: TypeAlias = (
    FilterClauseFilterMember
    | FilterClauseAndMember
    | FilterClauseOrMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FilterClause) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FilterClause: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "filter" in value:
        import capo_datazone.types.filter

        return {"filter": capo_datazone.types.filter.serialize_json(value["filter"])}
    elif "and" in value:
        import capo_datazone.types.filter_list

        return {"and": capo_datazone.types.filter_list.serialize_json(value["and"])}
    elif "or" in value:
        import capo_datazone.types.filter_list

        return {"or": capo_datazone.types.filter_list.serialize_json(value["or"])}
    else:
        raise SerializationError("FilterClause: no variant present")


def deserialize_json(data: dict) -> FilterClause:
    if data.get("filter") is not None:
        import capo_datazone.types.filter

        return {"filter": capo_datazone.types.filter.deserialize_json(data["filter"])}
    elif data.get("and") is not None:
        import capo_datazone.types.filter_list

        return {"and": capo_datazone.types.filter_list.deserialize_json(data["and"])}
    elif data.get("or") is not None:
        import capo_datazone.types.filter_list

        return {"or": capo_datazone.types.filter_list.deserialize_json(data["or"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FilterClause: no recognized variant key")
