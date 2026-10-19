"""Generated from Smithy shape ``com.amazonaws.mturk#UpdateQualificationTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.boolean
    import capo_mturk.types.entity_id
    import capo_mturk.types.integer
    import capo_mturk.types.long
    import capo_mturk.types.qualification_type_status
    import capo_mturk.types.string


class UpdateQualificationTypeRequest(TypedDict, closed=True):
    qualification_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the Qualification type to update.</p>"""
    description: NotRequired["capo_mturk.types.string.String"]
    """<p>The new description of the Qualification type.</p>"""
    qualification_type_status: NotRequired[
        "capo_mturk.types.qualification_type_status.QualificationTypeStatus"
    ]
    """<p>The new status of the Qualification type - Active | Inactive</p>"""
    test: NotRequired["capo_mturk.types.string.String"]
    """<p>The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, <code>TestDurationInSeconds</code> must also be specified.</p> <p>Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.</p> <p>Constraints: None. If not specified, the Worker may request the Qualification without answering any questions.</p>"""
    answer_key: NotRequired["capo_mturk.types.string.String"]
    """<p>The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.</p>"""
    test_duration_in_seconds: NotRequired["capo_mturk.types.long.Long"]
    """<p>The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.</p>"""
    retry_delay_in_seconds: NotRequired["capo_mturk.types.long.Long"]
    """<p>The amount of time, in seconds, that Workers must wait after requesting a Qualification of the specified Qualification type before they can retry the Qualification request. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must dispose of the existing retry-enabled Qualification type using DisposeQualificationType and then create a new Qualification type with retries disabled using CreateQualificationType.</p>"""
    auto_granted: NotRequired["capo_mturk.types.boolean.Boolean"]
    """<p>Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.</p> <p>Constraints: If the Test parameter is specified, this parameter cannot be true.</p>"""
    auto_granted_value: NotRequired["capo_mturk.types.integer.Integer"]
    """<p>The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQualificationTypeRequest) -> dict:
    out: dict = {}
    out["QualificationTypeId"] = value["qualification_type_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "qualification_type_status" in value:
        import capo_mturk.types.qualification_type_status

        out["QualificationTypeStatus"] = (
            capo_mturk.types.qualification_type_status.serialize_aws_json_1_1(
                value["qualification_type_status"]
            )
        )
    if "test" in value:
        out["Test"] = value["test"]
    if "answer_key" in value:
        out["AnswerKey"] = value["answer_key"]
    if "test_duration_in_seconds" in value:
        out["TestDurationInSeconds"] = value["test_duration_in_seconds"]
    if "retry_delay_in_seconds" in value:
        out["RetryDelayInSeconds"] = value["retry_delay_in_seconds"]
    if "auto_granted" in value:
        out["AutoGranted"] = value["auto_granted"]
    if "auto_granted_value" in value:
        out["AutoGrantedValue"] = value["auto_granted_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateQualificationTypeRequest:
    out: UpdateQualificationTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("QualificationTypeId") is not None:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        out["qualification_type_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("QualificationTypeStatus") is not None:
        import capo_mturk.types.qualification_type_status

        out["qualification_type_status"] = (
            capo_mturk.types.qualification_type_status.deserialize_aws_json_1_1(
                data["QualificationTypeStatus"]
            )
        )
    if data.get("Test") is not None:
        out["test"] = data["Test"]
    if data.get("AnswerKey") is not None:
        out["answer_key"] = data["AnswerKey"]
    if data.get("TestDurationInSeconds") is not None:
        out["test_duration_in_seconds"] = data["TestDurationInSeconds"]
    if data.get("RetryDelayInSeconds") is not None:
        out["retry_delay_in_seconds"] = data["RetryDelayInSeconds"]
    if data.get("AutoGranted") is not None:
        out["auto_granted"] = data["AutoGranted"]
    if data.get("AutoGrantedValue") is not None:
        out["auto_granted_value"] = data["AutoGrantedValue"]
    return out
