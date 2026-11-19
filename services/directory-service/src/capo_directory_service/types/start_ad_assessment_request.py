"""Generated from Smithy shape ``com.amazonaws.directoryservice#StartADAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_configuration
    import capo_directory_service.types.directory_id


class StartADAssessmentRequest(TypedDict, closed=True):
    assessment_configuration: NotRequired[
        "capo_directory_service.types.assessment_configuration.AssessmentConfiguration"
    ]
    """<p>Configuration parameters for the directory assessment, including DNS server information, domain name, Amazon VPC subnet, and Amazon Web Services System Manager managed node details.</p>"""
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory for which to perform the assessment. This should be an existing directory. If the assessment is not for an existing directory, this parameter should be omitted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartADAssessmentRequest) -> dict:
    out: dict = {}
    if "assessment_configuration" in value:
        import capo_directory_service.types.assessment_configuration

        out["AssessmentConfiguration"] = (
            capo_directory_service.types.assessment_configuration.serialize_aws_json_1_1(
                value["assessment_configuration"]
            )
        )
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartADAssessmentRequest:
    out: StartADAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssessmentConfiguration") is not None:
        import capo_directory_service.types.assessment_configuration

        out["assessment_configuration"] = (
            capo_directory_service.types.assessment_configuration.deserialize_aws_json_1_1(
                data["AssessmentConfiguration"]
            )
        )
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartADAssessmentRequest) -> dict:
    out: dict = {}
    if "assessment_configuration" in value:
        import capo_directory_service.types.assessment_configuration

        out["AssessmentConfiguration"] = (
            capo_directory_service.types.assessment_configuration.serialize_cbor(
                value["assessment_configuration"]
            )
        )
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_cbor(data: dict) -> StartADAssessmentRequest:
    out: StartADAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssessmentConfiguration") is not None:
        import capo_directory_service.types.assessment_configuration

        out["assessment_configuration"] = (
            capo_directory_service.types.assessment_configuration.deserialize_cbor(
                data["AssessmentConfiguration"]
            )
        )
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    return out
