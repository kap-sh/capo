"""Generated from Smithy shape ``com.amazonaws.appconfig#BadRequestDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_appconfig.errors import DeserializationError, SerializationError
from capo_appconfig.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_appconfig.types.invalid_configuration_detail_list


class BadRequestDetailsInvalidConfigurationMember(TypedDict, closed=True):
    InvalidConfiguration: "capo_appconfig.types.invalid_configuration_detail_list.InvalidConfigurationDetailList"


BadRequestDetails: TypeAlias = (
    BadRequestDetailsInvalidConfigurationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BadRequestDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "InvalidConfiguration" in value:
        import capo_appconfig.types.invalid_configuration_detail_list

        return {
            "InvalidConfiguration": capo_appconfig.types.invalid_configuration_detail_list.serialize_json(
                value["InvalidConfiguration"]
            )
        }
    else:
        raise SerializationError("BadRequestDetails: no variant present")


def deserialize_json(data: dict) -> BadRequestDetails:
    if data.get("InvalidConfiguration") is not None:
        import capo_appconfig.types.invalid_configuration_detail_list

        return {
            "InvalidConfiguration": capo_appconfig.types.invalid_configuration_detail_list.deserialize_json(
                data["InvalidConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BadRequestDetails: no recognized variant key")
