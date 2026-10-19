"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacityFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.capacity_bytes_range_filter
    import capo_quicksight.types.user_name_or_email_filter


class _UserIndexCapacityFilter_userNameOrEmail(TypedDict, closed=True):
    userNameOrEmail: (
        "capo_quicksight.types.user_name_or_email_filter.UserNameOrEmailFilter"
    )


class _UserIndexCapacityFilter_totalCapacityBytes(TypedDict, closed=True):
    totalCapacityBytes: (
        "capo_quicksight.types.capacity_bytes_range_filter.CapacityBytesRangeFilter"
    )


UserIndexCapacityFilter: TypeAlias = (
    _UserIndexCapacityFilter_userNameOrEmail
    | _UserIndexCapacityFilter_totalCapacityBytes
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UserIndexCapacityFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"UserIndexCapacityFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "userNameOrEmail" in value:
        import capo_quicksight.types.user_name_or_email_filter

        return {
            "userNameOrEmail": capo_quicksight.types.user_name_or_email_filter.serialize_json(
                value["userNameOrEmail"]
            )
        }
    elif "totalCapacityBytes" in value:
        import capo_quicksight.types.capacity_bytes_range_filter

        return {
            "totalCapacityBytes": capo_quicksight.types.capacity_bytes_range_filter.serialize_json(
                value["totalCapacityBytes"]
            )
        }
    else:
        raise SerializationError("UserIndexCapacityFilter: no variant present")


def deserialize_json(data: dict) -> UserIndexCapacityFilter:
    if data.get("userNameOrEmail") is not None:
        import capo_quicksight.types.user_name_or_email_filter

        return {
            "userNameOrEmail": capo_quicksight.types.user_name_or_email_filter.deserialize_json(
                data["userNameOrEmail"]
            )
        }
    elif data.get("totalCapacityBytes") is not None:
        import capo_quicksight.types.capacity_bytes_range_filter

        return {
            "totalCapacityBytes": capo_quicksight.types.capacity_bytes_range_filter.deserialize_json(
                data["totalCapacityBytes"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("UserIndexCapacityFilter: no recognized variant key")
