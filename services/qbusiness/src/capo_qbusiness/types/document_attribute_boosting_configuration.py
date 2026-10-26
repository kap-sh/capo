"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeBoostingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.date_attribute_boosting_configuration
    import capo_qbusiness.types.number_attribute_boosting_configuration
    import capo_qbusiness.types.string_attribute_boosting_configuration
    import capo_qbusiness.types.string_list_attribute_boosting_configuration


class _DocumentAttributeBoostingConfiguration_numberConfiguration(
    TypedDict, closed=True
):
    numberConfiguration: "capo_qbusiness.types.number_attribute_boosting_configuration.NumberAttributeBoostingConfiguration"


class _DocumentAttributeBoostingConfiguration_stringConfiguration(
    TypedDict, closed=True
):
    stringConfiguration: "capo_qbusiness.types.string_attribute_boosting_configuration.StringAttributeBoostingConfiguration"


class _DocumentAttributeBoostingConfiguration_dateConfiguration(TypedDict, closed=True):
    dateConfiguration: "capo_qbusiness.types.date_attribute_boosting_configuration.DateAttributeBoostingConfiguration"


class _DocumentAttributeBoostingConfiguration_stringListConfiguration(
    TypedDict, closed=True
):
    stringListConfiguration: "capo_qbusiness.types.string_list_attribute_boosting_configuration.StringListAttributeBoostingConfiguration"


DocumentAttributeBoostingConfiguration: TypeAlias = (
    _DocumentAttributeBoostingConfiguration_numberConfiguration
    | _DocumentAttributeBoostingConfiguration_stringConfiguration
    | _DocumentAttributeBoostingConfiguration_dateConfiguration
    | _DocumentAttributeBoostingConfiguration_stringListConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeBoostingConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DocumentAttributeBoostingConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "numberConfiguration" in value:
        import capo_qbusiness.types.number_attribute_boosting_configuration

        return {
            "numberConfiguration": capo_qbusiness.types.number_attribute_boosting_configuration.serialize_json(
                value["numberConfiguration"]
            )
        }
    elif "stringConfiguration" in value:
        import capo_qbusiness.types.string_attribute_boosting_configuration

        return {
            "stringConfiguration": capo_qbusiness.types.string_attribute_boosting_configuration.serialize_json(
                value["stringConfiguration"]
            )
        }
    elif "dateConfiguration" in value:
        import capo_qbusiness.types.date_attribute_boosting_configuration

        return {
            "dateConfiguration": capo_qbusiness.types.date_attribute_boosting_configuration.serialize_json(
                value["dateConfiguration"]
            )
        }
    elif "stringListConfiguration" in value:
        import capo_qbusiness.types.string_list_attribute_boosting_configuration

        return {
            "stringListConfiguration": capo_qbusiness.types.string_list_attribute_boosting_configuration.serialize_json(
                value["stringListConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "DocumentAttributeBoostingConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> DocumentAttributeBoostingConfiguration:
    if data.get("numberConfiguration") is not None:
        import capo_qbusiness.types.number_attribute_boosting_configuration

        return {
            "numberConfiguration": capo_qbusiness.types.number_attribute_boosting_configuration.deserialize_json(
                data["numberConfiguration"]
            )
        }
    elif data.get("stringConfiguration") is not None:
        import capo_qbusiness.types.string_attribute_boosting_configuration

        return {
            "stringConfiguration": capo_qbusiness.types.string_attribute_boosting_configuration.deserialize_json(
                data["stringConfiguration"]
            )
        }
    elif data.get("dateConfiguration") is not None:
        import capo_qbusiness.types.date_attribute_boosting_configuration

        return {
            "dateConfiguration": capo_qbusiness.types.date_attribute_boosting_configuration.deserialize_json(
                data["dateConfiguration"]
            )
        }
    elif data.get("stringListConfiguration") is not None:
        import capo_qbusiness.types.string_list_attribute_boosting_configuration

        return {
            "stringListConfiguration": capo_qbusiness.types.string_list_attribute_boosting_configuration.deserialize_json(
                data["stringListConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DocumentAttributeBoostingConfiguration: no recognized variant key"
        )
