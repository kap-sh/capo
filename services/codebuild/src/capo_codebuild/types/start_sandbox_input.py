"""Generated from Smithy shape ``com.amazonaws.codebuild#StartSandboxInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.sensitive_string


class StartSandboxInput(TypedDict, closed=True):
    project_name: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The CodeBuild project name.</p>"""
    idempotency_token: NotRequired[
        "capo_codebuild.types.sensitive_string.SensitiveString"
    ]
    """<p>A unique client token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSandboxInput) -> dict:
    out: dict = {}
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSandboxInput:
    out: StartSandboxInput = {}  # type: ignore[typeddict-item]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    if data.get("idempotencyToken") is not None:
        out["idempotency_token"] = data["idempotencyToken"]
    return out


def redact_sensitive(value: StartSandboxInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "idempotency_token" in value:
        out["idempotency_token"] = "*** Sensitive Data Redacted ***"
    return out
