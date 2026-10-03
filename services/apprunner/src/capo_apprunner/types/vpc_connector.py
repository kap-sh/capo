"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.integer
    import capo_apprunner.types.string_list
    import capo_apprunner.types.timestamp
    import capo_apprunner.types.vpc_connector_name
    import capo_apprunner.types.vpc_connector_status


class VpcConnector(TypedDict, closed=True):
    vpc_connector_name: NotRequired[
        "capo_apprunner.types.vpc_connector_name.VpcConnectorName"
    ]
    """<p>The customer-provided VPC connector name.</p>"""
    vpc_connector_arn: NotRequired[
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this VPC connector.</p>"""
    vpc_connector_revision: "capo_apprunner.types.integer.Integer"
    """<p>The revision of this VPC connector. It's unique among all the active connectors (<code>"Status": "ACTIVE"</code>) that share the same <code>Name</code>.</p> <note> <p>At this time, App Runner supports only one revision per name.</p> </note>"""
    subnets: NotRequired["capo_apprunner.types.string_list.StringList"]
    """<p>A list of IDs of subnets that App Runner uses for your service. All IDs are of subnets of a single Amazon VPC.</p>"""
    security_groups: NotRequired["capo_apprunner.types.string_list.StringList"]
    """<p>A list of IDs of security groups that App Runner uses for access to Amazon Web Services resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</p>"""
    status: NotRequired["capo_apprunner.types.vpc_connector_status.VpcConnectorStatus"]
    """<p>The current state of the VPC connector. If the status of a connector revision is <code>INACTIVE</code>, it was deleted and can't be used. Inactive connector revisions are permanently removed some time after they are deleted.</p>"""
    created_at: NotRequired["capo_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the VPC connector was created. It's in Unix time stamp format.</p>"""
    deleted_at: NotRequired["capo_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the VPC connector was deleted. It's in Unix time stamp format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcConnector) -> dict:
    out: dict = {}
    if "vpc_connector_name" in value:
        out["VpcConnectorName"] = value["vpc_connector_name"]
    if "vpc_connector_arn" in value:
        out["VpcConnectorArn"] = value["vpc_connector_arn"]
    out["VpcConnectorRevision"] = value.get("vpc_connector_revision", 0)
    if "subnets" in value:
        import capo_apprunner.types.string_list

        out["Subnets"] = capo_apprunner.types.string_list.serialize_aws_json_1_0(
            value["subnets"]
        )
    if "security_groups" in value:
        import capo_apprunner.types.string_list

        out["SecurityGroups"] = capo_apprunner.types.string_list.serialize_aws_json_1_0(
            value["security_groups"]
        )
    if "status" in value:
        import capo_apprunner.types.vpc_connector_status

        out["Status"] = (
            capo_apprunner.types.vpc_connector_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_at" in value:
        import capo_apprunner.types.timestamp

        out["CreatedAt"] = capo_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "deleted_at" in value:
        import capo_apprunner.types.timestamp

        out["DeletedAt"] = capo_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["deleted_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcConnector:
    out: VpcConnector = {}  # type: ignore[typeddict-item]
    if data.get("VpcConnectorName") is not None:
        out["vpc_connector_name"] = data["VpcConnectorName"]
    if data.get("VpcConnectorArn") is not None:
        out["vpc_connector_arn"] = data["VpcConnectorArn"]
    if data.get("VpcConnectorRevision") is not None:
        out["vpc_connector_revision"] = data["VpcConnectorRevision"]
    else:
        out["vpc_connector_revision"] = 0
    if data.get("Subnets") is not None:
        import capo_apprunner.types.string_list

        out["subnets"] = capo_apprunner.types.string_list.deserialize_aws_json_1_0(
            data["Subnets"]
        )
    if data.get("SecurityGroups") is not None:
        import capo_apprunner.types.string_list

        out["security_groups"] = (
            capo_apprunner.types.string_list.deserialize_aws_json_1_0(
                data["SecurityGroups"]
            )
        )
    if data.get("Status") is not None:
        import capo_apprunner.types.vpc_connector_status

        out["status"] = (
            capo_apprunner.types.vpc_connector_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_apprunner.types.timestamp

        out["created_at"] = capo_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if data.get("DeletedAt") is not None:
        import capo_apprunner.types.timestamp

        out["deleted_at"] = capo_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["DeletedAt"]
        )
    return out
