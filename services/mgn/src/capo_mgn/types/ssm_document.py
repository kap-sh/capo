"""Generated from Smithy shape ``com.amazonaws.mgn#SsmDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.bounded_string
    import capo_mgn.types.ssm_document_external_parameters
    import capo_mgn.types.ssm_document_name
    import capo_mgn.types.ssm_document_parameters
    import capo_mgn.types.strictly_positive_integer


class SsmDocument(TypedDict, closed=True):
    action_name: "capo_mgn.types.bounded_string.BoundedString"
    """<p>User-friendly name for the AWS Systems Manager Document.</p>"""
    ssm_document_name: "capo_mgn.types.ssm_document_name.SsmDocumentName"
    """<p>AWS Systems Manager Document name or full ARN.</p>"""
    timeout_seconds: NotRequired[
        "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>AWS Systems Manager Document timeout seconds.</p>"""
    must_succeed_for_cutover: NotRequired["bool"]
    """<p>If true, Cutover will not be enabled if the document has failed.</p>"""
    parameters: NotRequired[
        "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
    ]
    """<p>AWS Systems Manager Document parameters.</p>"""
    external_parameters: NotRequired[
        "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
    ]
    """<p>AWS Systems Manager Document external parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsmDocument) -> dict:
    out: dict = {}
    out["actionName"] = value["action_name"]
    out["ssmDocumentName"] = value["ssm_document_name"]
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
    return out


def deserialize_json(data: dict) -> SsmDocument:
    out: SsmDocument = {}  # type: ignore[typeddict-item]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    if data.get("ssmDocumentName") is not None:
        out["ssm_document_name"] = data["ssmDocumentName"]
    else:
        out["ssm_document_name"] = ""
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
    return out
