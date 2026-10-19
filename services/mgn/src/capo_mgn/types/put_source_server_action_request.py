"""Generated from Smithy shape ``com.amazonaws.mgn#PutSourceServerActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.action_category
    import capo_mgn.types.action_description
    import capo_mgn.types.action_id
    import capo_mgn.types.action_name
    import capo_mgn.types.bounded_string
    import capo_mgn.types.document_version
    import capo_mgn.types.order_type
    import capo_mgn.types.source_server_id
    import capo_mgn.types.ssm_document_external_parameters
    import capo_mgn.types.ssm_document_parameters
    import capo_mgn.types.strictly_positive_integer


class PutSourceServerActionRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>Source server ID.</p>"""
    action_name: "capo_mgn.types.action_name.ActionName"
    """<p>Source server post migration custom action name.</p>"""
    document_identifier: "capo_mgn.types.bounded_string.BoundedString"
    """<p>Source server post migration custom action document identifier.</p>"""
    order: "capo_mgn.types.order_type.OrderType"
    """<p>Source server post migration custom action order.</p>"""
    action_id: "capo_mgn.types.action_id.ActionID"
    """<p>Source server post migration custom action ID.</p>"""
    document_version: NotRequired["capo_mgn.types.document_version.DocumentVersion"]
    """<p>Source server post migration custom action document version.</p>"""
    active: NotRequired["bool"]
    """<p>Source server post migration custom action active status.</p>"""
    timeout_seconds: NotRequired[
        "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Source server post migration custom action timeout in seconds.</p>"""
    must_succeed_for_cutover: NotRequired["bool"]
    """<p>Source server post migration custom action must succeed for cutover.</p>"""
    parameters: NotRequired[
        "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
    ]
    """<p>Source server post migration custom action parameters.</p>"""
    external_parameters: NotRequired[
        "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
    ]
    """<p>Source server post migration custom action external parameters.</p>"""
    description: NotRequired["capo_mgn.types.action_description.ActionDescription"]
    """<p>Source server post migration custom action description.</p>"""
    category: NotRequired["capo_mgn.types.action_category.ActionCategory"]
    """<p>Source server post migration custom action category.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Source server post migration custom account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSourceServerActionRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    out["actionName"] = value["action_name"]
    out["documentIdentifier"] = value["document_identifier"]
    out["order"] = value["order"]
    out["actionID"] = value["action_id"]
    if "document_version" in value:
        out["documentVersion"] = value["document_version"]
    if "active" in value:
        out["active"] = value["active"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "must_succeed_for_cutover" in value:
        out["mustSucceedForCutover"] = value["must_succeed_for_cutover"]
    if "parameters" in value:
        import capo_mgn.types.ssm_document_parameters

        out["parameters"] = capo_mgn.types.ssm_document_parameters.serialize_json(
            value["parameters"]
        )
    if "external_parameters" in value:
        import capo_mgn.types.ssm_document_external_parameters

        out["externalParameters"] = (
            capo_mgn.types.ssm_document_external_parameters.serialize_json(
                value["external_parameters"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> PutSourceServerActionRequest:
    out: PutSourceServerActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    if data.get("documentIdentifier") is not None:
        out["document_identifier"] = data["documentIdentifier"]
    else:
        out["document_identifier"] = ""
    if data.get("order") is not None:
        out["order"] = data["order"]
    else:
        out["order"] = 0
    if data.get("actionID") is not None:
        out["action_id"] = data["actionID"]
    else:
        out["action_id"] = ""
    if data.get("documentVersion") is not None:
        out["document_version"] = data["documentVersion"]
    if data.get("active") is not None:
        out["active"] = data["active"]
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if data.get("mustSucceedForCutover") is not None:
        out["must_succeed_for_cutover"] = data["mustSucceedForCutover"]
    if data.get("parameters") is not None:
        import capo_mgn.types.ssm_document_parameters

        out["parameters"] = capo_mgn.types.ssm_document_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("externalParameters") is not None:
        import capo_mgn.types.ssm_document_external_parameters

        out["external_parameters"] = (
            capo_mgn.types.ssm_document_external_parameters.deserialize_json(
                data["externalParameters"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
