"""Generated from Smithy shape ``com.amazonaws.groundstation#SecurityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.role_arn
    import capo_groundstation.types.security_group_id_list
    import capo_groundstation.types.subnet_list


class SecurityDetails(TypedDict, closed=True):
    subnet_ids: "capo_groundstation.types.subnet_list.SubnetList"
    """<p>A list of subnets where AWS Ground Station places elastic network interfaces to send streams to your instances.</p>"""
    security_group_ids: (
        "capo_groundstation.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The security groups to attach to the elastic network interfaces.</p>"""
    role_arn: "capo_groundstation.types.role_arn.RoleArn"
    """<p>ARN to a role needed for connecting streams to your instances. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityDetails) -> dict:
    out: dict = {}
    import capo_groundstation.types.subnet_list

    out["subnetIds"] = capo_groundstation.types.subnet_list.serialize_json(
        value["subnet_ids"]
    )
    import capo_groundstation.types.security_group_id_list

    out["securityGroupIds"] = (
        capo_groundstation.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> SecurityDetails:
    out: SecurityDetails = {}  # type: ignore[typeddict-item]
    if data.get("subnetIds") is not None:
        import capo_groundstation.types.subnet_list

        out["subnet_ids"] = capo_groundstation.types.subnet_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroupIds") is not None:
        import capo_groundstation.types.security_group_id_list

        out["security_group_ids"] = (
            capo_groundstation.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
