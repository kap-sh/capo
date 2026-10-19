"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListWorkflowsItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.status
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.workflow_type


class ListWorkflowsItem(TypedDict, closed=True):
    workflow_type: "capo_customer_profiles.types.workflow_type.WorkflowType"
    """<p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>"""
    workflow_id: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>Unique identifier for the workflow.</p>"""
    status: "capo_customer_profiles.types.status.Status"
    """<p>Status of workflow execution.</p>"""
    status_description: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>Description for workflow execution status.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Creation timestamp for workflow.</p>"""
    last_updated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Last updated timestamp for workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsItem) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.workflow_type

    out["WorkflowType"] = capo_customer_profiles.types.workflow_type.serialize_json(
        value["workflow_type"]
    )
    out["WorkflowId"] = value["workflow_id"]
    import capo_customer_profiles.types.status

    out["Status"] = capo_customer_profiles.types.status.serialize_json(value["status"])
    out["StatusDescription"] = value["status_description"]
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ListWorkflowsItem:
    out: ListWorkflowsItem = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowType") is not None:
        import capo_customer_profiles.types.workflow_type

        out["workflow_type"] = (
            capo_customer_profiles.types.workflow_type.deserialize_json(
                data["WorkflowType"]
            )
        )
    else:
        import typing

        out["workflow_type"] = typing.cast(
            "capo_customer_profiles.types.workflow_type.WorkflowType", ""
        )
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("Status") is not None:
        import capo_customer_profiles.types.status

        out["status"] = capo_customer_profiles.types.status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_customer_profiles.types.status.Status", "")
    if data.get("StatusDescription") is not None:
        out["status_description"] = data["StatusDescription"]
    else:
        out["status_description"] = ""
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
