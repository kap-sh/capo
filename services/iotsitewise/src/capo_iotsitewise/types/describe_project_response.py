"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.timestamp


class DescribeProjectResponse(TypedDict, closed=True):
    project_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the project.</p>"""
    project_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the project, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId}</code> </p>"""
    project_name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the project.</p>"""
    portal_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the portal that the project is in.</p>"""
    project_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The project's description.</p>"""
    project_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the project was created, in Unix epoch time.</p>"""
    project_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the project was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProjectResponse) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    out["projectArn"] = value["project_arn"]
    out["projectName"] = value["project_name"]
    out["portalId"] = value["portal_id"]
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    import capo_iotsitewise.types.timestamp

    out["projectCreationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["project_creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["projectLastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["project_last_update_date"]
    )
    return out


def deserialize_json(data: dict) -> DescribeProjectResponse:
    out: DescribeProjectResponse = {}  # type: ignore[typeddict-item]
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("DescribeProjectResponse.project_id required")
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("DescribeProjectResponse.project_arn required")
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("DescribeProjectResponse.project_name required")
    if data.get("portalId") is not None:
        out["portal_id"] = data["portalId"]
    else:
        raise DeserializationError("DescribeProjectResponse.portal_id required")
    if data.get("projectDescription") is not None:
        out["project_description"] = data["projectDescription"]
    if data.get("projectCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["project_creation_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["projectCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeProjectResponse.project_creation_date required"
        )
    if data.get("projectLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["project_last_update_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["projectLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeProjectResponse.project_last_update_date required"
        )
    return out
