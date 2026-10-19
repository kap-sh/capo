"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobGenericDataSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_generic_data_enums
    import capo_amplifyuibuilder.types.codegen_generic_data_models
    import capo_amplifyuibuilder.types.codegen_generic_data_non_models
    import capo_amplifyuibuilder.types.codegen_job_generic_data_source_type


class CodegenJobGenericDataSchema(TypedDict, closed=True):
    data_source_type: "capo_amplifyuibuilder.types.codegen_job_generic_data_source_type.CodegenJobGenericDataSourceType"
    """<p>The type of the data source for the schema. Currently, the only valid value is an Amplify <code>DataStore</code>.</p>"""
    models: "capo_amplifyuibuilder.types.codegen_generic_data_models.CodegenGenericDataModels"
    """<p>The name of a <code>CodegenGenericDataModel</code>.</p>"""
    enums: (
        "capo_amplifyuibuilder.types.codegen_generic_data_enums.CodegenGenericDataEnums"
    )
    """<p>The name of a <code>CodegenGenericDataEnum</code>.</p>"""
    non_models: "capo_amplifyuibuilder.types.codegen_generic_data_non_models.CodegenGenericDataNonModels"
    """<p>The name of a <code>CodegenGenericDataNonModel</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobGenericDataSchema) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.codegen_job_generic_data_source_type

    out["dataSourceType"] = (
        capo_amplifyuibuilder.types.codegen_job_generic_data_source_type.serialize_json(
            value["data_source_type"]
        )
    )
    import capo_amplifyuibuilder.types.codegen_generic_data_models

    out["models"] = (
        capo_amplifyuibuilder.types.codegen_generic_data_models.serialize_json(
            value["models"]
        )
    )
    import capo_amplifyuibuilder.types.codegen_generic_data_enums

    out["enums"] = (
        capo_amplifyuibuilder.types.codegen_generic_data_enums.serialize_json(
            value["enums"]
        )
    )
    import capo_amplifyuibuilder.types.codegen_generic_data_non_models

    out["nonModels"] = (
        capo_amplifyuibuilder.types.codegen_generic_data_non_models.serialize_json(
            value["non_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodegenJobGenericDataSchema:
    out: CodegenJobGenericDataSchema = {}  # type: ignore[typeddict-item]
    if data.get("dataSourceType") is not None:
        import capo_amplifyuibuilder.types.codegen_job_generic_data_source_type

        out["data_source_type"] = (
            capo_amplifyuibuilder.types.codegen_job_generic_data_source_type.deserialize_json(
                data["dataSourceType"]
            )
        )
    else:
        import typing

        out["data_source_type"] = typing.cast(
            "capo_amplifyuibuilder.types.codegen_job_generic_data_source_type.CodegenJobGenericDataSourceType",
            "",
        )
    if data.get("models") is not None:
        import capo_amplifyuibuilder.types.codegen_generic_data_models

        out["models"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_models.deserialize_json(
                data["models"]
            )
        )
    else:
        out["models"] = {}
    if data.get("enums") is not None:
        import capo_amplifyuibuilder.types.codegen_generic_data_enums

        out["enums"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_enums.deserialize_json(
                data["enums"]
            )
        )
    else:
        out["enums"] = {}
    if data.get("nonModels") is not None:
        import capo_amplifyuibuilder.types.codegen_generic_data_non_models

        out["non_models"] = (
            capo_amplifyuibuilder.types.codegen_generic_data_non_models.deserialize_json(
                data["nonModels"]
            )
        )
    else:
        out["non_models"] = {}
    return out
