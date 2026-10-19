"""Generated from Smithy shape ``com.amazonaws.deadline#CreateLicenseEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.security_group_id_list
    import capo_deadline.types.subnet_id_list
    import capo_deadline.types.tags
    import capo_deadline.types.vpc_id


class CreateLicenseEndpointRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    vpc_id: "capo_deadline.types.vpc_id.VpcId"
    """<p>The VPC (virtual private cloud) ID to use with the license endpoint.</p>"""
    subnet_ids: "capo_deadline.types.subnet_id_list.SubnetIdList"
    """<p>The subnet IDs.</p>"""
    security_group_ids: "capo_deadline.types.security_group_id_list.SecurityGroupIdList"
    """<p>The security group IDs.</p>"""
    tags: NotRequired["capo_deadline.types.tags.Tags"]
    """<p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLicenseEndpointRequest) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import capo_deadline.types.subnet_id_list

    out["subnetIds"] = capo_deadline.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import capo_deadline.types.security_group_id_list

    out["securityGroupIds"] = capo_deadline.types.security_group_id_list.serialize_json(
        value["security_group_ids"]
    )
    if "tags" in value:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateLicenseEndpointRequest:
    out: CreateLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("subnetIds") is not None:
        import capo_deadline.types.subnet_id_list

        out["subnet_ids"] = capo_deadline.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroupIds") is not None:
        import capo_deadline.types.security_group_id_list

        out["security_group_ids"] = (
            capo_deadline.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    if data.get("tags") is not None:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.deserialize_json(data["tags"])
    return out
