"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociateWorkspaceApplicationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_resource_association


class AssociateWorkspaceApplicationResult(TypedDict, closed=True):
    association: NotRequired[
        "capo_workspaces.types.workspace_resource_association.WorkspaceResourceAssociation"
    ]
    """<p>Information about the association between the specified WorkSpace and the specified application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateWorkspaceApplicationResult) -> dict:
    out: dict = {}
    if "association" in value:
        import capo_workspaces.types.workspace_resource_association

        out["Association"] = (
            capo_workspaces.types.workspace_resource_association.serialize_aws_json_1_1(
                value["association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateWorkspaceApplicationResult:
    out: AssociateWorkspaceApplicationResult = {}  # type: ignore[typeddict-item]
    if data.get("Association") is not None:
        import capo_workspaces.types.workspace_resource_association

        out["association"] = (
            capo_workspaces.types.workspace_resource_association.deserialize_aws_json_1_1(
                data["Association"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateWorkspaceApplicationResult) -> dict:
    out: dict = {}
    if "association" in value:
        import capo_workspaces.types.workspace_resource_association

        out["Association"] = (
            capo_workspaces.types.workspace_resource_association.serialize_cbor(
                value["association"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AssociateWorkspaceApplicationResult:
    out: AssociateWorkspaceApplicationResult = {}  # type: ignore[typeddict-item]
    if data.get("Association") is not None:
        import capo_workspaces.types.workspace_resource_association

        out["association"] = (
            capo_workspaces.types.workspace_resource_association.deserialize_cbor(
                data["Association"]
            )
        )
    return out
