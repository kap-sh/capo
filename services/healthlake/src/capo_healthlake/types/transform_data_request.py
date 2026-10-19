"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#TransformDataRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.transform_input_data


class TransformDataRequest(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the data transformation profile to use for conversion.</p>"""
    input_data: "capo_healthlake.types.transform_input_data.TransformInputData"
    """<p>The clinical data to transform. Provide either raw C-CDA XML or CSV content.</p>"""
    drift_detection_enabled: NotRequired["bool"]
    """<p>Specifies whether drift detection is enabled for this request. When enabled, HealthLake writes a drift report in the API response.</p>"""
    provenance_enabled: NotRequired["bool"]
    """<p>Specifies whether FHIR R4 Provenance resource generation is enabled for this transformation. When provenance is enabled, the service also generates related DocumentReference and Device resources. If you don't specify a value, the default is <code>true</code>. To disable provenance output, set this parameter to <code>false</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformDataRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    import capo_healthlake.types.transform_input_data

    out["InputData"] = (
        capo_healthlake.types.transform_input_data.serialize_aws_json_1_0(
            value["input_data"]
        )
    )
    if "drift_detection_enabled" in value:
        out["DriftDetectionEnabled"] = value["drift_detection_enabled"]
    if "provenance_enabled" in value:
        out["ProvenanceEnabled"] = value["provenance_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TransformDataRequest:
    out: TransformDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("TransformDataRequest.profile_id required")
    if data.get("InputData") is not None:
        import capo_healthlake.types.transform_input_data

        out["input_data"] = (
            capo_healthlake.types.transform_input_data.deserialize_aws_json_1_0(
                data["InputData"]
            )
        )
    else:
        raise DeserializationError("TransformDataRequest.input_data required")
    if data.get("DriftDetectionEnabled") is not None:
        out["drift_detection_enabled"] = data["DriftDetectionEnabled"]
    if data.get("ProvenanceEnabled") is not None:
        out["provenance_enabled"] = data["ProvenanceEnabled"]
    return out


def redact_sensitive(value: TransformDataRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_data" in value:
        out["input_data"] = "*** Sensitive Data Redacted ***"
    return out
