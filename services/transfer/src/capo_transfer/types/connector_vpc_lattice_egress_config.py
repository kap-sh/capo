"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorVpcLatticeEgressConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.sftp_port
    import capo_transfer.types.vpc_lattice_resource_configuration_arn


class ConnectorVpcLatticeEgressConfig(TypedDict, closed=True):
    resource_configuration_arn: "capo_transfer.types.vpc_lattice_resource_configuration_arn.VpcLatticeResourceConfigurationArn"
    """<p>ARN of the VPC_LATTICE Resource Configuration that defines the target SFTP server location. Must point to a valid Resource Configuration in the customer's VPC with appropriate network connectivity to the SFTP server.</p>"""
    port_number: NotRequired["capo_transfer.types.sftp_port.SftpPort"]
    """<p>Port number for connecting to the SFTP server through VPC_LATTICE. Defaults to 22 if not specified. Must match the port on which the target SFTP server is listening.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorVpcLatticeEgressConfig) -> dict:
    out: dict = {}
    out["ResourceConfigurationArn"] = value["resource_configuration_arn"]
    if "port_number" in value:
        out["PortNumber"] = value["port_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorVpcLatticeEgressConfig:
    out: ConnectorVpcLatticeEgressConfig = {}  # type: ignore[typeddict-item]
    if data.get("ResourceConfigurationArn") is not None:
        out["resource_configuration_arn"] = data["ResourceConfigurationArn"]
    else:
        out["resource_configuration_arn"] = ""
    if data.get("PortNumber") is not None:
        out["port_number"] = data["PortNumber"]
    return out
