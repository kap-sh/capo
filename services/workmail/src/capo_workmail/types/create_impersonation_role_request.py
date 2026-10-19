"""Generated from Smithy shape ``com.amazonaws.workmail#CreateImpersonationRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.idempotency_client_token
    import capo_workmail.types.impersonation_role_description
    import capo_workmail.types.impersonation_role_name
    import capo_workmail.types.impersonation_role_type
    import capo_workmail.types.impersonation_rule_list
    import capo_workmail.types.organization_id


class CreateImpersonationRoleRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>The idempotency token for the client request.</p>"""
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization to create the new impersonation role within.</p>"""
    name: "capo_workmail.types.impersonation_role_name.ImpersonationRoleName"
    """<p>The name of the new impersonation role.</p>"""
    type: "capo_workmail.types.impersonation_role_type.ImpersonationRoleType"
    """<p>The impersonation role's type. The available impersonation role types are <code>READ_ONLY</code> or <code>FULL_ACCESS</code>.</p>"""
    description: NotRequired[
        "capo_workmail.types.impersonation_role_description.ImpersonationRoleDescription"
    ]
    """<p>The description of the new impersonation role.</p>"""
    rules: "capo_workmail.types.impersonation_rule_list.ImpersonationRuleList"
    """<p>The list of rules for the impersonation role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImpersonationRoleRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
    out["Name"] = value["name"]
    import capo_workmail.types.impersonation_role_type

    out["Type"] = capo_workmail.types.impersonation_role_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_workmail.types.impersonation_rule_list

    out["Rules"] = capo_workmail.types.impersonation_rule_list.serialize_aws_json_1_1(
        value["rules"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImpersonationRoleRequest:
    out: CreateImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_workmail.types.impersonation_role_type

        out["type"] = (
            capo_workmail.types.impersonation_role_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_workmail.types.impersonation_role_type.ImpersonationRoleType", ""
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Rules") is not None:
        import capo_workmail.types.impersonation_rule_list

        out["rules"] = (
            capo_workmail.types.impersonation_rule_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        out["rules"] = []
    return out
