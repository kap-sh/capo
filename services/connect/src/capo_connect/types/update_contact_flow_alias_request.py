"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_flow_description
    import capo_connect.types.contact_flow_name
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.resource_id
    import capo_connect.types.resource_version


class UpdateContactFlowAliasRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_id: "capo_connect.types.arn.ARN"
    """<p>The identifier of the flow.</p>"""
    alias_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The identifier of the alias.</p>"""
    name: NotRequired["capo_connect.types.contact_flow_name.ContactFlowName"]
    """<p>The name of the alias.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the alias.</p>"""
    contact_flow_version: NotRequired[
        "capo_connect.types.resource_version.ResourceVersion"
    ]
    """<p>The version of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowAliasRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "contact_flow_version" in value:
        out["ContactFlowVersion"] = value["contact_flow_version"]
    return out


def deserialize_json(data: dict) -> UpdateContactFlowAliasRequest:
    out: UpdateContactFlowAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ContactFlowVersion") is not None:
        out["contact_flow_version"] = data["ContactFlowVersion"]
    return out
