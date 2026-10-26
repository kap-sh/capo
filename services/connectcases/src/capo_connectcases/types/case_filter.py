"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.case_filter
    import capo_connectcases.types.case_filter_list
    import capo_connectcases.types.field_filter
    import capo_connectcases.types.tag_filter


class _CaseFilter_field(TypedDict, closed=True):
    field: "capo_connectcases.types.field_filter.FieldFilter"


_CaseFilter_not = TypedDict(
    "_CaseFilter_not",
    {
        "not": "capo_connectcases.types.case_filter.CaseFilter",
    },
    closed=True,
)


class _CaseFilter_tag(TypedDict, closed=True):
    tag: "capo_connectcases.types.tag_filter.TagFilter"


class _CaseFilter_andAll(TypedDict, closed=True):
    andAll: "capo_connectcases.types.case_filter_list.CaseFilterList"


class _CaseFilter_orAll(TypedDict, closed=True):
    orAll: "capo_connectcases.types.case_filter_list.CaseFilterList"


CaseFilter: TypeAlias = (
    _CaseFilter_field
    | _CaseFilter_not
    | _CaseFilter_tag
    | _CaseFilter_andAll
    | _CaseFilter_orAll
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CaseFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CaseFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "field" in value:
        import capo_connectcases.types.field_filter

        return {
            "field": capo_connectcases.types.field_filter.serialize_json(value["field"])
        }
    elif "not" in value:
        import capo_connectcases.types.case_filter

        return {"not": capo_connectcases.types.case_filter.serialize_json(value["not"])}
    elif "tag" in value:
        import capo_connectcases.types.tag_filter

        return {"tag": capo_connectcases.types.tag_filter.serialize_json(value["tag"])}
    elif "andAll" in value:
        import capo_connectcases.types.case_filter_list

        return {
            "andAll": capo_connectcases.types.case_filter_list.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import capo_connectcases.types.case_filter_list

        return {
            "orAll": capo_connectcases.types.case_filter_list.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("CaseFilter: no variant present")


def deserialize_json(data: dict) -> CaseFilter:
    if data.get("field") is not None:
        import capo_connectcases.types.field_filter

        return {
            "field": capo_connectcases.types.field_filter.deserialize_json(
                data["field"]
            )
        }
    elif data.get("not") is not None:
        import capo_connectcases.types.case_filter

        return {
            "not": capo_connectcases.types.case_filter.deserialize_json(data["not"])
        }
    elif data.get("tag") is not None:
        import capo_connectcases.types.tag_filter

        return {"tag": capo_connectcases.types.tag_filter.deserialize_json(data["tag"])}
    elif data.get("andAll") is not None:
        import capo_connectcases.types.case_filter_list

        return {
            "andAll": capo_connectcases.types.case_filter_list.deserialize_json(
                data["andAll"]
            )
        }
    elif data.get("orAll") is not None:
        import capo_connectcases.types.case_filter_list

        return {
            "orAll": capo_connectcases.types.case_filter_list.deserialize_json(
                data["orAll"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CaseFilter: no recognized variant key")
