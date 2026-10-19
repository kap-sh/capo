"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeExecutor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.executor_configuration
    import capo_codepipeline.types.executor_type
    import capo_codepipeline.types.job_timeout
    import capo_codepipeline.types.policy_statements_template


class ActionTypeExecutor(TypedDict, closed=True):
    configuration: (
        "capo_codepipeline.types.executor_configuration.ExecutorConfiguration"
    )
    """<p>The action configuration properties for the action type. These properties are specified in the action definition when the action type is created.</p>"""
    type: "capo_codepipeline.types.executor_type.ExecutorType"
    """<p>The integration model used to create and update the action type, <code>Lambda</code> or <code>JobWorker</code>. </p>"""
    policy_statements_template: NotRequired[
        "capo_codepipeline.types.policy_statements_template.PolicyStatementsTemplate"
    ]
    """<p>The policy statement that specifies the permissions in the CodePipeline customer account that are needed to successfully run an action.</p> <p>To grant permission to another account, specify the account ID as the Principal, a domain-style identifier defined by the service, for example <code>codepipeline.amazonaws.com</code>.</p> <note> <p>The size of the passed JSON policy document cannot exceed 2048 characters.</p> </note>"""
    job_timeout: NotRequired["capo_codepipeline.types.job_timeout.JobTimeout"]
    """<p>The timeout in seconds for the job. An action execution can have multiple jobs. This is the timeout for a single job, not the entire action execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeExecutor) -> dict:
    out: dict = {}
    import capo_codepipeline.types.executor_configuration

    out["configuration"] = (
        capo_codepipeline.types.executor_configuration.serialize_aws_json_1_1(
            value["configuration"]
        )
    )
    import capo_codepipeline.types.executor_type

    out["type"] = capo_codepipeline.types.executor_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "policy_statements_template" in value:
        out["policyStatementsTemplate"] = value["policy_statements_template"]
    if "job_timeout" in value:
        out["jobTimeout"] = value["job_timeout"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypeExecutor:
    out: ActionTypeExecutor = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_codepipeline.types.executor_configuration

        out["configuration"] = (
            capo_codepipeline.types.executor_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("ActionTypeExecutor.configuration required")
    if data.get("type") is not None:
        import capo_codepipeline.types.executor_type

        out["type"] = capo_codepipeline.types.executor_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_codepipeline.types.executor_type.ExecutorType", ""
        )
    if data.get("policyStatementsTemplate") is not None:
        out["policy_statements_template"] = data["policyStatementsTemplate"]
    if data.get("jobTimeout") is not None:
        out["job_timeout"] = data["jobTimeout"]
    return out
