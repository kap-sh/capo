"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.job_worker_executor_configuration
    import capo_codepipeline.types.lambda_executor_configuration


class ExecutorConfiguration(TypedDict, closed=True):
    lambda_executor_configuration: NotRequired[
        "capo_codepipeline.types.lambda_executor_configuration.LambdaExecutorConfiguration"
    ]
    """<p>Details about the <code>Lambda</code> executor of the action type.</p>"""
    job_worker_executor_configuration: NotRequired[
        "capo_codepipeline.types.job_worker_executor_configuration.JobWorkerExecutorConfiguration"
    ]
    """<p>Details about the <code>JobWorker</code> executor of the action type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutorConfiguration) -> dict:
    out: dict = {}
    if "lambda_executor_configuration" in value:
        import capo_codepipeline.types.lambda_executor_configuration

        out["lambdaExecutorConfiguration"] = (
            capo_codepipeline.types.lambda_executor_configuration.serialize_aws_json_1_1(
                value["lambda_executor_configuration"]
            )
        )
    if "job_worker_executor_configuration" in value:
        import capo_codepipeline.types.job_worker_executor_configuration

        out["jobWorkerExecutorConfiguration"] = (
            capo_codepipeline.types.job_worker_executor_configuration.serialize_aws_json_1_1(
                value["job_worker_executor_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutorConfiguration:
    out: ExecutorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("lambdaExecutorConfiguration") is not None:
        import capo_codepipeline.types.lambda_executor_configuration

        out["lambda_executor_configuration"] = (
            capo_codepipeline.types.lambda_executor_configuration.deserialize_aws_json_1_1(
                data["lambdaExecutorConfiguration"]
            )
        )
    if data.get("jobWorkerExecutorConfiguration") is not None:
        import capo_codepipeline.types.job_worker_executor_configuration

        out["job_worker_executor_configuration"] = (
            capo_codepipeline.types.job_worker_executor_configuration.deserialize_aws_json_1_1(
                data["jobWorkerExecutorConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutorConfiguration) -> dict:
    out: dict = {}
    if "lambda_executor_configuration" in value:
        import capo_codepipeline.types.lambda_executor_configuration

        out["lambdaExecutorConfiguration"] = (
            capo_codepipeline.types.lambda_executor_configuration.serialize_cbor(
                value["lambda_executor_configuration"]
            )
        )
    if "job_worker_executor_configuration" in value:
        import capo_codepipeline.types.job_worker_executor_configuration

        out["jobWorkerExecutorConfiguration"] = (
            capo_codepipeline.types.job_worker_executor_configuration.serialize_cbor(
                value["job_worker_executor_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ExecutorConfiguration:
    out: ExecutorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("lambdaExecutorConfiguration") is not None:
        import capo_codepipeline.types.lambda_executor_configuration

        out["lambda_executor_configuration"] = (
            capo_codepipeline.types.lambda_executor_configuration.deserialize_cbor(
                data["lambdaExecutorConfiguration"]
            )
        )
    if data.get("jobWorkerExecutorConfiguration") is not None:
        import capo_codepipeline.types.job_worker_executor_configuration

        out["job_worker_executor_configuration"] = (
            capo_codepipeline.types.job_worker_executor_configuration.deserialize_cbor(
                data["jobWorkerExecutorConfiguration"]
            )
        )
    return out
