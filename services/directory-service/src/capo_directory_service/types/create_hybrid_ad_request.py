"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateHybridADRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_id
    import capo_directory_service.types.secret_arn
    import capo_directory_service.types.tags


class CreateHybridADRequest(TypedDict, closed=True):
    secret_arn: "capo_directory_service.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials for the service account used to join hybrid domain controllers to your self-managed AD domain. This secret is used once and not stored.</p> <p>The secret must contain key-value pairs with keys matching <code>customerAdAdminDomainUsername</code> and <code>customerAdAdminDomainPassword</code>. For example: <code>{"customerAdAdminDomainUsername":"carlos_salazar","customerAdAdminDomainPassword":"ExamplePassword123!"}</code>.</p>"""
    assessment_id: "capo_directory_service.types.assessment_id.AssessmentId"
    """<p>The unique identifier of the successful directory assessment that validates your self-managed AD environment. You must have a successful directory assessment before you create a hybrid directory.</p>"""
    tags: NotRequired["capo_directory_service.types.tags.Tags"]
    """<p>The tags to be assigned to the directory. Each tag consists of a key and value pair. You can specify multiple tags as a list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHybridADRequest) -> dict:
    out: dict = {}
    out["SecretArn"] = value["secret_arn"]
    out["AssessmentId"] = value["assessment_id"]
    if "tags" in value:
        import capo_directory_service.types.tags

        out["Tags"] = capo_directory_service.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHybridADRequest:
    out: CreateHybridADRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("CreateHybridADRequest.secret_arn required")
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    else:
        raise DeserializationError("CreateHybridADRequest.assessment_id required")
    if data.get("Tags") is not None:
        import capo_directory_service.types.tags

        out["tags"] = capo_directory_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
