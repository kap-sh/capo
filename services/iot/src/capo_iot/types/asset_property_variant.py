"""Generated from Smithy shape ``com.amazonaws.iot#AssetPropertyVariant``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError, SerializationError
from capo_iot.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iot.types.asset_property_boolean_value
    import capo_iot.types.asset_property_double_value
    import capo_iot.types.asset_property_integer_value
    import capo_iot.types.asset_property_string_value


class _AssetPropertyVariant_stringValue(TypedDict, closed=True):
    stringValue: "capo_iot.types.asset_property_string_value.AssetPropertyStringValue"


class _AssetPropertyVariant_integerValue(TypedDict, closed=True):
    integerValue: (
        "capo_iot.types.asset_property_integer_value.AssetPropertyIntegerValue"
    )


class _AssetPropertyVariant_doubleValue(TypedDict, closed=True):
    doubleValue: "capo_iot.types.asset_property_double_value.AssetPropertyDoubleValue"


class _AssetPropertyVariant_booleanValue(TypedDict, closed=True):
    booleanValue: (
        "capo_iot.types.asset_property_boolean_value.AssetPropertyBooleanValue"
    )


AssetPropertyVariant: TypeAlias = (
    _AssetPropertyVariant_stringValue
    | _AssetPropertyVariant_integerValue
    | _AssetPropertyVariant_doubleValue
    | _AssetPropertyVariant_booleanValue
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyVariant) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssetPropertyVariant: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "integerValue" in value:
        return {"integerValue": value["integerValue"]}
    elif "doubleValue" in value:
        return {"doubleValue": value["doubleValue"]}
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
    else:
        raise SerializationError("AssetPropertyVariant: no variant present")


def deserialize_json(data: dict) -> AssetPropertyVariant:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("integerValue") is not None:
        return {"integerValue": data["integerValue"]}
    elif data.get("doubleValue") is not None:
        return {"doubleValue": data["doubleValue"]}
    elif data.get("booleanValue") is not None:
        return {"booleanValue": data["booleanValue"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AssetPropertyVariant: no recognized variant key")
