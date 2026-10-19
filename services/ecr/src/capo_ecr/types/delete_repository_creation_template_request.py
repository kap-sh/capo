"""Generated from Smithy shape ``com.amazonaws.ecr#DeleteRepositoryCreationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.prefix


class DeleteRepositoryCreationTemplateRequest(TypedDict, closed=True):
    prefix: "capo_ecr.types.prefix.Prefix"
    """<p>The repository namespace prefix associated with the repository creation template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRepositoryCreationTemplateRequest) -> dict:
    out: dict = {}
    out["prefix"] = value["prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRepositoryCreationTemplateRequest:
    out: DeleteRepositoryCreationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    return out
