"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchingWorkflowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.matching_workflow_arn
    import capo_entityresolution.types.resolution_type


class MatchingWorkflowSummary(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    workflow_arn: (
        "capo_entityresolution.types.matching_workflow_arn.MatchingWorkflowArn"
    )
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>MatchingWorkflow</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the workflow was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the workflow was last updated.</p>"""
    resolution_type: "capo_entityresolution.types.resolution_type.ResolutionType"
    """<p>The method that has been specified for data matching, either using matching provided by Entity Resolution or through a provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchingWorkflowSummary) -> dict:
    out: dict = {}
    out["workflowName"] = value["workflow_name"]
    out["workflowArn"] = value["workflow_arn"]
    import capo_entityresolution.types._prelude.timestamp

    out["createdAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["updatedAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    import capo_entityresolution.types.resolution_type

    out["resolutionType"] = capo_entityresolution.types.resolution_type.serialize_json(
        value["resolution_type"]
    )
    return out


def deserialize_json(data: dict) -> MatchingWorkflowSummary:
    out: MatchingWorkflowSummary = {}  # type: ignore[typeddict-item]
    if data.get("workflowName") is not None:
        out["workflow_name"] = data["workflowName"]
    else:
        out["workflow_name"] = ""
    if data.get("workflowArn") is not None:
        out["workflow_arn"] = data["workflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["created_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["updated_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("resolutionType") is not None:
        import capo_entityresolution.types.resolution_type

        out["resolution_type"] = (
            capo_entityresolution.types.resolution_type.deserialize_json(
                data["resolutionType"]
            )
        )
    else:
        import typing

        out["resolution_type"] = typing.cast(
            "capo_entityresolution.types.resolution_type.ResolutionType", ""
        )
    return out
