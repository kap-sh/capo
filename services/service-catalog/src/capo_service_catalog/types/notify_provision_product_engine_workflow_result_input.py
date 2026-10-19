"""Generated from Smithy shape ``com.amazonaws.servicecatalog#NotifyProvisionProductEngineWorkflowResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.engine_workflow_failure_reason
    import capo_service_catalog.types.engine_workflow_resource_identifier
    import capo_service_catalog.types.engine_workflow_status
    import capo_service_catalog.types.engine_workflow_token
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.record_outputs


class NotifyProvisionProductEngineWorkflowResultInput(TypedDict, closed=True):
    workflow_token: (
        "capo_service_catalog.types.engine_workflow_token.EngineWorkflowToken"
    )
    """<p> The encrypted contents of the provisioning engine execution payload that Service Catalog sends after the Terraform product provisioning workflow starts. </p>"""
    record_id: "capo_service_catalog.types.id.Id"
    """<p> The identifier of the record. </p>"""
    status: "capo_service_catalog.types.engine_workflow_status.EngineWorkflowStatus"
    """<p> The status of the provisioning engine execution. </p>"""
    failure_reason: NotRequired[
        "capo_service_catalog.types.engine_workflow_failure_reason.EngineWorkflowFailureReason"
    ]
    """<p> The reason why the provisioning engine execution failed. </p>"""
    resource_identifier: NotRequired[
        "capo_service_catalog.types.engine_workflow_resource_identifier.EngineWorkflowResourceIdentifier"
    ]
    """<p> The ID for the provisioned product resources that are part of a resource group. </p>"""
    outputs: NotRequired["capo_service_catalog.types.record_outputs.RecordOutputs"]
    """<p> The output of the provisioning engine execution. </p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p> The idempotency token that identifies the provisioning engine execution. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NotifyProvisionProductEngineWorkflowResultInput,
) -> dict:
    out: dict = {}
    out["WorkflowToken"] = value["workflow_token"]
    out["RecordId"] = value["record_id"]
    import capo_service_catalog.types.engine_workflow_status

    out["Status"] = (
        capo_service_catalog.types.engine_workflow_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "resource_identifier" in value:
        import capo_service_catalog.types.engine_workflow_resource_identifier

        out["ResourceIdentifier"] = (
            capo_service_catalog.types.engine_workflow_resource_identifier.serialize_aws_json_1_1(
                value["resource_identifier"]
            )
        )
    if "outputs" in value:
        import capo_service_catalog.types.record_outputs

        out["Outputs"] = (
            capo_service_catalog.types.record_outputs.serialize_aws_json_1_1(
                value["outputs"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NotifyProvisionProductEngineWorkflowResultInput:
    out: NotifyProvisionProductEngineWorkflowResultInput = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowToken") is not None:
        out["workflow_token"] = data["WorkflowToken"]
    else:
        out["workflow_token"] = ""
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    else:
        out["record_id"] = ""
    if data.get("Status") is not None:
        import capo_service_catalog.types.engine_workflow_status

        out["status"] = (
            capo_service_catalog.types.engine_workflow_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_service_catalog.types.engine_workflow_status.EngineWorkflowStatus", ""
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("ResourceIdentifier") is not None:
        import capo_service_catalog.types.engine_workflow_resource_identifier

        out["resource_identifier"] = (
            capo_service_catalog.types.engine_workflow_resource_identifier.deserialize_aws_json_1_1(
                data["ResourceIdentifier"]
            )
        )
    if data.get("Outputs") is not None:
        import capo_service_catalog.types.record_outputs

        out["outputs"] = (
            capo_service_catalog.types.record_outputs.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    return out
