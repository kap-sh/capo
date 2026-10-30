"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentRepositorySource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_id
    import capo_continuum.types.repository_branch
    import capo_continuum.types.repository_name


class EnvironmentRepositorySource(TypedDict, closed=True):
    integration_id: "capo_continuum.types.integration_id.IntegrationId"
    """Integration that provides the selected repository."""
    repository: "capo_continuum.types.repository_name.RepositoryName"
    """Repository selected from that integration in owner/repository form."""
    default_branch: NotRequired[
        "capo_continuum.types.repository_branch.RepositoryBranch"
    ]
    """Branch used when a scan does not choose a more specific revision."""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentRepositorySource) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["repository"] = value["repository"]
    if "default_branch" in value:
        out["defaultBranch"] = value["default_branch"]
    return out


def deserialize_json(data: dict) -> EnvironmentRepositorySource:
    out: EnvironmentRepositorySource = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    else:
        out["repository"] = ""
    if data.get("defaultBranch") is not None:
        out["default_branch"] = data["defaultBranch"]
    return out
