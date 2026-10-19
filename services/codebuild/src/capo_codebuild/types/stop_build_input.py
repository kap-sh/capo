"""Generated from Smithy shape ``com.amazonaws.codebuild#StopBuildInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class StopBuildInput(TypedDict, closed=True):
    id: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The ID of the build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopBuildInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopBuildInput:
    out: StopBuildInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
