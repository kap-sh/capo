"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowTypeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.description
    import capo_swf.types.registration_status
    import capo_swf.types.timestamp
    import capo_swf.types.workflow_type


class WorkflowTypeInfo(TypedDict, closed=True):
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The workflow type this information is about.</p>"""
    status: "capo_swf.types.registration_status.RegistrationStatus"
    """<p>The current status of the workflow type.</p>"""
    description: NotRequired["capo_swf.types.description.Description"]
    """<p>The description of the type registered through <a>RegisterWorkflowType</a>.</p>"""
    creation_date: "capo_swf.types.timestamp.Timestamp"
    """<p>The date when this type was registered.</p>"""
    deprecation_date: NotRequired["capo_swf.types.timestamp.Timestamp"]
    """<p>If the type is in deprecated state, then it is set to the date when the type was deprecated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowTypeInfo) -> dict:
    out: dict = {}
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    import capo_swf.types.registration_status

    out["status"] = capo_swf.types.registration_status.serialize_aws_json_1_0(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_swf.types.timestamp

    out["creationDate"] = capo_swf.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    if "deprecation_date" in value:
        import capo_swf.types.timestamp

        out["deprecationDate"] = capo_swf.types.timestamp.serialize_aws_json_1_0(
            value["deprecation_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowTypeInfo:
    out: WorkflowTypeInfo = {}  # type: ignore[typeddict-item]
    if data.get("workflowType") is not None:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError("WorkflowTypeInfo.workflow_type required")
    if data.get("status") is not None:
        import capo_swf.types.registration_status

        out["status"] = capo_swf.types.registration_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_swf.types.registration_status.RegistrationStatus", ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creationDate") is not None:
        import capo_swf.types.timestamp

        out["creation_date"] = capo_swf.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("deprecationDate") is not None:
        import capo_swf.types.timestamp

        out["deprecation_date"] = capo_swf.types.timestamp.deserialize_aws_json_1_0(
            data["deprecationDate"]
        )
    return out
