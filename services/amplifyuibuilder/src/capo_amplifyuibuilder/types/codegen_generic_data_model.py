"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_generic_data_fields
    import capo_amplifyuibuilder.types.codegen_primary_keys_list


class CodegenGenericDataModel(TypedDict, closed=True):
    fields: "capo_amplifyuibuilder.types.codegen_generic_data_fields.CodegenGenericDataFields"
    """<p>The fields in the generic data model.</p>"""
    is_join_table: NotRequired["bool"]
    """<p>Specifies whether the generic data model is a join table.</p>"""
    primary_keys: (
        "capo_amplifyuibuilder.types.codegen_primary_keys_list.CodegenPrimaryKeysList"
    )
    """<p>The primary keys of the generic data model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataModel) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.codegen_generic_data_fields

    out["fields"] = (
        capo_amplifyuibuilder.types.codegen_generic_data_fields.serialize_json(
            value["fields"]
        )
    )
    if "is_join_table" in value:
        out["isJoinTable"] = value["is_join_table"]
    import capo_amplifyuibuilder.types.codegen_primary_keys_list

    out["primaryKeys"] = (
        capo_amplifyuibuilder.types.codegen_primary_keys_list.serialize_json(
            value["primary_keys"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataModel:
    out: CodegenGenericDataModel = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_amplifyuibuilder.types.codegen_generic_data_fields

        out["fields"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        out["fields"] = {}
    if data.get("isJoinTable") is not None:
        out["is_join_table"] = data["isJoinTable"]
    if data.get("primaryKeys") is not None:
        import capo_amplifyuibuilder.types.codegen_primary_keys_list

        out["primary_keys"] = (
            capo_amplifyuibuilder.types.codegen_primary_keys_list.deserialize_json(
                data["primaryKeys"]
            )
        )
    else:
        out["primary_keys"] = []
    return out
