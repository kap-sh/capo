"""Generated from Smithy shape ``com.amazonaws.qconnect#ParsingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.bedrock_foundation_model_configuration_for_parsing
    import capo_qconnect.types.parsing_strategy


class ParsingConfiguration(TypedDict, closed=True):
    parsing_strategy: "capo_qconnect.types.parsing_strategy.ParsingStrategy"
    """<p>The parsing strategy for the data source.</p>"""
    bedrock_foundation_model_configuration: NotRequired[
        "capo_qconnect.types.bedrock_foundation_model_configuration_for_parsing.BedrockFoundationModelConfigurationForParsing"
    ]
    """<p>Settings for a foundation model used to parse documents for a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParsingConfiguration) -> dict:
    out: dict = {}
    out["parsingStrategy"] = value["parsing_strategy"]
    if "bedrock_foundation_model_configuration" in value:
        import capo_qconnect.types.bedrock_foundation_model_configuration_for_parsing

        out["bedrockFoundationModelConfiguration"] = (
            capo_qconnect.types.bedrock_foundation_model_configuration_for_parsing.serialize_json(
                value["bedrock_foundation_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParsingConfiguration:
    out: ParsingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("parsingStrategy") is not None:
        out["parsing_strategy"] = data["parsingStrategy"]
    else:
        out["parsing_strategy"] = ""
    if data.get("bedrockFoundationModelConfiguration") is not None:
        import capo_qconnect.types.bedrock_foundation_model_configuration_for_parsing

        out["bedrock_foundation_model_configuration"] = (
            capo_qconnect.types.bedrock_foundation_model_configuration_for_parsing.deserialize_json(
                data["bedrockFoundationModelConfiguration"]
            )
        )
    return out
