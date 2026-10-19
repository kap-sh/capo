"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_generic_data_field_data_type
    import capo_amplifyuibuilder.types.codegen_generic_data_relationship_type


class CodegenGenericDataField(TypedDict, closed=True):
    data_type: "capo_amplifyuibuilder.types.codegen_generic_data_field_data_type.CodegenGenericDataFieldDataType"
    """<p>The data type for the generic data field.</p>"""
    data_type_value: "str"
    """<p>The value of the data type for the generic data field.</p>"""
    required: "bool"
    """<p>Specifies whether the generic data field is required.</p>"""
    read_only: "bool"
    """<p>Specifies whether the generic data field is read-only.</p>"""
    is_array: "bool"
    """<p>Specifies whether the generic data field is an array.</p>"""
    relationship: NotRequired[
        "capo_amplifyuibuilder.types.codegen_generic_data_relationship_type.CodegenGenericDataRelationshipType"
    ]
    """<p>The relationship of the generic data schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataField) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.codegen_generic_data_field_data_type

    out["dataType"] = (
        capo_amplifyuibuilder.types.codegen_generic_data_field_data_type.serialize_json(
            value["data_type"]
        )
    )
    out["dataTypeValue"] = value["data_type_value"]
    out["required"] = value["required"]
    out["readOnly"] = value["read_only"]
    out["isArray"] = value["is_array"]
    if "relationship" in value:
        import capo_amplifyuibuilder.types.codegen_generic_data_relationship_type

        out["relationship"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_relationship_type.serialize_json(
                value["relationship"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataField:
    out: CodegenGenericDataField = {}  # type: ignore[typeddict-item]
    if data.get("dataType") is not None:
        import capo_amplifyuibuilder.types.codegen_generic_data_field_data_type

        out["data_type"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_field_data_type.deserialize_json(
                data["dataType"]
            )
        )
    else:
        import typing

        out["data_type"] = typing.cast(
            "capo_amplifyuibuilder.types.codegen_generic_data_field_data_type.CodegenGenericDataFieldDataType",
            "",
        )
    if data.get("dataTypeValue") is not None:
        out["data_type_value"] = data["dataTypeValue"]
    else:
        out["data_type_value"] = ""
    if data.get("required") is not None:
        out["required"] = data["required"]
    else:
        out["required"] = False
    if data.get("readOnly") is not None:
        out["read_only"] = data["readOnly"]
    else:
        out["read_only"] = False
    if data.get("isArray") is not None:
        out["is_array"] = data["isArray"]
    else:
        out["is_array"] = False
    if data.get("relationship") is not None:
        import capo_amplifyuibuilder.types.codegen_generic_data_relationship_type

        out["relationship"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_relationship_type.deserialize_json(
                data["relationship"]
            )
        )
    return out
