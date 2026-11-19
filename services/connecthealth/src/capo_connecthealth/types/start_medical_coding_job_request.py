"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalCodingJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.dataset_id
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.medical_codes_encounter_context
    import capo_connecthealth.types.medical_codes_patient_context
    import capo_connecthealth.types.medical_coding_output_data_config
    import capo_connecthealth.types.non_empty_string
    import capo_connecthealth.types.sensitive_non_empty_string


class StartMedicalCodingJobRequest(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""
    text: "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    """<p>The clinical text to generate medical codes for, such as a clinical note.</p>"""
    patient_context: NotRequired[
        "capo_connecthealth.types.medical_codes_patient_context.MedicalCodesPatientContext"
    ]
    """<p>Patient context for the job. Providing this information can improve the accuracy of the medical codes.</p>"""
    encounter_context: NotRequired[
        "capo_connecthealth.types.medical_codes_encounter_context.MedicalCodesEncounterContext"
    ]
    """<p>Encounter context for the job. Providing this information can improve the accuracy of the medical codes.</p>"""
    output_data_config: "capo_connecthealth.types.medical_coding_output_data_config.MedicalCodingOutputDataConfig"
    """<p>The output configuration for the job.</p>"""
    dataset_id: NotRequired["capo_connecthealth.types.dataset_id.DatasetId"]
    """<p>The unique identifier of an ACTIVE medical coding dataset in the Domain to code against. If you don't specify a dataset, the job uses the general medical coding knowledge base.</p>"""
    client_token: NotRequired[
        "capo_connecthealth.types.non_empty_string.NonEmptyString"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMedicalCodingJobRequest) -> dict:
    out: dict = {}
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartMedicalCodingJobRequest:
    out: StartMedicalCodingJobRequest = {}  # type: ignore[typeddict-item]
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
            "StartMedicalCodingJobRequest.output_data_config required"
        )
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: StartMedicalCodingJobRequest) -> dict[str, Any]:
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
