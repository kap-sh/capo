"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_validation_category
    import capo_directory_service.types.assessment_validation_name
    import capo_directory_service.types.assessment_validation_status
    import capo_directory_service.types.assessment_validation_status_code
    import capo_directory_service.types.assessment_validation_status_reason
    import capo_directory_service.types.assessment_validation_time_stamp


class AssessmentValidation(TypedDict, closed=True):
    category: NotRequired[
        "capo_directory_service.types.assessment_validation_category.AssessmentValidationCategory"
    ]
    """<p>The category of the validation test.</p>"""
    name: NotRequired[
        "capo_directory_service.types.assessment_validation_name.AssessmentValidationName"
    ]
    """<p>The name of the specific validation test performed within the category.</p>"""
    status: NotRequired[
        "capo_directory_service.types.assessment_validation_status.AssessmentValidationStatus"
    ]
    """<p>The result status of the validation test. Valid values include <code>SUCCESS</code>, <code>FAILED</code>, <code>PENDING</code>, and <code>IN_PROGRESS</code>.</p>"""
    status_code: NotRequired[
        "capo_directory_service.types.assessment_validation_status_code.AssessmentValidationStatusCode"
    ]
    """<p>A detailed status code providing additional information about the validation result.</p>"""
    status_reason: NotRequired[
        "capo_directory_service.types.assessment_validation_status_reason.AssessmentValidationStatusReason"
    ]
    """<p>A human-readable description of the validation result, including any error details or recommendations.</p>"""
    start_time: NotRequired[
        "capo_directory_service.types.assessment_validation_time_stamp.AssessmentValidationTimeStamp"
    ]
    """<p>The date and time when the validation test was started.</p>"""
    last_update_date_time: NotRequired[
        "capo_directory_service.types.assessment_validation_time_stamp.AssessmentValidationTimeStamp"
    ]
    """<p>The date and time when the validation test was completed or last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentValidation) -> dict:
    out: dict = {}
    if "category" in value:
        out["Category"] = value["category"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "start_time" in value:
        import capo_directory_service.types.assessment_validation_time_stamp

        out["StartTime"] = (
            capo_directory_service.types.assessment_validation_time_stamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "last_update_date_time" in value:
        import capo_directory_service.types.assessment_validation_time_stamp

        out["LastUpdateDateTime"] = (
            capo_directory_service.types.assessment_validation_time_stamp.serialize_aws_json_1_1(
                value["last_update_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentValidation:
    out: AssessmentValidation = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("StartTime") is not None:
        import capo_directory_service.types.assessment_validation_time_stamp

        out["start_time"] = (
            capo_directory_service.types.assessment_validation_time_stamp.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if data.get("LastUpdateDateTime") is not None:
        import capo_directory_service.types.assessment_validation_time_stamp

        out["last_update_date_time"] = (
            capo_directory_service.types.assessment_validation_time_stamp.deserialize_aws_json_1_1(
                data["LastUpdateDateTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssessmentValidation) -> dict:
    out: dict = {}
    if "category" in value:
        out["Category"] = value["category"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "start_time" in value:
        import capo_directory_service.types.assessment_validation_time_stamp

        out["StartTime"] = (
            capo_directory_service.types.assessment_validation_time_stamp.serialize_cbor(
                value["start_time"]
            )
        )
    if "last_update_date_time" in value:
        import capo_directory_service.types.assessment_validation_time_stamp

        out["LastUpdateDateTime"] = (
            capo_directory_service.types.assessment_validation_time_stamp.serialize_cbor(
                value["last_update_date_time"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AssessmentValidation:
    out: AssessmentValidation = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusCode") is not None:
        out["status_code"] = data["StatusCode"]
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("StartTime") is not None:
        import capo_directory_service.types.assessment_validation_time_stamp

        out["start_time"] = (
            capo_directory_service.types.assessment_validation_time_stamp.deserialize_cbor(
                data["StartTime"]
            )
        )
    if data.get("LastUpdateDateTime") is not None:
        import capo_directory_service.types.assessment_validation_time_stamp

        out["last_update_date_time"] = (
            capo_directory_service.types.assessment_validation_time_stamp.deserialize_cbor(
                data["LastUpdateDateTime"]
            )
        )
    return out
