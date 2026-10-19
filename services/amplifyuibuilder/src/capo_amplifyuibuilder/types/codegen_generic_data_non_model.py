"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataNonModel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_generic_data_non_model_fields


class CodegenGenericDataNonModel(TypedDict, closed=True):
    fields: "capo_amplifyuibuilder.types.codegen_generic_data_non_model_fields.CodegenGenericDataNonModelFields"
    """<p>The fields in a generic data schema non model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataNonModel) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.codegen_generic_data_non_model_fields

    out["fields"] = (
        capo_amplifyuibuilder.types.codegen_generic_data_non_model_fields.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataNonModel:
    out: CodegenGenericDataNonModel = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_amplifyuibuilder.types.codegen_generic_data_non_model_fields

        out["fields"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_non_model_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        out["fields"] = {}
    return out
