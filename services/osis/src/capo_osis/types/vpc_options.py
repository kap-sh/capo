"""Generated from Smithy shape ``com.amazonaws.osis#VpcOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.security_group_ids
    import capo_osis.types.subnet_ids
    import capo_osis.types.vpc_attachment_options
    import capo_osis.types.vpc_endpoint_management


class VpcOptions(TypedDict, closed=True):
    subnet_ids: "capo_osis.types.subnet_ids.SubnetIds"
    """<p>A list of subnet IDs associated with the VPC endpoint.</p>"""
    security_group_ids: NotRequired[
        "capo_osis.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of security groups associated with the VPC endpoint.</p>"""
    vpc_attachment_options: NotRequired[
        "capo_osis.types.vpc_attachment_options.VpcAttachmentOptions"
    ]
    """<p>Options for attaching a VPC to a pipeline.</p>"""
    vpc_endpoint_management: NotRequired[
        "capo_osis.types.vpc_endpoint_management.VpcEndpointManagement"
    ]
    """<p>Defines whether you or Amazon OpenSearch Ingestion service create and manage the VPC endpoint configured for the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcOptions) -> dict:
    out: dict = {}
    import capo_osis.types.subnet_ids

    out["SubnetIds"] = capo_osis.types.subnet_ids.serialize_json(value["subnet_ids"])
    if "security_group_ids" in value:
        import capo_osis.types.security_group_ids

        out["SecurityGroupIds"] = capo_osis.types.security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    if "vpc_attachment_options" in value:
        import capo_osis.types.vpc_attachment_options

        out["VpcAttachmentOptions"] = (
            capo_osis.types.vpc_attachment_options.serialize_json(
                value["vpc_attachment_options"]
            )
        )
    if "vpc_endpoint_management" in value:
        import capo_osis.types.vpc_endpoint_management

        out["VpcEndpointManagement"] = (
            capo_osis.types.vpc_endpoint_management.serialize_json(
                value["vpc_endpoint_management"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcOptions:
    out: VpcOptions = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_osis.types.subnet_ids

        out["subnet_ids"] = capo_osis.types.subnet_ids.deserialize_json(
            data["SubnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("SecurityGroupIds") is not None:
        import capo_osis.types.security_group_ids

        out["security_group_ids"] = capo_osis.types.security_group_ids.deserialize_json(
            data["SecurityGroupIds"]
        )
    if data.get("VpcAttachmentOptions") is not None:
        import capo_osis.types.vpc_attachment_options

        out["vpc_attachment_options"] = (
            capo_osis.types.vpc_attachment_options.deserialize_json(
                data["VpcAttachmentOptions"]
            )
        )
    if data.get("VpcEndpointManagement") is not None:
        import capo_osis.types.vpc_endpoint_management

        out["vpc_endpoint_management"] = (
            capo_osis.types.vpc_endpoint_management.deserialize_json(
                data["VpcEndpointManagement"]
            )
        )
    return out
