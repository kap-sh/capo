"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentProfileInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.aws_account_id
    import capo_datazone.types.aws_region
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_parameters_list
    import capo_datazone.types.environment_profile_name
    import capo_datazone.types.project_id


class CreateEnvironmentProfileInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this environment profile is created.</p>"""
    name: "capo_datazone.types.environment_profile_name.EnvironmentProfileName"
    """<p>The name of this Amazon DataZone environment profile.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone environment profile.</p>"""
    environment_blueprint_identifier: (
        "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The ID of the blueprint with which this environment profile is created.</p>"""
    project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project in which to create the environment profile.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The user parameters of this Amazon DataZone environment profile.</p>"""
    aws_account_id: NotRequired["capo_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account in which the Amazon DataZone environment is created.</p>"""
    aws_account_region: NotRequired["capo_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services region in which this environment profile is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentProfileInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["environmentBlueprintIdentifier"] = value["environment_blueprint_identifier"]
    out["projectIdentifier"] = value["project_identifier"]
    if "user_parameters" in value:
        import capo_datazone.types.environment_parameters_list

        out["userParameters"] = (
            capo_datazone.types.environment_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentProfileInput:
    out: CreateEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("environmentBlueprintIdentifier") is not None:
        out["environment_blueprint_identifier"] = data["environmentBlueprintIdentifier"]
    else:
        out["environment_blueprint_identifier"] = ""
    if data.get("projectIdentifier") is not None:
        out["project_identifier"] = data["projectIdentifier"]
    else:
        out["project_identifier"] = ""
    if data.get("userParameters") is not None:
        import capo_datazone.types.environment_parameters_list

        out["user_parameters"] = (
            capo_datazone.types.environment_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("awsAccountRegion") is not None:
        out["aws_account_region"] = data["awsAccountRegion"]
    return out


def redact_sensitive(value: CreateEnvironmentProfileInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
