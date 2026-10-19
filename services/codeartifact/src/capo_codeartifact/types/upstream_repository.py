"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpstreamRepository``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.repository_name


class UpstreamRepository(TypedDict, closed=True):
    repository_name: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p> The name of an upstream repository. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpstreamRepository) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_json(data: dict) -> UpstreamRepository:
    out: UpstreamRepository = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    return out
