"""Generated from Smithy shape ``com.amazonaws.codedeploy#AppSpecContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.raw_string_content
    import capo_codedeploy.types.raw_string_sha256


class AppSpecContent(TypedDict, closed=True):
    content: NotRequired["capo_codedeploy.types.raw_string_content.RawStringContent"]
    """<p> The YAML-formatted or JSON-formatted revision string. </p> <p> For an Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version. </p> <p> For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more. </p> <p> For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as <code>BeforeInstall</code>, during a deployment. </p>"""
    sha256: NotRequired["capo_codedeploy.types.raw_string_sha256.RawStringSha256"]
    """<p> The SHA256 hash value of the revision content. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppSpecContent) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "sha256" in value:
        out["sha256"] = value["sha256"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AppSpecContent:
    out: AppSpecContent = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("sha256") is not None:
        out["sha256"] = data["sha256"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppSpecContent) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "sha256" in value:
        out["sha256"] = value["sha256"]
    return out


def deserialize_cbor(data: dict) -> AppSpecContent:
    out: AppSpecContent = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("sha256") is not None:
        out["sha256"] = data["sha256"]
    return out
