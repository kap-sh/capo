"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.boolean_configuration_options
    import capo_securityhub.types.double_configuration_options
    import capo_securityhub.types.enum_configuration_options
    import capo_securityhub.types.enum_list_configuration_options
    import capo_securityhub.types.integer_configuration_options
    import capo_securityhub.types.integer_list_configuration_options
    import capo_securityhub.types.string_configuration_options
    import capo_securityhub.types.string_list_configuration_options


class _ConfigurationOptions_Integer(TypedDict, closed=True):
    Integer: "capo_securityhub.types.integer_configuration_options.IntegerConfigurationOptions"


class _ConfigurationOptions_IntegerList(TypedDict, closed=True):
    IntegerList: "capo_securityhub.types.integer_list_configuration_options.IntegerListConfigurationOptions"


class _ConfigurationOptions_Double(TypedDict, closed=True):
    Double: (
        "capo_securityhub.types.double_configuration_options.DoubleConfigurationOptions"
    )


class _ConfigurationOptions_String(TypedDict, closed=True):
    String: (
        "capo_securityhub.types.string_configuration_options.StringConfigurationOptions"
    )


class _ConfigurationOptions_StringList(TypedDict, closed=True):
    StringList: "capo_securityhub.types.string_list_configuration_options.StringListConfigurationOptions"


class _ConfigurationOptions_Boolean(TypedDict, closed=True):
    Boolean: "capo_securityhub.types.boolean_configuration_options.BooleanConfigurationOptions"


class _ConfigurationOptions_Enum(TypedDict, closed=True):
    Enum: "capo_securityhub.types.enum_configuration_options.EnumConfigurationOptions"


class _ConfigurationOptions_EnumList(TypedDict, closed=True):
    EnumList: "capo_securityhub.types.enum_list_configuration_options.EnumListConfigurationOptions"


ConfigurationOptions: TypeAlias = (
    _ConfigurationOptions_Integer
    | _ConfigurationOptions_IntegerList
    | _ConfigurationOptions_Double
    | _ConfigurationOptions_String
    | _ConfigurationOptions_StringList
    | _ConfigurationOptions_Boolean
    | _ConfigurationOptions_Enum
    | _ConfigurationOptions_EnumList
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationOptions) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ConfigurationOptions: cannot serialize unknown variant {value.name!r}"
        )
    elif "Integer" in value:
        import capo_securityhub.types.integer_configuration_options

        return {
            "Integer": capo_securityhub.types.integer_configuration_options.serialize_json(
                value["Integer"]
            )
        }
    elif "IntegerList" in value:
        import capo_securityhub.types.integer_list_configuration_options

        return {
            "IntegerList": capo_securityhub.types.integer_list_configuration_options.serialize_json(
                value["IntegerList"]
            )
        }
    elif "Double" in value:
        import capo_securityhub.types.double_configuration_options

        return {
            "Double": capo_securityhub.types.double_configuration_options.serialize_json(
                value["Double"]
            )
        }
    elif "String" in value:
        import capo_securityhub.types.string_configuration_options

        return {
            "String": capo_securityhub.types.string_configuration_options.serialize_json(
                value["String"]
            )
        }
    elif "StringList" in value:
        import capo_securityhub.types.string_list_configuration_options

        return {
            "StringList": capo_securityhub.types.string_list_configuration_options.serialize_json(
                value["StringList"]
            )
        }
    elif "Boolean" in value:
        import capo_securityhub.types.boolean_configuration_options

        return {
            "Boolean": capo_securityhub.types.boolean_configuration_options.serialize_json(
                value["Boolean"]
            )
        }
    elif "Enum" in value:
        import capo_securityhub.types.enum_configuration_options

        return {
            "Enum": capo_securityhub.types.enum_configuration_options.serialize_json(
                value["Enum"]
            )
        }
    elif "EnumList" in value:
        import capo_securityhub.types.enum_list_configuration_options

        return {
            "EnumList": capo_securityhub.types.enum_list_configuration_options.serialize_json(
                value["EnumList"]
            )
        }
    else:
        raise SerializationError("ConfigurationOptions: no variant present")


def deserialize_json(data: dict) -> ConfigurationOptions:
    if data.get("Integer") is not None:
        import capo_securityhub.types.integer_configuration_options

        return {
            "Integer": capo_securityhub.types.integer_configuration_options.deserialize_json(
                data["Integer"]
            )
        }
    elif data.get("IntegerList") is not None:
        import capo_securityhub.types.integer_list_configuration_options

        return {
            "IntegerList": capo_securityhub.types.integer_list_configuration_options.deserialize_json(
                data["IntegerList"]
            )
        }
    elif data.get("Double") is not None:
        import capo_securityhub.types.double_configuration_options

        return {
            "Double": capo_securityhub.types.double_configuration_options.deserialize_json(
                data["Double"]
            )
        }
    elif data.get("String") is not None:
        import capo_securityhub.types.string_configuration_options

        return {
            "String": capo_securityhub.types.string_configuration_options.deserialize_json(
                data["String"]
            )
        }
    elif data.get("StringList") is not None:
        import capo_securityhub.types.string_list_configuration_options

        return {
            "StringList": capo_securityhub.types.string_list_configuration_options.deserialize_json(
                data["StringList"]
            )
        }
    elif data.get("Boolean") is not None:
        import capo_securityhub.types.boolean_configuration_options

        return {
            "Boolean": capo_securityhub.types.boolean_configuration_options.deserialize_json(
                data["Boolean"]
            )
        }
    elif data.get("Enum") is not None:
        import capo_securityhub.types.enum_configuration_options

        return {
            "Enum": capo_securityhub.types.enum_configuration_options.deserialize_json(
                data["Enum"]
            )
        }
    elif data.get("EnumList") is not None:
        import capo_securityhub.types.enum_list_configuration_options

        return {
            "EnumList": capo_securityhub.types.enum_list_configuration_options.deserialize_json(
                data["EnumList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ConfigurationOptions: no recognized variant key")
