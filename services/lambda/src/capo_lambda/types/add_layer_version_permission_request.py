"""Generated from Smithy shape ``com.amazonaws.lambda#AddLayerVersionPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.layer_name
    import capo_lambda.types.layer_permission_allowed_action
    import capo_lambda.types.layer_permission_allowed_principal
    import capo_lambda.types.layer_version_number
    import capo_lambda.types.organization_id
    import capo_lambda.types.statement_id
    import capo_lambda.types.string


class AddLayerVersionPermissionRequest(TypedDict, closed=True):
    layer_name: "capo_lambda.types.layer_name.LayerName"
    """<p>The name or Amazon Resource Name (ARN) of the layer.</p>"""
    version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber"
    """<p>The version number.</p>"""
    statement_id: "capo_lambda.types.statement_id.StatementId"
    """<p>An identifier that distinguishes the policy from others on the same layer version.</p>"""
    action: (
        "capo_lambda.types.layer_permission_allowed_action.LayerPermissionAllowedAction"
    )
    """<p>The API action that grants access to the layer. For example, <code>lambda:GetLayerVersion</code>.</p>"""
    principal: "capo_lambda.types.layer_permission_allowed_principal.LayerPermissionAllowedPrincipal"
    """<p>An account ID, or <code>*</code> to grant layer usage permission to all accounts in an organization, or all Amazon Web Services accounts (if <code>organizationId</code> is not specified). For the last case, make sure that you really do want all Amazon Web Services accounts to have usage permission to this layer. </p>"""
    organization_id: NotRequired["capo_lambda.types.organization_id.OrganizationId"]
    """<p>With the principal set to <code>*</code>, grant permission to all accounts in the specified organization.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddLayerVersionPermissionRequest) -> dict:
    out: dict = {}
    out["StatementId"] = value["statement_id"]
    out["Action"] = value["action"]
    out["Principal"] = value["principal"]
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_json(data: dict) -> AddLayerVersionPermissionRequest:
    out: AddLayerVersionPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("StatementId") is not None:
        out["statement_id"] = data["StatementId"]
    else:
        out["statement_id"] = ""
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        out["action"] = ""
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    else:
        out["principal"] = ""
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    return out
