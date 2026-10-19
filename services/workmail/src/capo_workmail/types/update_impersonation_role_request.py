"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateImpersonationRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_role_description
    import capo_workmail.types.impersonation_role_id
    import capo_workmail.types.impersonation_role_name
    import capo_workmail.types.impersonation_role_type
    import capo_workmail.types.impersonation_rule_list
    import capo_workmail.types.organization_id


class UpdateImpersonationRoleRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization that contains the impersonation role to update.</p>"""
    impersonation_role_id: (
        "capo_workmail.types.impersonation_role_id.ImpersonationRoleId"
    )
    """<p>The ID of the impersonation role to update.</p>"""
    name: "capo_workmail.types.impersonation_role_name.ImpersonationRoleName"
    """<p>The updated impersonation role name.</p>"""
    type: "capo_workmail.types.impersonation_role_type.ImpersonationRoleType"
    """<p>The updated impersonation role type.</p>"""
    description: NotRequired[
        "capo_workmail.types.impersonation_role_description.ImpersonationRoleDescription"
    ]
    """<p>The updated impersonation role description.</p>"""
    rules: "capo_workmail.types.impersonation_rule_list.ImpersonationRuleList"
    """<p>The updated list of rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImpersonationRoleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ImpersonationRoleId"] = value["impersonation_role_id"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateImpersonationRoleRequest:
    out: UpdateImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("ImpersonationRoleId") is not None:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    else:
        out["impersonation_role_id"] = ""
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
