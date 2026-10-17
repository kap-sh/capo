"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.resource_id


class CreateContactFlowAliasResponse(TypedDict, closed=True):
    contact_flow_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowAliasResponse) -> dict:
    out: dict = {}
    if "contact_flow_arn" in value:
        out["ContactFlowArn"] = value["contact_flow_arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowAliasResponse:
    out: CreateContactFlowAliasResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContactFlowArn") is not None:
        out["contact_flow_arn"] = data["ContactFlowArn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
