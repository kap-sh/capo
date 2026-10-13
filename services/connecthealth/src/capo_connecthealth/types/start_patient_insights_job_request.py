"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartPatientInsightsJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.input_data_config
    import capo_connecthealth.types.insights_context
    import capo_connecthealth.types.non_empty_string
    import capo_connecthealth.types.output_data_config
    import capo_connecthealth.types.patient_insights_encounter_context
    import capo_connecthealth.types.patient_insights_patient_context
    import capo_connecthealth.types.user_context


class StartPatientInsightsJobRequest(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p/>"""
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
    client_token: NotRequired[
        "capo_connecthealth.types.non_empty_string.NonEmptyString"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPatientInsightsJobRequest) -> dict:
    out: dict = {}
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartPatientInsightsJobRequest:
    out: StartPatientInsightsJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("patientContext") is not None:
        import capo_connecthealth.types.patient_insights_patient_context

        out["patient_context"] = (
            capo_connecthealth.types.patient_insights_patient_context.deserialize_json(
                data["patientContext"]
            )
        )
    else:
        raise DeserializationError(
            "StartPatientInsightsJobRequest.patient_context required"
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
            "StartPatientInsightsJobRequest.insights_context required"
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
            "StartPatientInsightsJobRequest.encounter_context required"
        )
    if data.get("userContext") is not None:
        import capo_connecthealth.types.user_context

        out["user_context"] = capo_connecthealth.types.user_context.deserialize_json(
            data["userContext"]
        )
    else:
        raise DeserializationError(
            "StartPatientInsightsJobRequest.user_context required"
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
            "StartPatientInsightsJobRequest.input_data_config required"
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
            "StartPatientInsightsJobRequest.output_data_config required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: StartPatientInsightsJobRequest) -> dict[str, Any]:
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
