"""Generated from Smithy shape ``com.amazonaws.connect#BatchGetFlowAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.list_flow_association_resource_type
    import capo_connect.types.resource_arn_list_max_limit100


class BatchGetFlowAssociationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    resource_ids: (
        "capo_connect.types.resource_arn_list_max_limit100.resourceArnListMaxLimit100"
    )
    """<p>A list of resource identifiers to retrieve flow associations.</p> <ul> <li> <p>Amazon Web Services End User Messaging SMS phone number ARN when using <code>SMS_PHONE_NUMBER</code> </p> </li> <li> <p>Amazon Web Services End User Messaging Social phone number ARN when using <code>WHATSAPP_MESSAGING_PHONE_NUMBER</code> </p> </li> </ul>"""
    resource_type: NotRequired[
        "capo_connect.types.list_flow_association_resource_type.ListFlowAssociationResourceType"
    ]
    """<p>The type of resource association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFlowAssociationRequest) -> dict:
    out: dict = {}
    import capo_connect.types.resource_arn_list_max_limit100

    out["ResourceIds"] = (
        capo_connect.types.resource_arn_list_max_limit100.serialize_json(
            value["resource_ids"]
        )
    )
    if "resource_type" in value:
        import capo_connect.types.list_flow_association_resource_type

        out["ResourceType"] = (
            capo_connect.types.list_flow_association_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetFlowAssociationRequest:
    out: BatchGetFlowAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceIds") is not None:
        import capo_connect.types.resource_arn_list_max_limit100

        out["resource_ids"] = (
            capo_connect.types.resource_arn_list_max_limit100.deserialize_json(
                data["ResourceIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetFlowAssociationRequest.resource_ids required"
        )
    if data.get("ResourceType") is not None:
        import capo_connect.types.list_flow_association_resource_type

        out["resource_type"] = (
            capo_connect.types.list_flow_association_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    return out
