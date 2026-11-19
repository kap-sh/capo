"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetMedicalCodingJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.dataset_id
    import capo_connecthealth.types.job_id
    import capo_connecthealth.types.job_status
    import capo_connecthealth.types.medical_codes_encounter_context
    import capo_connecthealth.types.medical_codes_patient_context
    import capo_connecthealth.types.medical_coding_job_arn
    import capo_connecthealth.types.medical_coding_output
    import capo_connecthealth.types.medical_coding_output_data_config
    import capo_connecthealth.types.non_empty_string
    import capo_connecthealth.types.sensitive_non_empty_string


class GetMedicalCodingJobResponse(TypedDict, closed=True):
    job_id: "capo_connecthealth.types.job_id.JobId"
    """<p>The unique identifier of the medical coding job.</p>"""
    job_arn: "capo_connecthealth.types.medical_coding_job_arn.MedicalCodingJobArn"
    """<p>The Amazon Resource Name (ARN) of the medical coding job.</p>"""
    job_status: "capo_connecthealth.types.job_status.JobStatus"
    """<p>The status of the medical coding job.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The date and time that the medical coding job was created.</p>"""
    updated_time: NotRequired["datetime.datetime"]
    """<p>The date and time that the medical coding job was last updated.</p>"""
    text: "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    """<p>The clinical text that the medical coding job codes.</p>"""
    patient_context: NotRequired[
        "capo_connecthealth.types.medical_codes_patient_context.MedicalCodesPatientContext"
    ]
    """<p>The patient context that you provided for the job.</p>"""
    encounter_context: NotRequired[
        "capo_connecthealth.types.medical_codes_encounter_context.MedicalCodesEncounterContext"
    ]
    """<p>The encounter context that you provided for the job.</p>"""
    output_data_config: "capo_connecthealth.types.medical_coding_output_data_config.MedicalCodingOutputDataConfig"
    """<p>The output configuration that you provided for the job.</p>"""
    dataset_id: NotRequired["capo_connecthealth.types.dataset_id.DatasetId"]
    """<p>The unique identifier of the dataset that the job codes against. Not returned if the job uses the general medical coding knowledge base.</p>"""
    medical_coding_output: NotRequired[
        "capo_connecthealth.types.medical_coding_output.MedicalCodingOutput"
    ]
    """<p>The location of the job results. Returned when the job succeeds.</p>"""
    status_details: NotRequired[
        "capo_connecthealth.types.non_empty_string.NonEmptyString"
    ]
    """<p>Details about the status of the job, such as the reason that it failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalCodingJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["jobArn"] = value["job_arn"]
    import capo_connecthealth.types.job_status

    out["jobStatus"] = capo_connecthealth.types.job_status.serialize_json(
        value["job_status"]
    )
    if "creation_time" in value:
        import capo_connecthealth._protocol.serialize

        out["creationTime"] = capo_connecthealth._protocol.serialize.fmt_date_time(
            value["creation_time"]
        )
    if "updated_time" in value:
        import capo_connecthealth._protocol.serialize

        out["updatedTime"] = capo_connecthealth._protocol.serialize.fmt_date_time(
            value["updated_time"]
        )
    out["text"] = value["text"]
    if "patient_context" in value:
        import capo_connecthealth.types.medical_codes_patient_context

        out["patientContext"] = (
            capo_connecthealth.types.medical_codes_patient_context.serialize_json(
                value["patient_context"]
            )
        )
    if "encounter_context" in value:
        import capo_connecthealth.types.medical_codes_encounter_context

        out["encounterContext"] = (
            capo_connecthealth.types.medical_codes_encounter_context.serialize_json(
                value["encounter_context"]
            )
        )
    import capo_connecthealth.types.medical_coding_output_data_config

    out["outputDataConfig"] = (
        capo_connecthealth.types.medical_coding_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    if "medical_coding_output" in value:
        import capo_connecthealth.types.medical_coding_output

        out["medicalCodingOutput"] = (
            capo_connecthealth.types.medical_coding_output.serialize_json(
                value["medical_coding_output"]
            )
        )
    if "status_details" in value:
        out["statusDetails"] = value["status_details"]
    return out


def deserialize_json(data: dict) -> GetMedicalCodingJobResponse:
    out: GetMedicalCodingJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("jobStatus") is not None:
        import capo_connecthealth.types.job_status

        out["job_status"] = capo_connecthealth.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_connecthealth.types.job_status.JobStatus", ""
        )
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    if data.get("updatedTime") is not None:
        import datetime

        out["updated_time"] = datetime.datetime.fromisoformat(
            data["updatedTime"].replace("Z", "+00:00")
        )
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("patientContext") is not None:
        import capo_connecthealth.types.medical_codes_patient_context

        out["patient_context"] = (
            capo_connecthealth.types.medical_codes_patient_context.deserialize_json(
                data["patientContext"]
            )
        )
    if data.get("encounterContext") is not None:
        import capo_connecthealth.types.medical_codes_encounter_context

        out["encounter_context"] = (
            capo_connecthealth.types.medical_codes_encounter_context.deserialize_json(
                data["encounterContext"]
            )
        )
    if data.get("outputDataConfig") is not None:
        import capo_connecthealth.types.medical_coding_output_data_config

        out["output_data_config"] = (
            capo_connecthealth.types.medical_coding_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetMedicalCodingJobResponse.output_data_config required"
        )
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    if data.get("medicalCodingOutput") is not None:
        import capo_connecthealth.types.medical_coding_output

        out["medical_coding_output"] = (
            capo_connecthealth.types.medical_coding_output.deserialize_json(
                data["medicalCodingOutput"]
            )
        )
    if data.get("statusDetails") is not None:
        out["status_details"] = data["statusDetails"]
    return out


def redact_sensitive(value: GetMedicalCodingJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "patient_context" in value:
        import capo_connecthealth.types.medical_codes_patient_context

        out["patient_context"] = (
            capo_connecthealth.types.medical_codes_patient_context.redact_sensitive(
                value["patient_context"]
            )
        )
    if "encounter_context" in value:
        import capo_connecthealth.types.medical_codes_encounter_context

        out["encounter_context"] = (
            capo_connecthealth.types.medical_codes_encounter_context.redact_sensitive(
                value["encounter_context"]
            )
        )
    return out
