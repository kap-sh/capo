"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TransformationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.query_transformation_mode
    import capo_bedrock_agent_runtime.types.text_to_sql_configuration


class TransformationConfiguration(TypedDict, closed=True):
    mode: "capo_bedrock_agent_runtime.types.query_transformation_mode.QueryTransformationMode"
    """<p>The mode of the transformation.</p>"""
    text_to_sql_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.text_to_sql_configuration.TextToSqlConfiguration"
    ]
    """<p>Specifies configurations for transforming text to SQL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformationConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.query_transformation_mode

    out["mode"] = (
        capo_bedrock_agent_runtime.types.query_transformation_mode.serialize_json(
            value["mode"]
        )
    )
    if "text_to_sql_configuration" in value:
        import capo_bedrock_agent_runtime.types.text_to_sql_configuration

        out["textToSqlConfiguration"] = (
            capo_bedrock_agent_runtime.types.text_to_sql_configuration.serialize_json(
                value["text_to_sql_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransformationConfiguration:
    out: TransformationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_bedrock_agent_runtime.types.query_transformation_mode

        out["mode"] = (
            capo_bedrock_agent_runtime.types.query_transformation_mode.deserialize_json(
                data["mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_bedrock_agent_runtime.types.query_transformation_mode.QueryTransformationMode",
            "",
        )
    if data.get("textToSqlConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.text_to_sql_configuration

        out["text_to_sql_configuration"] = (
            capo_bedrock_agent_runtime.types.text_to_sql_configuration.deserialize_json(
                data["textToSqlConfiguration"]
            )
        )
    return out
