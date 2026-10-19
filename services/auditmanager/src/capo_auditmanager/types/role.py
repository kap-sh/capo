"""Generated from Smithy shape ``com.amazonaws.auditmanager#Role``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.iam_arn
    import capo_auditmanager.types.role_type


class Role(TypedDict, closed=True):
    role_type: "capo_auditmanager.types.role_type.RoleType"
    """<p> The type of customer persona. </p> <note> <p>In <code>CreateAssessment</code>, <code>roleType</code> can only be <code>PROCESS_OWNER</code>. </p> <p>In <code>UpdateSettings</code>, <code>roleType</code> can only be <code>PROCESS_OWNER</code>.</p> <p>In <code>BatchCreateDelegationByAssessment</code>, <code>roleType</code> can only be <code>RESOURCE_OWNER</code>.</p> </note>"""
    role_arn: "capo_auditmanager.types.iam_arn.IamArn"
    """<p> The Amazon Resource Name (ARN) of the IAM role. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Role) -> dict:
    out: dict = {}
    import capo_auditmanager.types.role_type

    out["roleType"] = capo_auditmanager.types.role_type.serialize_json(
        value["role_type"]
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> Role:
    out: Role = {}  # type: ignore[typeddict-item]
    if data.get("roleType") is not None:
        import capo_auditmanager.types.role_type

        out["role_type"] = capo_auditmanager.types.role_type.deserialize_json(
            data["roleType"]
        )
    else:
        import typing

        out["role_type"] = typing.cast("capo_auditmanager.types.role_type.RoleType", "")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
