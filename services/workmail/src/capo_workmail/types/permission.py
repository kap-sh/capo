"""Generated from Smithy shape ``com.amazonaws.workmail#Permission``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.member_type
    import capo_workmail.types.permission_values
    import capo_workmail.types.work_mail_identifier


class Permission(TypedDict, closed=True):
    grantee_id: "capo_workmail.types.work_mail_identifier.WorkMailIdentifier"
    """<p>The identifier of the user, group, or resource to which the permissions are granted.</p>"""
    grantee_type: "capo_workmail.types.member_type.MemberType"
    """<p>The type of user, group, or resource referred to in GranteeId.</p>"""
    permission_values: "capo_workmail.types.permission_values.PermissionValues"
    """<p>The permissions granted to the grantee. SEND_AS allows the grantee to send email as the owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the owner of the mailbox (the grantee is not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee full access to the mailbox, irrespective of other folder-level permissions set on the mailbox.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Permission) -> dict:
    out: dict = {}
    out["GranteeId"] = value["grantee_id"]
    import capo_workmail.types.member_type

    out["GranteeType"] = capo_workmail.types.member_type.serialize_aws_json_1_1(
        value["grantee_type"]
    )
    import capo_workmail.types.permission_values

    out["PermissionValues"] = (
        capo_workmail.types.permission_values.serialize_aws_json_1_1(
            value["permission_values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if data.get("GranteeId") is not None:
        out["grantee_id"] = data["GranteeId"]
    else:
        out["grantee_id"] = ""
    if data.get("GranteeType") is not None:
        import capo_workmail.types.member_type

        out["grantee_type"] = capo_workmail.types.member_type.deserialize_aws_json_1_1(
            data["GranteeType"]
        )
    else:
        import typing

        out["grantee_type"] = typing.cast(
            "capo_workmail.types.member_type.MemberType", ""
        )
    if data.get("PermissionValues") is not None:
        import capo_workmail.types.permission_values

        out["permission_values"] = (
            capo_workmail.types.permission_values.deserialize_aws_json_1_1(
                data["PermissionValues"]
            )
        )
    else:
        out["permission_values"] = []
    return out
