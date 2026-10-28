"""Generated from Smithy shape ``com.amazonaws.deadline#JobParameter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.boolean_string
    import capo_deadline.types.boolean_string_list
    import capo_deadline.types.float_string
    import capo_deadline.types.float_string_list
    import capo_deadline.types.int_string
    import capo_deadline.types.int_string_list
    import capo_deadline.types.int_string_list_list
    import capo_deadline.types.parameter_string
    import capo_deadline.types.parameter_string_list
    import capo_deadline.types.path_string
    import capo_deadline.types.path_string_list
    import capo_deadline.types.range_expr_string


class JobParameterIntMember(TypedDict, closed=True):
    int: "capo_deadline.types.int_string.IntString"


class JobParameterFloatMember(TypedDict, closed=True):
    float: "capo_deadline.types.float_string.FloatString"


class JobParameterStringMember(TypedDict, closed=True):
    string: "capo_deadline.types.parameter_string.ParameterString"


class JobParameterPathMember(TypedDict, closed=True):
    path: "capo_deadline.types.path_string.PathString"


class JobParameterBoolMember(TypedDict, closed=True):
    bool: "capo_deadline.types.boolean_string.BooleanString"


class JobParameterRangeExprMember(TypedDict, closed=True):
    rangeExpr: "capo_deadline.types.range_expr_string.RangeExprString"


class JobParameterStringListMember(TypedDict, closed=True):
    stringList: "capo_deadline.types.parameter_string_list.ParameterStringList"


class JobParameterPathListMember(TypedDict, closed=True):
    pathList: "capo_deadline.types.path_string_list.PathStringList"


class JobParameterIntListMember(TypedDict, closed=True):
    intList: "capo_deadline.types.int_string_list.IntStringList"


class JobParameterFloatListMember(TypedDict, closed=True):
    floatList: "capo_deadline.types.float_string_list.FloatStringList"


class JobParameterBoolListMember(TypedDict, closed=True):
    boolList: "capo_deadline.types.boolean_string_list.BooleanStringList"


class JobParameterIntListListMember(TypedDict, closed=True):
    intListList: "capo_deadline.types.int_string_list_list.IntStringListList"


JobParameter: TypeAlias = (
    JobParameterIntMember
    | JobParameterFloatMember
    | JobParameterStringMember
    | JobParameterPathMember
    | JobParameterBoolMember
    | JobParameterRangeExprMember
    | JobParameterStringListMember
    | JobParameterPathListMember
    | JobParameterIntListMember
    | JobParameterFloatListMember
    | JobParameterBoolListMember
    | JobParameterIntListListMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: JobParameter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"JobParameter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "int" in value:
        return {"int": value["int"]}
    elif "float" in value:
        return {"float": value["float"]}
    elif "string" in value:
        return {"string": value["string"]}
    elif "path" in value:
        return {"path": value["path"]}
    elif "bool" in value:
        return {"bool": value["bool"]}
    elif "rangeExpr" in value:
        return {"rangeExpr": value["rangeExpr"]}
    elif "stringList" in value:
        import capo_deadline.types.parameter_string_list

        return {
            "stringList": capo_deadline.types.parameter_string_list.serialize_json(
                value["stringList"]
            )
        }
    elif "pathList" in value:
        import capo_deadline.types.path_string_list

        return {
            "pathList": capo_deadline.types.path_string_list.serialize_json(
                value["pathList"]
            )
        }
    elif "intList" in value:
        import capo_deadline.types.int_string_list

        return {
            "intList": capo_deadline.types.int_string_list.serialize_json(
                value["intList"]
            )
        }
    elif "floatList" in value:
        import capo_deadline.types.float_string_list

        return {
            "floatList": capo_deadline.types.float_string_list.serialize_json(
                value["floatList"]
            )
        }
    elif "boolList" in value:
        import capo_deadline.types.boolean_string_list

        return {
            "boolList": capo_deadline.types.boolean_string_list.serialize_json(
                value["boolList"]
            )
        }
    elif "intListList" in value:
        import capo_deadline.types.int_string_list_list

        return {
            "intListList": capo_deadline.types.int_string_list_list.serialize_json(
                value["intListList"]
            )
        }
    else:
        raise SerializationError("JobParameter: no variant present")


def deserialize_json(data: dict) -> JobParameter:
    if data.get("int") is not None:
        return {"int": data["int"]}
    elif data.get("float") is not None:
        return {"float": data["float"]}
    elif data.get("string") is not None:
        return {"string": data["string"]}
    elif data.get("path") is not None:
        return {"path": data["path"]}
    elif data.get("bool") is not None:
        return {"bool": data["bool"]}
    elif data.get("rangeExpr") is not None:
        return {"rangeExpr": data["rangeExpr"]}
    elif data.get("stringList") is not None:
        import capo_deadline.types.parameter_string_list

        return {
            "stringList": capo_deadline.types.parameter_string_list.deserialize_json(
                data["stringList"]
            )
        }
    elif data.get("pathList") is not None:
        import capo_deadline.types.path_string_list

        return {
            "pathList": capo_deadline.types.path_string_list.deserialize_json(
                data["pathList"]
            )
        }
    elif data.get("intList") is not None:
        import capo_deadline.types.int_string_list

        return {
            "intList": capo_deadline.types.int_string_list.deserialize_json(
                data["intList"]
            )
        }
    elif data.get("floatList") is not None:
        import capo_deadline.types.float_string_list

        return {
            "floatList": capo_deadline.types.float_string_list.deserialize_json(
                data["floatList"]
            )
        }
    elif data.get("boolList") is not None:
        import capo_deadline.types.boolean_string_list

        return {
            "boolList": capo_deadline.types.boolean_string_list.deserialize_json(
                data["boolList"]
            )
        }
    elif data.get("intListList") is not None:
        import capo_deadline.types.int_string_list_list

        return {
            "intListList": capo_deadline.types.int_string_list_list.deserialize_json(
                data["intListList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("JobParameter: no recognized variant key")
