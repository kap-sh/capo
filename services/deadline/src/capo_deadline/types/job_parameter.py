"""Generated from Smithy shape ``com.amazonaws.deadline#JobParameter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError

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


class _JobParameter_int(TypedDict, closed=True):
    int: "capo_deadline.types.int_string.IntString"


class _JobParameter_float(TypedDict, closed=True):
    float: "capo_deadline.types.float_string.FloatString"


class _JobParameter_string(TypedDict, closed=True):
    string: "capo_deadline.types.parameter_string.ParameterString"


class _JobParameter_path(TypedDict, closed=True):
    path: "capo_deadline.types.path_string.PathString"


class _JobParameter_bool(TypedDict, closed=True):
    bool: "capo_deadline.types.boolean_string.BooleanString"


class _JobParameter_rangeExpr(TypedDict, closed=True):
    rangeExpr: "capo_deadline.types.range_expr_string.RangeExprString"


class _JobParameter_stringList(TypedDict, closed=True):
    stringList: "capo_deadline.types.parameter_string_list.ParameterStringList"


class _JobParameter_pathList(TypedDict, closed=True):
    pathList: "capo_deadline.types.path_string_list.PathStringList"


class _JobParameter_intList(TypedDict, closed=True):
    intList: "capo_deadline.types.int_string_list.IntStringList"


class _JobParameter_floatList(TypedDict, closed=True):
    floatList: "capo_deadline.types.float_string_list.FloatStringList"


class _JobParameter_boolList(TypedDict, closed=True):
    boolList: "capo_deadline.types.boolean_string_list.BooleanStringList"


class _JobParameter_intListList(TypedDict, closed=True):
    intListList: "capo_deadline.types.int_string_list_list.IntStringListList"


JobParameter: TypeAlias = (
    _JobParameter_int
    | _JobParameter_float
    | _JobParameter_string
    | _JobParameter_path
    | _JobParameter_bool
    | _JobParameter_rangeExpr
    | _JobParameter_stringList
    | _JobParameter_pathList
    | _JobParameter_intList
    | _JobParameter_floatList
    | _JobParameter_boolList
    | _JobParameter_intListList
)


# --- restJson1 ser/de ---
def serialize_json(value: JobParameter) -> dict:
    if "int" in value:
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
        raise DeserializationError("JobParameter: no recognized variant key")
