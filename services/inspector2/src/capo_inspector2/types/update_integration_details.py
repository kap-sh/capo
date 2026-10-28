"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateIntegrationDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.update_git_hub_integration_detail
    import capo_inspector2.types.update_git_lab_self_managed_integration_detail


class UpdateIntegrationDetailsGitlabSelfManagedMember(TypedDict, closed=True):
    gitlabSelfManaged: "capo_inspector2.types.update_git_lab_self_managed_integration_detail.UpdateGitLabSelfManagedIntegrationDetail"


class UpdateIntegrationDetailsGithubMember(TypedDict, closed=True):
    github: "capo_inspector2.types.update_git_hub_integration_detail.UpdateGitHubIntegrationDetail"


UpdateIntegrationDetails: TypeAlias = (
    UpdateIntegrationDetailsGitlabSelfManagedMember
    | UpdateIntegrationDetailsGithubMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpdateIntegrationDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "gitlabSelfManaged" in value:
        import capo_inspector2.types.update_git_lab_self_managed_integration_detail

        return {
            "gitlabSelfManaged": capo_inspector2.types.update_git_lab_self_managed_integration_detail.serialize_json(
                value["gitlabSelfManaged"]
            )
        }
    elif "github" in value:
        import capo_inspector2.types.update_git_hub_integration_detail

        return {
            "github": capo_inspector2.types.update_git_hub_integration_detail.serialize_json(
                value["github"]
            )
        }
    else:
        raise SerializationError("UpdateIntegrationDetails: no variant present")


def deserialize_json(data: dict) -> UpdateIntegrationDetails:
    if data.get("gitlabSelfManaged") is not None:
        import capo_inspector2.types.update_git_lab_self_managed_integration_detail

        return {
            "gitlabSelfManaged": capo_inspector2.types.update_git_lab_self_managed_integration_detail.deserialize_json(
                data["gitlabSelfManaged"]
            )
        }
    elif data.get("github") is not None:
        import capo_inspector2.types.update_git_hub_integration_detail

        return {
            "github": capo_inspector2.types.update_git_hub_integration_detail.deserialize_json(
                data["github"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "UpdateIntegrationDetails: no recognized variant key"
        )


def redact_sensitive(value: UpdateIntegrationDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "gitlabSelfManaged" in value:
        import capo_inspector2.types.update_git_lab_self_managed_integration_detail

        out["gitlabSelfManaged"] = (
            capo_inspector2.types.update_git_lab_self_managed_integration_detail.redact_sensitive(
                value["gitlabSelfManaged"]
            )
        )
    if "github" in value:
        import capo_inspector2.types.update_git_hub_integration_detail

        out["github"] = (
            capo_inspector2.types.update_git_hub_integration_detail.redact_sensitive(
                value["github"]
            )
        )
    return out
