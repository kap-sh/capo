"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomFieldsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.custom_fields_filter
    import capo_connectcases.types.custom_fields_filter_list
    import capo_connectcases.types.field_filter


class CustomFieldsFilterFieldMember(TypedDict, closed=True):
    field: "capo_connectcases.types.field_filter.FieldFilter"


CustomFieldsFilterNotMember = TypedDict(
    "CustomFieldsFilterNotMember",
    {
        "not": "capo_connectcases.types.custom_fields_filter.CustomFieldsFilter",
    },
    closed=True,
)


class CustomFieldsFilterAndAllMember(TypedDict, closed=True):
    andAll: "capo_connectcases.types.custom_fields_filter_list.CustomFieldsFilterList"


class CustomFieldsFilterOrAllMember(TypedDict, closed=True):
    orAll: "capo_connectcases.types.custom_fields_filter_list.CustomFieldsFilterList"


CustomFieldsFilter: TypeAlias = (
    CustomFieldsFilterFieldMember
    | CustomFieldsFilterNotMember
    | CustomFieldsFilterAndAllMember
    | CustomFieldsFilterOrAllMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomFieldsFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CustomFieldsFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "field" in value:
        import capo_connectcases.types.field_filter

        return {
            "field": capo_connectcases.types.field_filter.serialize_json(value["field"])
        }
    elif "not" in value:
        import capo_connectcases.types.custom_fields_filter

        return {
            "not": capo_connectcases.types.custom_fields_filter.serialize_json(
                value["not"]
            )
        }
    elif "andAll" in value:
        import capo_connectcases.types.custom_fields_filter_list

        return {
            "andAll": capo_connectcases.types.custom_fields_filter_list.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import capo_connectcases.types.custom_fields_filter_list

        return {
            "orAll": capo_connectcases.types.custom_fields_filter_list.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("CustomFieldsFilter: no variant present")


def deserialize_json(data: dict) -> CustomFieldsFilter:
    if data.get("field") is not None:
        import capo_connectcases.types.field_filter

        return {
            "field": capo_connectcases.types.field_filter.deserialize_json(
                data["field"]
            )
        }
    elif data.get("not") is not None:
        import capo_connectcases.types.custom_fields_filter

        return {
            "not": capo_connectcases.types.custom_fields_filter.deserialize_json(
                data["not"]
            )
        }
    elif data.get("andAll") is not None:
        import capo_connectcases.types.custom_fields_filter_list

        return {
            "andAll": capo_connectcases.types.custom_fields_filter_list.deserialize_json(
                data["andAll"]
            )
        }
    elif data.get("orAll") is not None:
        import capo_connectcases.types.custom_fields_filter_list

        return {
            "orAll": capo_connectcases.types.custom_fields_filter_list.deserialize_json(
                data["orAll"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CustomFieldsFilter: no recognized variant key")
