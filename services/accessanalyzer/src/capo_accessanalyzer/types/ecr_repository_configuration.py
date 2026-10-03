"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#EcrRepositoryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.ecr_repository_policy


class EcrRepositoryConfiguration(TypedDict, closed=True):
    repository_policy: NotRequired[
        "capo_accessanalyzer.types.ecr_repository_policy.EcrRepositoryPolicy"
    ]
    """<p>The JSON repository policy text to apply to the Amazon ECR repository. For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html">Private repository policy examples</a> in the <i>Amazon ECR User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrRepositoryConfiguration) -> dict:
    out: dict = {}
    if "repository_policy" in value:
        out["repositoryPolicy"] = value["repository_policy"]
    return out


def deserialize_json(data: dict) -> EcrRepositoryConfiguration:
    out: EcrRepositoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("repositoryPolicy") is not None:
        out["repository_policy"] = data["repositoryPolicy"]
    return out
