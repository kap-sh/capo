"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataEnum``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_generic_data_enum_values_list


class CodegenGenericDataEnum(TypedDict, closed=True):
    values: "capo_amplifyuibuilder.types.codegen_generic_data_enum_values_list.CodegenGenericDataEnumValuesList"
    """<p>The list of enum values in the generic data schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataEnum) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.codegen_generic_data_enum_values_list

    out["values"] = (
        capo_amplifyuibuilder.types.codegen_generic_data_enum_values_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataEnum:
    out: CodegenGenericDataEnum = {}  # type: ignore[typeddict-item]
    if data.get("values") is not None:
        import capo_amplifyuibuilder.types.codegen_generic_data_enum_values_list

        out["values"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_enum_values_list.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
