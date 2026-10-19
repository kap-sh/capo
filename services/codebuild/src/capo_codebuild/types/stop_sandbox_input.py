"""Generated from Smithy shape ``com.amazonaws.codebuild#StopSandboxInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class StopSandboxInput(TypedDict, closed=True):
    id: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>Information about the requested sandbox ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSandboxInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSandboxInput:
    out: StopSandboxInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
