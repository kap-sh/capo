"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFlowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.account_id
    import capo_quicksight.types.flow_description_input
    import capo_quicksight.types.flow_id
    import capo_quicksight.types.sensitive_document
    import capo_quicksight.types.title_input
    import capo_quicksight.types.update_flow_request_client_token_string


class UpdateFlowRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that contains the flow that you are updating.</p>"""
    flow_id: "capo_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow to update.</p>"""
    name: NotRequired["capo_quicksight.types.title_input.TitleInput"]
    """<p>Updated display name for the flow. Omit to preserve the existing name.</p>"""
    description: NotRequired[
        "capo_quicksight.types.flow_description_input.FlowDescriptionInput"
    ]
    """<p>Updated description for the flow. Omit to preserve the existing description.</p>"""
    flow_definition: NotRequired[
        "capo_quicksight.types.sensitive_document.SensitiveDocument"
    ]
    """<p>The definition of the flow, specifying the steps and configurations. This is the flow definition in Quick Flow's internal format. The format is subject to change. When provided, all existing steps are replaced. Omit to preserve the existing definition.</p> <note> <p>Always derive or depend on the flow definition from the <code>DescribeFlow</code> operation to ensure you are working with the latest format.</p> </note>"""
    client_token: NotRequired[
        "capo_quicksight.types.update_flow_request_client_token_string.UpdateFlowRequestClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "flow_definition" in value:
        out["FlowDefinition"] = value["flow_definition"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateFlowRequest:
    out: UpdateFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FlowDefinition") is not None:
        out["flow_definition"] = data["FlowDefinition"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: UpdateFlowRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow_definition" in value:
        out["flow_definition"] = "*** Sensitive Data Redacted ***"
    return out
