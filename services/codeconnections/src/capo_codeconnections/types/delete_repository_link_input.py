"""Generated from Smithy shape ``com.amazonaws.codeconnections#DeleteRepositoryLinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_link_id


class DeleteRepositoryLinkInput(TypedDict, closed=True):
    repository_link_id: "capo_codeconnections.types.repository_link_id.RepositoryLinkId"
    """<p>The ID of the repository link to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRepositoryLinkInput) -> dict:
    out: dict = {}
    out["RepositoryLinkId"] = value["repository_link_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRepositoryLinkInput:
    out: DeleteRepositoryLinkInput = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryLinkId") is not None:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        out["repository_link_id"] = ""
    return out
