"""Generated from Smithy shape ``com.amazonaws.codebuild#InvalidateProjectCacheInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class InvalidateProjectCacheInput(TypedDict, closed=True):
    project_name: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The name of the CodeBuild build project that the cache is reset for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidateProjectCacheInput) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidateProjectCacheInput:
    out: InvalidateProjectCacheInput = {}  # type: ignore[typeddict-item]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        out["project_name"] = ""
    return out
