"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptOverrideConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.lambda_arn
    import capo_bedrock_agent.types.prompt_configurations


class PromptOverrideConfiguration(TypedDict, closed=True):
    prompt_configurations: (
        "capo_bedrock_agent.types.prompt_configurations.PromptConfigurations"
    )
    """<p>Contains configurations to override a prompt template in one part of an agent sequence. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p>"""
    override_lambda: NotRequired["capo_bedrock_agent.types.lambda_arn.LambdaArn"]
    """<p>The ARN of the Lambda function to use when parsing the raw foundation model output in parts of the agent sequence. If you specify this field, at least one of the <code>promptConfigurations</code> must contain a <code>parserMode</code> value that is set to <code>OVERRIDDEN</code>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/lambda-parser.html">Parser Lambda function in Amazon Bedrock Agents</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptOverrideConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.prompt_configurations

    out["promptConfigurations"] = (
        capo_bedrock_agent.types.prompt_configurations.serialize_json(
            value["prompt_configurations"]
        )
    )
    if "override_lambda" in value:
        out["overrideLambda"] = value["override_lambda"]
    return out


def deserialize_json(data: dict) -> PromptOverrideConfiguration:
    out: PromptOverrideConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("promptConfigurations") is not None:
        import capo_bedrock_agent.types.prompt_configurations

        out["prompt_configurations"] = (
            capo_bedrock_agent.types.prompt_configurations.deserialize_json(
                data["promptConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "PromptOverrideConfiguration.prompt_configurations required"
        )
    if data.get("overrideLambda") is not None:
        out["override_lambda"] = data["overrideLambda"]
    return out
