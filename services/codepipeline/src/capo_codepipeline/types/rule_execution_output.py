"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.rule_execution_result


class RuleExecutionOutput(TypedDict, closed=True):
    execution_result: NotRequired[
        "capo_codepipeline.types.rule_execution_result.RuleExecutionResult"
    ]
    """<p>Execution result information listed in the output details for a rule execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecutionOutput) -> dict:
    out: dict = {}
    if "execution_result" in value:
        import capo_codepipeline.types.rule_execution_result

        out["executionResult"] = (
            capo_codepipeline.types.rule_execution_result.serialize_aws_json_1_1(
                value["execution_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleExecutionOutput:
    out: RuleExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("executionResult") is not None:
        import capo_codepipeline.types.rule_execution_result

        out["execution_result"] = (
            capo_codepipeline.types.rule_execution_result.deserialize_aws_json_1_1(
                data["executionResult"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleExecutionOutput) -> dict:
    out: dict = {}
    if "execution_result" in value:
        import capo_codepipeline.types.rule_execution_result

        out["executionResult"] = (
            capo_codepipeline.types.rule_execution_result.serialize_cbor(
                value["execution_result"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RuleExecutionOutput:
    out: RuleExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("executionResult") is not None:
        import capo_codepipeline.types.rule_execution_result

        out["execution_result"] = (
            capo_codepipeline.types.rule_execution_result.deserialize_cbor(
                data["executionResult"]
            )
        )
    return out
