"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesCellValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_keyspacesstreams.errors import DeserializationError, SerializationError
from capo_keyspacesstreams.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.keyspaces_cell_list
    import capo_keyspacesstreams.types.keyspaces_cell_map
    import capo_keyspacesstreams.types.keyspaces_udt_map


class KeyspacesCellValueAsciiTMember(TypedDict, closed=True):
    asciiT: "str"


class KeyspacesCellValueBigintTMember(TypedDict, closed=True):
    bigintT: "str"


class KeyspacesCellValueBlobTMember(TypedDict, closed=True):
    blobT: "bytes"


class KeyspacesCellValueBoolTMember(TypedDict, closed=True):
    boolT: "bool"


class KeyspacesCellValueCounterTMember(TypedDict, closed=True):
    counterT: "str"


class KeyspacesCellValueDateTMember(TypedDict, closed=True):
    dateT: "str"


class KeyspacesCellValueDecimalTMember(TypedDict, closed=True):
    decimalT: "str"


class KeyspacesCellValueDoubleTMember(TypedDict, closed=True):
    doubleT: "str"


class KeyspacesCellValueDurationTMember(TypedDict, closed=True):
    durationT: "str"


class KeyspacesCellValueFloatTMember(TypedDict, closed=True):
    floatT: "str"


class KeyspacesCellValueInetTMember(TypedDict, closed=True):
    inetT: "str"


class KeyspacesCellValueIntTMember(TypedDict, closed=True):
    intT: "str"


class KeyspacesCellValueListTMember(TypedDict, closed=True):
    listT: "capo_keyspacesstreams.types.keyspaces_cell_list.KeyspacesCellList"


class KeyspacesCellValueMapTMember(TypedDict, closed=True):
    mapT: "capo_keyspacesstreams.types.keyspaces_cell_map.KeyspacesCellMap"


class KeyspacesCellValueSetTMember(TypedDict, closed=True):
    setT: "capo_keyspacesstreams.types.keyspaces_cell_list.KeyspacesCellList"


class KeyspacesCellValueSmallintTMember(TypedDict, closed=True):
    smallintT: "str"


class KeyspacesCellValueTextTMember(TypedDict, closed=True):
    textT: "str"


class KeyspacesCellValueTimeTMember(TypedDict, closed=True):
    timeT: "str"


class KeyspacesCellValueTimestampTMember(TypedDict, closed=True):
    timestampT: "str"


class KeyspacesCellValueTimeuuidTMember(TypedDict, closed=True):
    timeuuidT: "str"


class KeyspacesCellValueTinyintTMember(TypedDict, closed=True):
    tinyintT: "str"


class KeyspacesCellValueTupleTMember(TypedDict, closed=True):
    tupleT: "capo_keyspacesstreams.types.keyspaces_cell_list.KeyspacesCellList"


class KeyspacesCellValueUuidTMember(TypedDict, closed=True):
    uuidT: "str"


class KeyspacesCellValueVarcharTMember(TypedDict, closed=True):
    varcharT: "str"


class KeyspacesCellValueVarintTMember(TypedDict, closed=True):
    varintT: "str"


class KeyspacesCellValueUdtTMember(TypedDict, closed=True):
    udtT: "capo_keyspacesstreams.types.keyspaces_udt_map.KeyspacesUdtMap"


KeyspacesCellValue: TypeAlias = (
    KeyspacesCellValueAsciiTMember
    | KeyspacesCellValueBigintTMember
    | KeyspacesCellValueBlobTMember
    | KeyspacesCellValueBoolTMember
    | KeyspacesCellValueCounterTMember
    | KeyspacesCellValueDateTMember
    | KeyspacesCellValueDecimalTMember
    | KeyspacesCellValueDoubleTMember
    | KeyspacesCellValueDurationTMember
    | KeyspacesCellValueFloatTMember
    | KeyspacesCellValueInetTMember
    | KeyspacesCellValueIntTMember
    | KeyspacesCellValueListTMember
    | KeyspacesCellValueMapTMember
    | KeyspacesCellValueSetTMember
    | KeyspacesCellValueSmallintTMember
    | KeyspacesCellValueTextTMember
    | KeyspacesCellValueTimeTMember
    | KeyspacesCellValueTimestampTMember
    | KeyspacesCellValueTimeuuidTMember
    | KeyspacesCellValueTinyintTMember
    | KeyspacesCellValueTupleTMember
    | KeyspacesCellValueUuidTMember
    | KeyspacesCellValueVarcharTMember
    | KeyspacesCellValueVarintTMember
    | KeyspacesCellValueUdtTMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspacesCellValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"KeyspacesCellValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "asciiT" in value:
        return {"asciiT": value["asciiT"]}
    elif "bigintT" in value:
        return {"bigintT": value["bigintT"]}
    elif "blobT" in value:
        import capo_keyspacesstreams.types._prelude.blob

        return {
            "blobT": capo_keyspacesstreams.types._prelude.blob.serialize_aws_json_1_0(
                value["blobT"]
            )
        }
    elif "boolT" in value:
        return {"boolT": value["boolT"]}
    elif "counterT" in value:
        return {"counterT": value["counterT"]}
    elif "dateT" in value:
        return {"dateT": value["dateT"]}
    elif "decimalT" in value:
        return {"decimalT": value["decimalT"]}
    elif "doubleT" in value:
        return {"doubleT": value["doubleT"]}
    elif "durationT" in value:
        return {"durationT": value["durationT"]}
    elif "floatT" in value:
        return {"floatT": value["floatT"]}
    elif "inetT" in value:
        return {"inetT": value["inetT"]}
    elif "intT" in value:
        return {"intT": value["intT"]}
    elif "listT" in value:
        import capo_keyspacesstreams.types.keyspaces_cell_list

        return {
            "listT": capo_keyspacesstreams.types.keyspaces_cell_list.serialize_aws_json_1_0(
                value["listT"]
            )
        }
    elif "mapT" in value:
        import capo_keyspacesstreams.types.keyspaces_cell_map

        return {
            "mapT": capo_keyspacesstreams.types.keyspaces_cell_map.serialize_aws_json_1_0(
                value["mapT"]
            )
        }
    elif "setT" in value:
        import capo_keyspacesstreams.types.keyspaces_cell_list

        return {
            "setT": capo_keyspacesstreams.types.keyspaces_cell_list.serialize_aws_json_1_0(
                value["setT"]
            )
        }
    elif "smallintT" in value:
        return {"smallintT": value["smallintT"]}
    elif "textT" in value:
        return {"textT": value["textT"]}
    elif "timeT" in value:
        return {"timeT": value["timeT"]}
    elif "timestampT" in value:
        return {"timestampT": value["timestampT"]}
    elif "timeuuidT" in value:
        return {"timeuuidT": value["timeuuidT"]}
    elif "tinyintT" in value:
        return {"tinyintT": value["tinyintT"]}
    elif "tupleT" in value:
        import capo_keyspacesstreams.types.keyspaces_cell_list

        return {
            "tupleT": capo_keyspacesstreams.types.keyspaces_cell_list.serialize_aws_json_1_0(
                value["tupleT"]
            )
        }
    elif "uuidT" in value:
        return {"uuidT": value["uuidT"]}
    elif "varcharT" in value:
        return {"varcharT": value["varcharT"]}
    elif "varintT" in value:
        return {"varintT": value["varintT"]}
    elif "udtT" in value:
        import capo_keyspacesstreams.types.keyspaces_udt_map

        return {
            "udtT": capo_keyspacesstreams.types.keyspaces_udt_map.serialize_aws_json_1_0(
                value["udtT"]
            )
        }
    else:
        raise SerializationError("KeyspacesCellValue: no variant present")


def deserialize_aws_json_1_0(data: dict) -> KeyspacesCellValue:
    if data.get("asciiT") is not None:
        return {"asciiT": data["asciiT"]}
    elif data.get("bigintT") is not None:
        return {"bigintT": data["bigintT"]}
    elif data.get("blobT") is not None:
        import capo_keyspacesstreams.types._prelude.blob

        return {
            "blobT": capo_keyspacesstreams.types._prelude.blob.deserialize_aws_json_1_0(
                data["blobT"]
            )
        }
    elif data.get("boolT") is not None:
        return {"boolT": data["boolT"]}
    elif data.get("counterT") is not None:
        return {"counterT": data["counterT"]}
    elif data.get("dateT") is not None:
        return {"dateT": data["dateT"]}
    elif data.get("decimalT") is not None:
        return {"decimalT": data["decimalT"]}
    elif data.get("doubleT") is not None:
        return {"doubleT": data["doubleT"]}
    elif data.get("durationT") is not None:
        return {"durationT": data["durationT"]}
    elif data.get("floatT") is not None:
        return {"floatT": data["floatT"]}
    elif data.get("inetT") is not None:
        return {"inetT": data["inetT"]}
    elif data.get("intT") is not None:
        return {"intT": data["intT"]}
    elif data.get("listT") is not None:
        import capo_keyspacesstreams.types.keyspaces_cell_list

        return {
            "listT": capo_keyspacesstreams.types.keyspaces_cell_list.deserialize_aws_json_1_0(
                data["listT"]
            )
        }
    elif data.get("mapT") is not None:
        import capo_keyspacesstreams.types.keyspaces_cell_map

        return {
            "mapT": capo_keyspacesstreams.types.keyspaces_cell_map.deserialize_aws_json_1_0(
                data["mapT"]
            )
        }
    elif data.get("setT") is not None:
        import capo_keyspacesstreams.types.keyspaces_cell_list

        return {
            "setT": capo_keyspacesstreams.types.keyspaces_cell_list.deserialize_aws_json_1_0(
                data["setT"]
            )
        }
    elif data.get("smallintT") is not None:
        return {"smallintT": data["smallintT"]}
    elif data.get("textT") is not None:
        return {"textT": data["textT"]}
    elif data.get("timeT") is not None:
        return {"timeT": data["timeT"]}
    elif data.get("timestampT") is not None:
        return {"timestampT": data["timestampT"]}
    elif data.get("timeuuidT") is not None:
        return {"timeuuidT": data["timeuuidT"]}
    elif data.get("tinyintT") is not None:
        return {"tinyintT": data["tinyintT"]}
    elif data.get("tupleT") is not None:
        import capo_keyspacesstreams.types.keyspaces_cell_list

        return {
            "tupleT": capo_keyspacesstreams.types.keyspaces_cell_list.deserialize_aws_json_1_0(
                data["tupleT"]
            )
        }
    elif data.get("uuidT") is not None:
        return {"uuidT": data["uuidT"]}
    elif data.get("varcharT") is not None:
        return {"varcharT": data["varcharT"]}
    elif data.get("varintT") is not None:
        return {"varintT": data["varintT"]}
    elif data.get("udtT") is not None:
        import capo_keyspacesstreams.types.keyspaces_udt_map

        return {
            "udtT": capo_keyspacesstreams.types.keyspaces_udt_map.deserialize_aws_json_1_0(
                data["udtT"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("KeyspacesCellValue: no recognized variant key")
