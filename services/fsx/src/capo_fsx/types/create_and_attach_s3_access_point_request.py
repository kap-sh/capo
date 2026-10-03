"""Generated from Smithy shape ``com.amazonaws.fsx#CreateAndAttachS3AccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration
    import capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration
    import capo_fsx.types.create_and_attach_s3_access_point_s3_configuration
    import capo_fsx.types.s3_access_point_attachment_name
    import capo_fsx.types.s3_access_point_attachment_type


class CreateAndAttachS3AccessPointRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    name: NotRequired[
        "capo_fsx.types.s3_access_point_attachment_name.S3AccessPointAttachmentName"
    ]
    """<p>The name you want to assign to this S3 access point.</p>"""
    type: NotRequired[
        "capo_fsx.types.s3_access_point_attachment_type.S3AccessPointAttachmentType"
    ]
    """<p>The type of S3 access point you want to create. Only <code>OpenZFS</code> is supported.</p>"""
    open_zfs_configuration: NotRequired[
        "capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration.CreateAndAttachS3AccessPointOpenZFSConfiguration"
    ]
    """<p>Specifies the configuration to use when creating and attaching an S3 access point to an FSx for OpenZFS volume.</p>"""
    ontap_configuration: NotRequired[
        "capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration.CreateAndAttachS3AccessPointOntapConfiguration"
    ]
    s3_access_point: NotRequired[
        "capo_fsx.types.create_and_attach_s3_access_point_s3_configuration.CreateAndAttachS3AccessPointS3Configuration"
    ]
    """<p>Specifies the virtual private cloud (VPC) configuration if you're creating an access point that is restricted to a VPC. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-vpc.html">Creating access points restricted to a virtual private cloud</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAndAttachS3AccessPointRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_fsx.types.s3_access_point_attachment_type

        out["Type"] = (
            capo_fsx.types.s3_access_point_attachment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "open_zfs_configuration" in value:
        import capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration

        out["OpenZFSConfiguration"] = (
            capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    if "ontap_configuration" in value:
        import capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration

        out["OntapConfiguration"] = (
            capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "s3_access_point" in value:
        import capo_fsx.types.create_and_attach_s3_access_point_s3_configuration

        out["S3AccessPoint"] = (
            capo_fsx.types.create_and_attach_s3_access_point_s3_configuration.serialize_aws_json_1_1(
                value["s3_access_point"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAndAttachS3AccessPointRequest:
    out: CreateAndAttachS3AccessPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_fsx.types.s3_access_point_attachment_type

        out["type"] = (
            capo_fsx.types.s3_access_point_attachment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("OpenZFSConfiguration") is not None:
        import capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration

        out["open_zfs_configuration"] = (
            capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    if data.get("OntapConfiguration") is not None:
        import capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration

        out["ontap_configuration"] = (
            capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if data.get("S3AccessPoint") is not None:
        import capo_fsx.types.create_and_attach_s3_access_point_s3_configuration

        out["s3_access_point"] = (
            capo_fsx.types.create_and_attach_s3_access_point_s3_configuration.deserialize_aws_json_1_1(
                data["S3AccessPoint"]
            )
        )
    return out
