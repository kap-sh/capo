"""Generated from Smithy shape ``com.amazonaws.codebuild#StopBuildBatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class StopBuildBatchInput(TypedDict, closed=True):
    id: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the batch build to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopBuildBatchInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopBuildBatchInput:
    out: StopBuildBatchInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
