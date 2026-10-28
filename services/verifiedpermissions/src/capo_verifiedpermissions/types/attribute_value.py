"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#AttributeValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.boolean_attribute
    import capo_verifiedpermissions.types.datetime_attribute
    import capo_verifiedpermissions.types.decimal
    import capo_verifiedpermissions.types.duration
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.ip_addr
    import capo_verifiedpermissions.types.long_attribute
    import capo_verifiedpermissions.types.record_attribute
    import capo_verifiedpermissions.types.set_attribute
    import capo_verifiedpermissions.types.string_attribute


class AttributeValueBooleanMember(TypedDict, closed=True):
    boolean: "capo_verifiedpermissions.types.boolean_attribute.BooleanAttribute"


class AttributeValueEntityIdentifierMember(TypedDict, closed=True):
    entityIdentifier: (
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    )


class AttributeValueLongMember(TypedDict, closed=True):
    long: "capo_verifiedpermissions.types.long_attribute.LongAttribute"


class AttributeValueStringMember(TypedDict, closed=True):
    string: "capo_verifiedpermissions.types.string_attribute.StringAttribute"


class AttributeValueSetMember(TypedDict, closed=True):
    set: "capo_verifiedpermissions.types.set_attribute.SetAttribute"


class AttributeValueRecordMember(TypedDict, closed=True):
    record: "capo_verifiedpermissions.types.record_attribute.RecordAttribute"


class AttributeValueIpaddrMember(TypedDict, closed=True):
    ipaddr: "capo_verifiedpermissions.types.ip_addr.IpAddr"


class AttributeValueDecimalMember(TypedDict, closed=True):
    decimal: "capo_verifiedpermissions.types.decimal.Decimal"


class AttributeValueDatetimeMember(TypedDict, closed=True):
    datetime: "capo_verifiedpermissions.types.datetime_attribute.DatetimeAttribute"


class AttributeValueDurationMember(TypedDict, closed=True):
    duration: "capo_verifiedpermissions.types.duration.Duration"


AttributeValue: TypeAlias = (
    AttributeValueBooleanMember
    | AttributeValueEntityIdentifierMember
    | AttributeValueLongMember
    | AttributeValueStringMember
    | AttributeValueSetMember
    | AttributeValueRecordMember
    | AttributeValueIpaddrMember
    | AttributeValueDecimalMember
    | AttributeValueDatetimeMember
    | AttributeValueDurationMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AttributeValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "boolean" in value:
        return {"boolean": value["boolean"]}
    elif "entityIdentifier" in value:
        import capo_verifiedpermissions.types.entity_identifier

        return {
            "entityIdentifier": capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["entityIdentifier"]
            )
        }
    elif "long" in value:
        return {"long": value["long"]}
    elif "string" in value:
        return {"string": value["string"]}
    elif "set" in value:
        import capo_verifiedpermissions.types.set_attribute

        return {
            "set": capo_verifiedpermissions.types.set_attribute.serialize_aws_json_1_0(
                value["set"]
            )
        }
    elif "record" in value:
        import capo_verifiedpermissions.types.record_attribute

        return {
            "record": capo_verifiedpermissions.types.record_attribute.serialize_aws_json_1_0(
                value["record"]
            )
        }
    elif "ipaddr" in value:
        return {"ipaddr": value["ipaddr"]}
    elif "decimal" in value:
        return {"decimal": value["decimal"]}
    elif "datetime" in value:
        return {"datetime": value["datetime"]}
    elif "duration" in value:
        return {"duration": value["duration"]}
    else:
        raise SerializationError("AttributeValue: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AttributeValue:
    if data.get("boolean") is not None:
        return {"boolean": data["boolean"]}
    elif data.get("entityIdentifier") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        return {
            "entityIdentifier": capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["entityIdentifier"]
            )
        }
    elif data.get("long") is not None:
        return {"long": data["long"]}
    elif data.get("string") is not None:
        return {"string": data["string"]}
    elif data.get("set") is not None:
        import capo_verifiedpermissions.types.set_attribute

        return {
            "set": capo_verifiedpermissions.types.set_attribute.deserialize_aws_json_1_0(
                data["set"]
            )
        }
    elif data.get("record") is not None:
        import capo_verifiedpermissions.types.record_attribute

        return {
            "record": capo_verifiedpermissions.types.record_attribute.deserialize_aws_json_1_0(
                data["record"]
            )
        }
    elif data.get("ipaddr") is not None:
        return {"ipaddr": data["ipaddr"]}
    elif data.get("decimal") is not None:
        return {"decimal": data["decimal"]}
    elif data.get("datetime") is not None:
        return {"datetime": data["datetime"]}
    elif data.get("duration") is not None:
        return {"duration": data["duration"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AttributeValue: no recognized variant key")


def redact_sensitive(value: AttributeValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "boolean" in value:
        out["boolean"] = "*** Sensitive Data Redacted ***"
    if "entityIdentifier" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["entityIdentifier"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["entityIdentifier"]
            )
        )
    if "long" in value:
        out["long"] = "*** Sensitive Data Redacted ***"
    if "string" in value:
        out["string"] = "*** Sensitive Data Redacted ***"
    if "set" in value:
        import capo_verifiedpermissions.types.set_attribute

        out["set"] = capo_verifiedpermissions.types.set_attribute.redact_sensitive(
            value["set"]
        )
    if "record" in value:
        import capo_verifiedpermissions.types.record_attribute

        out["record"] = (
            capo_verifiedpermissions.types.record_attribute.redact_sensitive(
                value["record"]
            )
        )
    if "ipaddr" in value:
        out["ipaddr"] = "*** Sensitive Data Redacted ***"
    if "decimal" in value:
        out["decimal"] = "*** Sensitive Data Redacted ***"
    if "datetime" in value:
        out["datetime"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    return out
