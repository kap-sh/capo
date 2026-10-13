"""Generated from Smithy shape ``com.amazonaws.bedrock#RequestMetadataFilters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.request_metadata_filters_list
    import capo_bedrock.types.request_metadata_map


class _RequestMetadataFilters_equals(TypedDict, closed=True):
    equals: "capo_bedrock.types.request_metadata_map.RequestMetadataMap"


class _RequestMetadataFilters_notEquals(TypedDict, closed=True):
    notEquals: "capo_bedrock.types.request_metadata_map.RequestMetadataMap"


class _RequestMetadataFilters_andAll(TypedDict, closed=True):
    andAll: (
        "capo_bedrock.types.request_metadata_filters_list.RequestMetadataFiltersList"
    )


class _RequestMetadataFilters_orAll(TypedDict, closed=True):
    orAll: "capo_bedrock.types.request_metadata_filters_list.RequestMetadataFiltersList"


RequestMetadataFilters: TypeAlias = (
    _RequestMetadataFilters_equals
    | _RequestMetadataFilters_notEquals
    | _RequestMetadataFilters_andAll
    | _RequestMetadataFilters_orAll
)


# --- restJson1 ser/de ---
def serialize_json(value: RequestMetadataFilters) -> dict:
    if "equals" in value:
        import capo_bedrock.types.request_metadata_map

        return {
            "equals": capo_bedrock.types.request_metadata_map.serialize_json(
                value["equals"]
            )
        }
    elif "notEquals" in value:
        import capo_bedrock.types.request_metadata_map

        return {
            "notEquals": capo_bedrock.types.request_metadata_map.serialize_json(
                value["notEquals"]
            )
        }
    elif "andAll" in value:
        import capo_bedrock.types.request_metadata_filters_list

        return {
            "andAll": capo_bedrock.types.request_metadata_filters_list.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import capo_bedrock.types.request_metadata_filters_list

        return {
            "orAll": capo_bedrock.types.request_metadata_filters_list.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("RequestMetadataFilters: no variant present")


def deserialize_json(data: dict) -> RequestMetadataFilters:
    if data.get("equals") is not None:
        import capo_bedrock.types.request_metadata_map

        return {
            "equals": capo_bedrock.types.request_metadata_map.deserialize_json(
                data["equals"]
            )
        }
    elif data.get("notEquals") is not None:
        import capo_bedrock.types.request_metadata_map

        return {
            "notEquals": capo_bedrock.types.request_metadata_map.deserialize_json(
                data["notEquals"]
            )
        }
    elif data.get("andAll") is not None:
        import capo_bedrock.types.request_metadata_filters_list

        return {
            "andAll": capo_bedrock.types.request_metadata_filters_list.deserialize_json(
                data["andAll"]
            )
        }
    elif data.get("orAll") is not None:
        import capo_bedrock.types.request_metadata_filters_list

        return {
            "orAll": capo_bedrock.types.request_metadata_filters_list.deserialize_json(
                data["orAll"]
            )
        }
    else:
        raise DeserializationError("RequestMetadataFilters: no recognized variant key")


def redact_sensitive(value: RequestMetadataFilters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "equals" in value:
        out["equals"] = "*** Sensitive Data Redacted ***"
    if "notEquals" in value:
        out["notEquals"] = "*** Sensitive Data Redacted ***"
    if "andAll" in value:
        import capo_bedrock.types.request_metadata_filters_list

        out["andAll"] = (
            capo_bedrock.types.request_metadata_filters_list.redact_sensitive(
                value["andAll"]
            )
        )
    if "orAll" in value:
        import capo_bedrock.types.request_metadata_filters_list

        out["orAll"] = (
            capo_bedrock.types.request_metadata_filters_list.redact_sensitive(
                value["orAll"]
            )
        )
    return out
