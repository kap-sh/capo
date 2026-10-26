"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#StartCodegenJobData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_feature_flags
    import capo_amplifyuibuilder.types.codegen_job_generic_data_schema
    import capo_amplifyuibuilder.types.codegen_job_render_config
    import capo_amplifyuibuilder.types.tags


class StartCodegenJobData(TypedDict, closed=True):
    render_config: (
        "capo_amplifyuibuilder.types.codegen_job_render_config.CodegenJobRenderConfig"
    )
    """<p>The code generation configuration for the codegen job.</p>"""
    generic_data_schema: NotRequired[
        "capo_amplifyuibuilder.types.codegen_job_generic_data_schema.CodegenJobGenericDataSchema"
    ]
    """<p>The data schema to use for a code generation job.</p>"""
    auto_generate_forms: NotRequired["bool"]
    """<p>Specifies whether to autogenerate forms in the code generation job.</p>"""
    features: NotRequired[
        "capo_amplifyuibuilder.types.codegen_feature_flags.CodegenFeatureFlags"
    ]
    """<p>The feature flags for a code generation job.</p>"""
    tags: NotRequired["capo_amplifyuibuilder.types.tags.Tags"]
    """<p>One or more key-value pairs to use when tagging the code generation job data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodegenJobData) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.codegen_job_render_config

    out["renderConfig"] = (
        capo_amplifyuibuilder.types.codegen_job_render_config.serialize_json(
            value["render_config"]
        )
    )
    if "generic_data_schema" in value:
        import capo_amplifyuibuilder.types.codegen_job_generic_data_schema

        out["genericDataSchema"] = (
            capo_amplifyuibuilder.types.codegen_job_generic_data_schema.serialize_json(
                value["generic_data_schema"]
            )
        )
    if "auto_generate_forms" in value:
        out["autoGenerateForms"] = value["auto_generate_forms"]
    if "features" in value:
        import capo_amplifyuibuilder.types.codegen_feature_flags

        out["features"] = (
            capo_amplifyuibuilder.types.codegen_feature_flags.serialize_json(
                value["features"]
            )
        )
    if "tags" in value:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartCodegenJobData:
    out: StartCodegenJobData = {}  # type: ignore[typeddict-item]
    if data.get("renderConfig") is not None:
        import capo_amplifyuibuilder.types.codegen_job_render_config

        out["render_config"] = (
            capo_amplifyuibuilder.types.codegen_job_render_config.deserialize_json(
                data["renderConfig"]
            )
        )
    else:
        out["render_config"] = {"$unknown": {"name": ""}}
    if data.get("genericDataSchema") is not None:
        import capo_amplifyuibuilder.types.codegen_job_generic_data_schema

        out["generic_data_schema"] = (
            capo_amplifyuibuilder.types.codegen_job_generic_data_schema.deserialize_json(
                data["genericDataSchema"]
            )
        )
    if data.get("autoGenerateForms") is not None:
        out["auto_generate_forms"] = data["autoGenerateForms"]
    if data.get("features") is not None:
        import capo_amplifyuibuilder.types.codegen_feature_flags

        out["features"] = (
            capo_amplifyuibuilder.types.codegen_feature_flags.deserialize_json(
                data["features"]
            )
        )
    if data.get("tags") is not None:
        import capo_amplifyuibuilder.types.tags

        out["tags"] = capo_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    return out
