"""Generated from Smithy shape ``com.amazonaws.kendra#CreateExperienceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.client_token_name
    import capo_kendra.types.description
    import capo_kendra.types.experience_configuration
    import capo_kendra.types.experience_name
    import capo_kendra.types.index_id
    import capo_kendra.types.role_arn


class CreateExperienceRequest(TypedDict, closed=True):
    name: "capo_kendra.types.experience_name.ExperienceName"
    """<p>A name for your Amazon Kendra experience.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access <code>Query</code> API, <code>GetQuerySuggestions</code> API, and other required APIs. The role also must include permission to access IAM Identity Center that stores your user and group information. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>"""
    configuration: NotRequired[
        "capo_kendra.types.experience_configuration.ExperienceConfiguration"
    ]
    """<p>Configuration information for your Amazon Kendra experience. This includes <code>ContentSourceConfiguration</code>, which specifies the data source IDs and/or FAQ IDs, and <code>UserIdentityConfiguration</code>, which specifies the user or group information to grant access to your Amazon Kendra experience.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A description for your Amazon Kendra experience.</p>"""
    client_token: NotRequired["capo_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create your Amazon Kendra experience. Multiple calls to the <code>CreateExperience</code> API with the same client token creates only one Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExperienceRequest) -> dict:
    out: dict = {}
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExperienceRequest:
    out: CreateExperienceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateExperienceRequest.name required")
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("CreateExperienceRequest.index_id required")
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
