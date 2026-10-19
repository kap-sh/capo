"""Generated from Smithy shape ``com.amazonaws.servicecatalog#NotifyTerminateProvisionedProductEngineWorkflowResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.engine_workflow_failure_reason
    import capo_service_catalog.types.engine_workflow_status
    import capo_service_catalog.types.engine_workflow_token
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token


class NotifyTerminateProvisionedProductEngineWorkflowResultInput(
    TypedDict, closed=True
):
    workflow_token: (
        "capo_service_catalog.types.engine_workflow_token.EngineWorkflowToken"
    )
    """<p> The encrypted contents of the terminate engine execution payload that Service Catalog sends after the Terraform product terminate workflow starts. </p>"""
    record_id: "capo_service_catalog.types.id.Id"
    """<p> The identifier of the record. </p>"""
    status: "capo_service_catalog.types.engine_workflow_status.EngineWorkflowStatus"
    """<p> The status of the terminate engine execution. </p>"""
    failure_reason: NotRequired[
        "capo_service_catalog.types.engine_workflow_failure_reason.EngineWorkflowFailureReason"
    ]
    """<p> The reason why the terminate engine execution failed. </p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p> The idempotency token that identifies the terminate engine execution. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NotifyTerminateProvisionedProductEngineWorkflowResultInput,
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
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NotifyTerminateProvisionedProductEngineWorkflowResultInput:
    out: NotifyTerminateProvisionedProductEngineWorkflowResultInput = {}  # type: ignore[typeddict-item]
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
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    return out
