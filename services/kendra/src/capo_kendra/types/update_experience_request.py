"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateExperienceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.description
    import capo_kendra.types.experience_configuration
    import capo_kendra.types.experience_id
    import capo_kendra.types.experience_name
    import capo_kendra.types.index_id
    import capo_kendra.types.role_arn


class UpdateExperienceRequest(TypedDict, closed=True):
    id: "capo_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience you want to update.</p>"""
    name: NotRequired["capo_kendra.types.experience_name.ExperienceName"]
    """<p>A new name for your Amazon Kendra experience.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the <code>Query</code> API, <code>QuerySuggestions</code> API, <code>SubmitFeedback</code> API, and IAM Identity Center that stores your users and groups information. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM roles for Amazon Kendra</a>.</p>"""
    configuration: NotRequired[
        "capo_kendra.types.experience_configuration.ExperienceConfiguration"
    ]
    """<p>Configuration information you want to update for your Amazon Kendra experience.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A new description for your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExperienceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    out["IndexId"] = value["index_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "configuration" in value:
        import capo_kendra.types.experience_configuration

        out["Configuration"] = (
            capo_kendra.types.experience_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExperienceRequest:
    out: UpdateExperienceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateExperienceRequest.id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("UpdateExperienceRequest.index_id required")
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Configuration") is not None:
        import capo_kendra.types.experience_configuration

        out["configuration"] = (
            capo_kendra.types.experience_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
