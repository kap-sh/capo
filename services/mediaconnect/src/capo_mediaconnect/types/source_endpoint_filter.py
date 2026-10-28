"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_type_list
    import capo_mediaconnect.types.string_list


class SourceEndpointFilterRegionNamesMember(TypedDict, closed=True):
    RegionNames: "capo_mediaconnect.types.string_list.StringList"


class SourceEndpointFilterSourceTypesMember(TypedDict, closed=True):
    SourceTypes: (
        "capo_mediaconnect.types.source_endpoint_type_list.SourceEndpointTypeList"
    )


class SourceEndpointFilterNameContainsMember(TypedDict, closed=True):
    NameContains: "capo_mediaconnect.types.string_list.StringList"


SourceEndpointFilter: TypeAlias = (
    SourceEndpointFilterRegionNamesMember
    | SourceEndpointFilterSourceTypesMember
    | SourceEndpointFilterNameContainsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceEndpointFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "RegionNames" in value:
        import capo_mediaconnect.types.string_list

        return {
            "regionNames": capo_mediaconnect.types.string_list.serialize_json(
                value["RegionNames"]
            )
        }
    elif "SourceTypes" in value:
        import capo_mediaconnect.types.source_endpoint_type_list

        return {
            "sourceTypes": capo_mediaconnect.types.source_endpoint_type_list.serialize_json(
                value["SourceTypes"]
            )
        }
    elif "NameContains" in value:
        import capo_mediaconnect.types.string_list

        return {
            "nameContains": capo_mediaconnect.types.string_list.serialize_json(
                value["NameContains"]
            )
        }
    else:
        raise SerializationError("SourceEndpointFilter: no variant present")


def deserialize_json(data: dict) -> SourceEndpointFilter:
    if data.get("regionNames") is not None:
        import capo_mediaconnect.types.string_list

        return {
            "RegionNames": capo_mediaconnect.types.string_list.deserialize_json(
                data["regionNames"]
            )
        }
    elif data.get("sourceTypes") is not None:
        import capo_mediaconnect.types.source_endpoint_type_list

        return {
            "SourceTypes": capo_mediaconnect.types.source_endpoint_type_list.deserialize_json(
                data["sourceTypes"]
            )
        }
    elif data.get("nameContains") is not None:
        import capo_mediaconnect.types.string_list

        return {
            "NameContains": capo_mediaconnect.types.string_list.deserialize_json(
                data["nameContains"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SourceEndpointFilter: no recognized variant key")
