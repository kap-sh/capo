"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentProfileOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.aws_account_id
    import capo_datazone.types.aws_region
    import capo_datazone.types.custom_parameter_list
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_profile_id
    import capo_datazone.types.environment_profile_name
    import capo_datazone.types.project_id


class CreateEnvironmentProfileOutput(TypedDict, closed=True):
    id: "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
    """<p>The ID of this Amazon DataZone environment profile.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this environment profile is created.</p>"""
    aws_account_id: NotRequired["capo_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account ID in which this Amazon DataZone environment profile is created.</p>"""
    aws_account_region: NotRequired["capo_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services region in which this Amazon DataZone environment profile is created.</p>"""
    created_by: "str"
    """<p>The Amazon DataZone user who created this environment profile.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when this environment profile was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when this environment profile was updated.</p>"""
    name: "capo_datazone.types.environment_profile_name.EnvironmentProfileName"
    """<p>The name of this Amazon DataZone environment profile.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone environment profile.</p>"""
    environment_blueprint_id: (
        "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The ID of the blueprint with which this environment profile is created.</p>"""
    project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the Amazon DataZone project in which this environment profile is created.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters of this Amazon DataZone environment profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentProfileOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone._protocol.serialize

        out["updatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["environmentBlueprintId"] = value["environment_blueprint_id"]
    if "project_id" in value:
        out["projectId"] = value["project_id"]
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["userParameters"] = (
            capo_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateEnvironmentProfileOutput:
    out: CreateEnvironmentProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("awsAccountRegion") is not None:
        out["aws_account_region"] = data["awsAccountRegion"]
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("environmentBlueprintId") is not None:
        out["environment_blueprint_id"] = data["environmentBlueprintId"]
    else:
        out["environment_blueprint_id"] = ""
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    if data.get("userParameters") is not None:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    return out


def redact_sensitive(value: CreateEnvironmentProfileOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.redact_sensitive(
                value["user_parameters"]
            )
        )
    return out
