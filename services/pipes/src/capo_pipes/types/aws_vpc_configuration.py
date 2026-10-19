"""Generated from Smithy shape ``com.amazonaws.pipes#AwsVpcConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.assign_public_ip
    import capo_pipes.types.security_groups
    import capo_pipes.types.subnets


class AwsVpcConfiguration(TypedDict, closed=True):
    subnets: "capo_pipes.types.subnets.Subnets"
    """<p>Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.</p>"""
    security_groups: NotRequired["capo_pipes.types.security_groups.SecurityGroups"]
    """<p>Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.</p>"""
    assign_public_ip: NotRequired["capo_pipes.types.assign_public_ip.AssignPublicIp"]
    """<p>Specifies whether the task's elastic network interface receives a public IP address. You can specify <code>ENABLED</code> only when <code>LaunchType</code> in <code>EcsParameters</code> is set to <code>FARGATE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsVpcConfiguration) -> dict:
    out: dict = {}
    import capo_pipes.types.subnets

    out["Subnets"] = capo_pipes.types.subnets.serialize_json(value["subnets"])
    if "security_groups" in value:
        import capo_pipes.types.security_groups

        out["SecurityGroups"] = capo_pipes.types.security_groups.serialize_json(
            value["security_groups"]
        )
    if "assign_public_ip" in value:
        out["AssignPublicIp"] = value["assign_public_ip"]
    return out


def deserialize_json(data: dict) -> AwsVpcConfiguration:
    out: AwsVpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Subnets") is not None:
        import capo_pipes.types.subnets

        out["subnets"] = capo_pipes.types.subnets.deserialize_json(data["Subnets"])
    else:
        out["subnets"] = []
    if data.get("SecurityGroups") is not None:
        import capo_pipes.types.security_groups

        out["security_groups"] = capo_pipes.types.security_groups.deserialize_json(
            data["SecurityGroups"]
        )
    if data.get("AssignPublicIp") is not None:
        out["assign_public_ip"] = data["AssignPublicIp"]
    return out


def redact_sensitive(value: AwsVpcConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subnets" in value:
        import capo_pipes.types.subnets

        out["subnets"] = capo_pipes.types.subnets.redact_sensitive(value["subnets"])
    if "security_groups" in value:
        import capo_pipes.types.security_groups

        out["security_groups"] = capo_pipes.types.security_groups.redact_sensitive(
            value["security_groups"]
        )
    return out
