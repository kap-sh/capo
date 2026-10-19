"""Generated from Smithy shape ``com.amazonaws.codebuild#StartSandboxConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class StartSandboxConnectionInput(TypedDict, closed=True):
    sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSandboxConnectionInput) -> dict:
    out: dict = {}
    out["sandboxId"] = value["sandbox_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSandboxConnectionInput:
    out: StartSandboxConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("sandboxId") is not None:
        out["sandbox_id"] = data["sandboxId"]
    else:
        out["sandbox_id"] = ""
    return out
