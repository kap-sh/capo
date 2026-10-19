"""Generated from Smithy shape ``com.amazonaws.codestarconnections#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.security_group_ids
    import capo_codestar_connections.types.subnet_ids
    import capo_codestar_connections.types.tls_certificate
    import capo_codestar_connections.types.vpc_id


class VpcConfiguration(TypedDict, closed=True):
    vpc_id: "capo_codestar_connections.types.vpc_id.VpcId"
    """<p>The ID of the Amazon VPC connected to the infrastructure where your provider type is installed.</p>"""
    subnet_ids: "capo_codestar_connections.types.subnet_ids.SubnetIds"
    """<p>The ID of the subnet or subnets associated with the Amazon VPC connected to the infrastructure where your provider type is installed.</p>"""
    security_group_ids: (
        "capo_codestar_connections.types.security_group_ids.SecurityGroupIds"
    )
    """<p>The ID of the security group or security groups associated with the Amazon VPC connected to the infrastructure where your provider type is installed.</p>"""
    tls_certificate: NotRequired[
        "capo_codestar_connections.types.tls_certificate.TlsCertificate"
    ]
    """<p>The value of the Transport Layer Security (TLS) certificate associated with the infrastructure where your provider type is installed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcConfiguration) -> dict:
    out: dict = {}
    out["VpcId"] = value["vpc_id"]
    import capo_codestar_connections.types.subnet_ids

    out["SubnetIds"] = (
        capo_codestar_connections.types.subnet_ids.serialize_aws_json_1_0(
            value["subnet_ids"]
        )
    )
    import capo_codestar_connections.types.security_group_ids

    out["SecurityGroupIds"] = (
        capo_codestar_connections.types.security_group_ids.serialize_aws_json_1_0(
            value["security_group_ids"]
        )
    )
    if "tls_certificate" in value:
        out["TlsCertificate"] = value["tls_certificate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("SubnetIds") is not None:
        import capo_codestar_connections.types.subnet_ids

        out["subnet_ids"] = (
            capo_codestar_connections.types.subnet_ids.deserialize_aws_json_1_0(
                data["SubnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    if data.get("SecurityGroupIds") is not None:
        import capo_codestar_connections.types.security_group_ids

        out["security_group_ids"] = (
            capo_codestar_connections.types.security_group_ids.deserialize_aws_json_1_0(
                data["SecurityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    if data.get("TlsCertificate") is not None:
        out["tls_certificate"] = data["TlsCertificate"]
    return out
