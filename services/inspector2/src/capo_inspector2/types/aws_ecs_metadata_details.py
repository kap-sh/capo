"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEcsMetadataDetails``."""

from typing_extensions import TypedDict


class AwsEcsMetadataDetails(TypedDict, closed=True):
    details_group: "str"
    """<p>The details group information for a task in a cluster.</p>"""
    task_definition_arn: "str"
    """<p>The task definition ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsMetadataDetails) -> dict:
    out: dict = {}
    out["detailsGroup"] = value["details_group"]
    out["taskDefinitionArn"] = value["task_definition_arn"]
    return out


def deserialize_json(data: dict) -> AwsEcsMetadataDetails:
    out: AwsEcsMetadataDetails = {}  # type: ignore[typeddict-item]
    if data.get("detailsGroup") is not None:
        out["details_group"] = data["detailsGroup"]
    else:
        out["details_group"] = ""
    if data.get("taskDefinitionArn") is not None:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    else:
        out["task_definition_arn"] = ""
    return out
