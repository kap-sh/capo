"""Generated from Smithy shape ``com.amazonaws.proton#DeleteRepositoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider


class DeleteRepositoryInput(TypedDict, closed=True):
    provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRepositoryInput) -> dict:
    out: dict = {}
    out["provider"] = value["provider"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRepositoryInput:
    out: DeleteRepositoryInput = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
