"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateIntegrationDetail``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.create_git_lab_self_managed_integration_detail


class CreateIntegrationDetailGitlabSelfManagedMember(TypedDict, closed=True):
    gitlabSelfManaged: "capo_inspector2.types.create_git_lab_self_managed_integration_detail.CreateGitLabSelfManagedIntegrationDetail"


CreateIntegrationDetail: TypeAlias = (
    CreateIntegrationDetailGitlabSelfManagedMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationDetail) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CreateIntegrationDetail: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "gitlabSelfManaged" in value:
        import capo_inspector2.types.create_git_lab_self_managed_integration_detail

        return {
            "gitlabSelfManaged": capo_inspector2.types.create_git_lab_self_managed_integration_detail.serialize_json(
                value["gitlabSelfManaged"]
            )
        }
    else:
        raise SerializationError("CreateIntegrationDetail: no variant present")


def deserialize_json(data: dict) -> CreateIntegrationDetail:
    if data.get("gitlabSelfManaged") is not None:
        import capo_inspector2.types.create_git_lab_self_managed_integration_detail

        return {
            "gitlabSelfManaged": capo_inspector2.types.create_git_lab_self_managed_integration_detail.deserialize_json(
                data["gitlabSelfManaged"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CreateIntegrationDetail: no recognized variant key")


def redact_sensitive(value: CreateIntegrationDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "gitlabSelfManaged" in value:
        import capo_inspector2.types.create_git_lab_self_managed_integration_detail

        out["gitlabSelfManaged"] = (
            capo_inspector2.types.create_git_lab_self_managed_integration_detail.redact_sensitive(
                value["gitlabSelfManaged"]
            )
        )
    return out
