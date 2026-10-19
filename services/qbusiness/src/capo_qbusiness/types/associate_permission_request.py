"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.permission_conditions
    import capo_qbusiness.types.principal_role_arn
    import capo_qbusiness.types.q_iam_actions
    import capo_qbusiness.types.statement_id


class AssociatePermissionRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    statement_id: "capo_qbusiness.types.statement_id.StatementId"
    """<p>A unique identifier for the policy statement.</p>"""
    actions: "capo_qbusiness.types.q_iam_actions.QIamActions"
    """<p>The list of Amazon Q Business actions that the ISV is allowed to perform.</p>"""
    conditions: NotRequired[
        "capo_qbusiness.types.permission_conditions.PermissionConditions"
    ]
    """<p>The conditions that restrict when the permission is effective. These conditions can be used to limit the permission based on specific attributes of the request.</p>"""
    principal: "capo_qbusiness.types.principal_role_arn.PrincipalRoleArn"
    """<p>The Amazon Resource Name of the IAM role for the ISV that is being granted permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePermissionRequest) -> dict:
    out: dict = {}
    out["statementId"] = value["statement_id"]
    import capo_qbusiness.types.q_iam_actions

    out["actions"] = capo_qbusiness.types.q_iam_actions.serialize_json(value["actions"])
    if "conditions" in value:
        import capo_qbusiness.types.permission_conditions

        out["conditions"] = capo_qbusiness.types.permission_conditions.serialize_json(
            value["conditions"]
        )
    out["principal"] = value["principal"]
    return out


def deserialize_json(data: dict) -> AssociatePermissionRequest:
    out: AssociatePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("statementId") is not None:
        out["statement_id"] = data["statementId"]
    else:
        out["statement_id"] = ""
    if data.get("actions") is not None:
        import capo_qbusiness.types.q_iam_actions

        out["actions"] = capo_qbusiness.types.q_iam_actions.deserialize_json(
            data["actions"]
        )
    else:
        out["actions"] = []
    if data.get("conditions") is not None:
        import capo_qbusiness.types.permission_conditions

        out["conditions"] = capo_qbusiness.types.permission_conditions.deserialize_json(
            data["conditions"]
        )
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    else:
        out["principal"] = ""
    return out
