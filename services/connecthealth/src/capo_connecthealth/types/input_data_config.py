"""Generated from Smithy shape ``com.amazonaws.connecthealth#InputDataConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.fhir_server
    import capo_connecthealth.types.s3_sources


class InputDataConfig(TypedDict, closed=True):
    fhir_server: NotRequired["capo_connecthealth.types.fhir_server.FHIRServer"]
    """<p>FHIR server configuration to retrieve patient data.</p>"""
    s3_sources: NotRequired["capo_connecthealth.types.s3_sources.S3Sources"]
    """<p>List of S3 sources containing patient data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputDataConfig) -> dict:
    out: dict = {}
    if "fhir_server" in value:
        import capo_connecthealth.types.fhir_server

        out["fhirServer"] = capo_connecthealth.types.fhir_server.serialize_json(
            value["fhir_server"]
        )
    if "s3_sources" in value:
        import capo_connecthealth.types.s3_sources

        out["s3Sources"] = capo_connecthealth.types.s3_sources.serialize_json(
            value["s3_sources"]
        )
    return out


def deserialize_json(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("fhirServer") is not None:
        import capo_connecthealth.types.fhir_server

        out["fhir_server"] = capo_connecthealth.types.fhir_server.deserialize_json(
            data["fhirServer"]
        )
    if data.get("s3Sources") is not None:
        import capo_connecthealth.types.s3_sources

        out["s3_sources"] = capo_connecthealth.types.s3_sources.deserialize_json(
            data["s3Sources"]
        )
    return out


def redact_sensitive(value: InputDataConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fhir_server" in value:
        import capo_connecthealth.types.fhir_server

        out["fhir_server"] = capo_connecthealth.types.fhir_server.redact_sensitive(
            value["fhir_server"]
        )
    return out
