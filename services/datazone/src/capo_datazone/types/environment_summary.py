"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.aws_account_id
    import capo_datazone.types.aws_region
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_configuration_id
    import capo_datazone.types.environment_configuration_name
    import capo_datazone.types.environment_id
    import capo_datazone.types.environment_name
    import capo_datazone.types.environment_profile_id
    import capo_datazone.types.environment_status
    import capo_datazone.types.project_id


class EnvironmentSummary(TypedDict, closed=True):
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project in which the environment exists.</p>"""
    id: NotRequired["capo_datazone.types.environment_id.EnvironmentId"]
    """<p>The identifier of the environment.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the environment exists.</p>"""
    created_by: "str"
    """<p>The Amazon DataZone user who created the environment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment was updated.</p>"""
    name: "capo_datazone.types.environment_name.EnvironmentName"
    """<p>The name of the environment.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the environment.</p>"""
    environment_profile_id: (
        "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
    )
    """<p>The identifier of the environment profile with which the environment was created.</p>"""
    aws_account_id: NotRequired["capo_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The identifier of the Amazon Web Services account in which an environment exists.</p>"""
    aws_account_region: NotRequired["capo_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region in which an environment exists.</p>"""
    provider: "str"
    """<p>The provider of the environment.</p>"""
    status: NotRequired["capo_datazone.types.environment_status.EnvironmentStatus"]
    """<p>The status of the environment.</p>"""
    environment_configuration_id: NotRequired[
        "capo_datazone.types.environment_configuration_id.EnvironmentConfigurationId"
    ]
    """<p>The configuration ID with which the environment is created.</p>"""
    environment_configuration_name: NotRequired[
        "capo_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The configuration name with which the environment is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSummary) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    if "id" in value:
        out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
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
    out["environmentProfileId"] = value.get("environment_profile_id", "")
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    out["provider"] = value["provider"]
    if "status" in value:
        import capo_datazone.types.environment_status

        out["status"] = capo_datazone.types.environment_status.serialize_json(
            value["status"]
        )
    if "environment_configuration_id" in value:
        out["environmentConfigurationId"] = value["environment_configuration_id"]
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    return out


def deserialize_json(data: dict) -> EnvironmentSummary:
    out: EnvironmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        out["project_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
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
    if data.get("environmentProfileId") is not None:
        out["environment_profile_id"] = data["environmentProfileId"]
    else:
        out["environment_profile_id"] = ""
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("awsAccountRegion") is not None:
        out["aws_account_region"] = data["awsAccountRegion"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("status") is not None:
        import capo_datazone.types.environment_status

        out["status"] = capo_datazone.types.environment_status.deserialize_json(
            data["status"]
        )
    if data.get("environmentConfigurationId") is not None:
        out["environment_configuration_id"] = data["environmentConfigurationId"]
    if data.get("environmentConfigurationName") is not None:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    return out


def redact_sensitive(value: EnvironmentSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "environment_configuration_id" in value:
        out["environment_configuration_id"] = "*** Sensitive Data Redacted ***"
    if "environment_configuration_name" in value:
        out["environment_configuration_name"] = "*** Sensitive Data Redacted ***"
    return out
