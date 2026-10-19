"""Generated from Smithy shape ``com.amazonaws.codebuild#GitSubmodulesConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.wrapper_boolean


class GitSubmodulesConfig(TypedDict, closed=True):
    fetch_submodules: "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    """<p> Set to true to fetch Git submodules for your CodeBuild build project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitSubmodulesConfig) -> dict:
    out: dict = {}
    out["fetchSubmodules"] = value["fetch_submodules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GitSubmodulesConfig:
    out: GitSubmodulesConfig = {}  # type: ignore[typeddict-item]
    if data.get("fetchSubmodules") is not None:
        out["fetch_submodules"] = data["fetchSubmodules"]
    else:
        out["fetch_submodules"] = False
    return out
