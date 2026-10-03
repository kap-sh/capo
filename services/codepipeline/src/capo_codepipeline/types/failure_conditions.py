"""Generated from Smithy shape ``com.amazonaws.codepipeline#FailureConditions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_list
    import capo_codepipeline.types.result
    import capo_codepipeline.types.retry_configuration


class FailureConditions(TypedDict, closed=True):
    result: NotRequired["capo_codepipeline.types.result.Result"]
    """<p>The specified result for when the failure conditions are met, such as rolling back the stage.</p>"""
    retry_configuration: NotRequired[
        "capo_codepipeline.types.retry_configuration.RetryConfiguration"
    ]
    """<p>The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode.</p>"""
    conditions: NotRequired["capo_codepipeline.types.condition_list.ConditionList"]
    """<p>The conditions that are configured as failure conditions. For more information about conditions, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html">Stage conditions</a> and <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html">How do stage conditions work?</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureConditions) -> dict:
    out: dict = {}
    if "result" in value:
        import capo_codepipeline.types.result

        out["result"] = capo_codepipeline.types.result.serialize_aws_json_1_1(
            value["result"]
        )
    if "retry_configuration" in value:
        import capo_codepipeline.types.retry_configuration

        out["retryConfiguration"] = (
            capo_codepipeline.types.retry_configuration.serialize_aws_json_1_1(
                value["retry_configuration"]
            )
        )
    if "conditions" in value:
        import capo_codepipeline.types.condition_list

        out["conditions"] = (
            capo_codepipeline.types.condition_list.serialize_aws_json_1_1(
                value["conditions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureConditions:
    out: FailureConditions = {}  # type: ignore[typeddict-item]
    if data.get("result") is not None:
        import capo_codepipeline.types.result

        out["result"] = capo_codepipeline.types.result.deserialize_aws_json_1_1(
            data["result"]
        )
    if data.get("retryConfiguration") is not None:
        import capo_codepipeline.types.retry_configuration

        out["retry_configuration"] = (
            capo_codepipeline.types.retry_configuration.deserialize_aws_json_1_1(
                data["retryConfiguration"]
            )
        )
    if data.get("conditions") is not None:
        import capo_codepipeline.types.condition_list

        out["conditions"] = (
            capo_codepipeline.types.condition_list.deserialize_aws_json_1_1(
                data["conditions"]
            )
        )
    return out
