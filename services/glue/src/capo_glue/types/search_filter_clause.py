"""Generated from Smithy shape ``com.amazonaws.glue#SearchFilterClause``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError, SerializationError
from capo_glue.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_glue.types.search_attribute_filter
    import capo_glue.types.search_filter_clause_list
    import capo_glue.types.search_map_filter


class SearchFilterClauseAndAllFiltersMember(TypedDict, closed=True):
    AndAllFilters: "capo_glue.types.search_filter_clause_list.SearchFilterClauseList"


class SearchFilterClauseOrAnyFiltersMember(TypedDict, closed=True):
    OrAnyFilters: "capo_glue.types.search_filter_clause_list.SearchFilterClauseList"


class SearchFilterClauseAttributeFilterMember(TypedDict, closed=True):
    AttributeFilter: "capo_glue.types.search_attribute_filter.SearchAttributeFilter"


class SearchFilterClauseMapFilterMember(TypedDict, closed=True):
    MapFilter: "capo_glue.types.search_map_filter.SearchMapFilter"


SearchFilterClause: TypeAlias = (
    SearchFilterClauseAndAllFiltersMember
    | SearchFilterClauseOrAnyFiltersMember
    | SearchFilterClauseAttributeFilterMember
    | SearchFilterClauseMapFilterMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFilterClause) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SearchFilterClause: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AndAllFilters" in value:
        import capo_glue.types.search_filter_clause_list

        return {
            "AndAllFilters": capo_glue.types.search_filter_clause_list.serialize_aws_json_1_1(
                value["AndAllFilters"]
            )
        }
    elif "OrAnyFilters" in value:
        import capo_glue.types.search_filter_clause_list

        return {
            "OrAnyFilters": capo_glue.types.search_filter_clause_list.serialize_aws_json_1_1(
                value["OrAnyFilters"]
            )
        }
    elif "AttributeFilter" in value:
        import capo_glue.types.search_attribute_filter

        return {
            "AttributeFilter": capo_glue.types.search_attribute_filter.serialize_aws_json_1_1(
                value["AttributeFilter"]
            )
        }
    elif "MapFilter" in value:
        import capo_glue.types.search_map_filter

        return {
            "MapFilter": capo_glue.types.search_map_filter.serialize_aws_json_1_1(
                value["MapFilter"]
            )
        }
    else:
        raise SerializationError("SearchFilterClause: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SearchFilterClause:
    if data.get("AndAllFilters") is not None:
        import capo_glue.types.search_filter_clause_list

        return {
            "AndAllFilters": capo_glue.types.search_filter_clause_list.deserialize_aws_json_1_1(
                data["AndAllFilters"]
            )
        }
    elif data.get("OrAnyFilters") is not None:
        import capo_glue.types.search_filter_clause_list

        return {
            "OrAnyFilters": capo_glue.types.search_filter_clause_list.deserialize_aws_json_1_1(
                data["OrAnyFilters"]
            )
        }
    elif data.get("AttributeFilter") is not None:
        import capo_glue.types.search_attribute_filter

        return {
            "AttributeFilter": capo_glue.types.search_attribute_filter.deserialize_aws_json_1_1(
                data["AttributeFilter"]
            )
        }
    elif data.get("MapFilter") is not None:
        import capo_glue.types.search_map_filter

        return {
            "MapFilter": capo_glue.types.search_map_filter.deserialize_aws_json_1_1(
                data["MapFilter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SearchFilterClause: no recognized variant key")
