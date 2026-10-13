"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetPatientInsightsJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.input_data_config
    import capo_connecthealth.types.insights_context
    import capo_connecthealth.types.insights_output
    import capo_connecthealth.types.job_arn
    import capo_connecthealth.types.job_id
    import capo_connecthealth.types.job_status
    import capo_connecthealth.types.non_empty_string
    import capo_connecthealth.types.output_data_config
    import capo_connecthealth.types.patient_insights_encounter_context
    import capo_connecthealth.types.patient_insights_patient_context
    import capo_connecthealth.types.user_context


class GetPatientInsightsJobResponse(TypedDict, closed=True):
    job_id: "capo_connecthealth.types.job_id.JobId"
    """<p/>"""
    job_arn: "capo_connecthealth.types.job_arn.JobArn"
    """<p/>"""
    job_status: "capo_connecthealth.types.job_status.JobStatus"
    """<p/>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>Date and time the patient insights job was submitted.</p>"""
    updated_time: NotRequired["datetime.datetime"]
    """<p>Date and time the patient insights job was last updated.</p>"""
    insights_output: NotRequired[
        "capo_connecthealth.types.insights_output.InsightsOutput"
    ]
    """<p/>"""
    status_details: NotRequired[
        "capo_connecthealth.types.non_empty_string.NonEmptyString"
    ]
    """<p>Contains information about the status of a job.</p>"""
    patient_context: "capo_connecthealth.types.patient_insights_patient_context.PatientInsightsPatientContext"
    """<p/>"""
    insights_context: "capo_connecthealth.types.insights_context.InsightsContext"
    """<p/>"""
    encounter_context: "capo_connecthealth.types.patient_insights_encounter_context.PatientInsightsEncounterContext"
    """<p/>"""
    user_context: "capo_connecthealth.types.user_context.UserContext"
    """<p/>"""
    input_data_config: "capo_connecthealth.types.input_data_config.InputDataConfig"
    """<p/>"""
    output_data_config: "capo_connecthealth.types.output_data_config.OutputDataConfig"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPatientInsightsJobResponse) -> dict:
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
    if "insights_output" in value:
        import capo_connecthealth.types.insights_output

        out["insightsOutput"] = capo_connecthealth.types.insights_output.serialize_json(
            value["insights_output"]
        )
    if "status_details" in value:
        out["statusDetails"] = value["status_details"]
    import capo_connecthealth.types.patient_insights_patient_context

    out["patientContext"] = (
        capo_connecthealth.types.patient_insights_patient_context.serialize_json(
            value["patient_context"]
        )
    )
    import capo_connecthealth.types.insights_context

    out["insightsContext"] = capo_connecthealth.types.insights_context.serialize_json(
        value["insights_context"]
    )
    import capo_connecthealth.types.patient_insights_encounter_context

    out["encounterContext"] = (
        capo_connecthealth.types.patient_insights_encounter_context.serialize_json(
            value["encounter_context"]
        )
    )
    import capo_connecthealth.types.user_context

    out["userContext"] = capo_connecthealth.types.user_context.serialize_json(
        value["user_context"]
    )
    import capo_connecthealth.types.input_data_config

    out["inputDataConfig"] = capo_connecthealth.types.input_data_config.serialize_json(
        value["input_data_config"]
    )
    import capo_connecthealth.types.output_data_config

    out["outputDataConfig"] = (
        capo_connecthealth.types.output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPatientInsightsJobResponse:
    out: GetPatientInsightsJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("GetPatientInsightsJobResponse.job_id required")
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("GetPatientInsightsJobResponse.job_arn required")
    if data.get("jobStatus") is not None:
        import capo_connecthealth.types.job_status

        out["job_status"] = capo_connecthealth.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        raise DeserializationError("GetPatientInsightsJobResponse.job_status required")
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
    if data.get("insightsOutput") is not None:
        import capo_connecthealth.types.insights_output

        out["insights_output"] = (
            capo_connecthealth.types.insights_output.deserialize_json(
                data["insightsOutput"]
            )
        )
    if data.get("statusDetails") is not None:
        out["status_details"] = data["statusDetails"]
    if data.get("patientContext") is not None:
        import capo_connecthealth.types.patient_insights_patient_context

        out["patient_context"] = (
            capo_connecthealth.types.patient_insights_patient_context.deserialize_json(
                data["patientContext"]
            )
        )
    else:
        raise DeserializationError(
            "GetPatientInsightsJobResponse.patient_context required"
        )
    if data.get("insightsContext") is not None:
        import capo_connecthealth.types.insights_context

        out["insights_context"] = (
            capo_connecthealth.types.insights_context.deserialize_json(
                data["insightsContext"]
            )
        )
    else:
        raise DeserializationError(
            "GetPatientInsightsJobResponse.insights_context required"
        )
    if data.get("encounterContext") is not None:
        import capo_connecthealth.types.patient_insights_encounter_context

        out["encounter_context"] = (
            capo_connecthealth.types.patient_insights_encounter_context.deserialize_json(
                data["encounterContext"]
            )
        )
    else:
        raise DeserializationError(
            "GetPatientInsightsJobResponse.encounter_context required"
        )
    if data.get("userContext") is not None:
        import capo_connecthealth.types.user_context

        out["user_context"] = capo_connecthealth.types.user_context.deserialize_json(
            data["userContext"]
        )
    else:
        raise DeserializationError(
            "GetPatientInsightsJobResponse.user_context required"
        )
    if data.get("inputDataConfig") is not None:
        import capo_connecthealth.types.input_data_config

        out["input_data_config"] = (
            capo_connecthealth.types.input_data_config.deserialize_json(
                data["inputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetPatientInsightsJobResponse.input_data_config required"
        )
    if data.get("outputDataConfig") is not None:
        import capo_connecthealth.types.output_data_config

        out["output_data_config"] = (
            capo_connecthealth.types.output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetPatientInsightsJobResponse.output_data_config required"
        )
    return out


def redact_sensitive(value: GetPatientInsightsJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "patient_context" in value:
        import capo_connecthealth.types.patient_insights_patient_context

        out["patient_context"] = (
            capo_connecthealth.types.patient_insights_patient_context.redact_sensitive(
                value["patient_context"]
            )
        )
    if "encounter_context" in value:
        import capo_connecthealth.types.patient_insights_encounter_context

        out["encounter_context"] = (
            capo_connecthealth.types.patient_insights_encounter_context.redact_sensitive(
                value["encounter_context"]
            )
        )
    if "user_context" in value:
        import capo_connecthealth.types.user_context

        out["user_context"] = capo_connecthealth.types.user_context.redact_sensitive(
            value["user_context"]
        )
    if "input_data_config" in value:
        import capo_connecthealth.types.input_data_config

        out["input_data_config"] = (
            capo_connecthealth.types.input_data_config.redact_sensitive(
                value["input_data_config"]
            )
        )
    return out
