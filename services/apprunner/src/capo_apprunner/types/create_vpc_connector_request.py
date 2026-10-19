"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateVpcConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.string_list
    import capo_apprunner.types.tag_list
    import capo_apprunner.types.vpc_connector_name


class CreateVpcConnectorRequest(TypedDict, closed=True):
    vpc_connector_name: "capo_apprunner.types.vpc_connector_name.VpcConnectorName"
    """<p>A name for the VPC connector.</p>"""
    subnets: "capo_apprunner.types.string_list.StringList"
    """<p>A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.</p> <note> <p> App Runner only supports subnets of IP address type <i>IPv4</i> and <i>dual stack</i> (IPv4 and IPv6).</p> </note>"""
    security_groups: NotRequired["capo_apprunner.types.string_list.StringList"]
    """<p>A list of IDs of security groups that App Runner should use for access to Amazon Web Services resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</p>"""
    tags: NotRequired["capo_apprunner.types.tag_list.TagList"]
    """<p>A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVpcConnectorRequest) -> dict:
    out: dict = {}
    out["VpcConnectorName"] = value["vpc_connector_name"]
    import capo_apprunner.types.string_list

    out["Subnets"] = capo_apprunner.types.string_list.serialize_aws_json_1_0(
        value["subnets"]
    )
    if "security_groups" in value:
        import capo_apprunner.types.string_list

        out["SecurityGroups"] = capo_apprunner.types.string_list.serialize_aws_json_1_0(
            value["security_groups"]
        )
    if "tags" in value:
        import capo_apprunner.types.tag_list

        out["Tags"] = capo_apprunner.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVpcConnectorRequest:
    out: CreateVpcConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("VpcConnectorName") is not None:
        out["vpc_connector_name"] = data["VpcConnectorName"]
    else:
        out["vpc_connector_name"] = ""
    if data.get("Subnets") is not None:
        import capo_apprunner.types.string_list

        out["subnets"] = capo_apprunner.types.string_list.deserialize_aws_json_1_0(
            data["Subnets"]
        )
    else:
        out["subnets"] = []
    if data.get("SecurityGroups") is not None:
        import capo_apprunner.types.string_list

        out["security_groups"] = (
            capo_apprunner.types.string_list.deserialize_aws_json_1_0(
                data["SecurityGroups"]
            )
        )
    if data.get("Tags") is not None:
        import capo_apprunner.types.tag_list

        out["tags"] = capo_apprunner.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
