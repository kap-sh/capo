"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_flow_description
    import capo_connect.types.contact_flow_name
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.resource_version


class CreateContactFlowAliasRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the alias.</p>"""
    contact_flow_id: "capo_connect.types.arn.ARN"
    """<p>The identifier of the flow.</p>"""
    contact_flow_version: "capo_connect.types.resource_version.ResourceVersion"
    """<p>The version of the flow.</p>"""
    alias_name: "capo_connect.types.contact_flow_name.ContactFlowName"
    """<p>The name of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowAliasRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["ContactFlowVersion"] = value["contact_flow_version"]
    out["AliasName"] = value["alias_name"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowAliasRequest:
    out: CreateContactFlowAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ContactFlowVersion") is not None:
        out["contact_flow_version"] = data["ContactFlowVersion"]
    else:
        raise DeserializationError(
            "CreateContactFlowAliasRequest.contact_flow_version required"
        )
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError("CreateContactFlowAliasRequest.alias_name required")
    return out
