"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_validations
    import capo_directory_service.types.ip_addr


class AssessmentReport(TypedDict, closed=True):
    domain_controller_ip: NotRequired["capo_directory_service.types.ip_addr.IpAddr"]
    """<p>The IP address of the domain controller that was tested during the assessment.</p>"""
    validations: NotRequired[
        "capo_directory_service.types.assessment_validations.AssessmentValidations"
    ]
    """<p>A list of validation results for different test categories performed against this domain controller.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentReport) -> dict:
    out: dict = {}
    if "domain_controller_ip" in value:
        out["DomainControllerIp"] = value["domain_controller_ip"]
    if "validations" in value:
        import capo_directory_service.types.assessment_validations

        out["Validations"] = (
            capo_directory_service.types.assessment_validations.serialize_aws_json_1_1(
                value["validations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentReport:
    out: AssessmentReport = {}  # type: ignore[typeddict-item]
    if data.get("DomainControllerIp") is not None:
        out["domain_controller_ip"] = data["DomainControllerIp"]
    if data.get("Validations") is not None:
        import capo_directory_service.types.assessment_validations

        out["validations"] = (
            capo_directory_service.types.assessment_validations.deserialize_aws_json_1_1(
                data["Validations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssessmentReport) -> dict:
    out: dict = {}
    if "domain_controller_ip" in value:
        out["DomainControllerIp"] = value["domain_controller_ip"]
    if "validations" in value:
        import capo_directory_service.types.assessment_validations

        out["Validations"] = (
            capo_directory_service.types.assessment_validations.serialize_cbor(
                value["validations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AssessmentReport:
    out: AssessmentReport = {}  # type: ignore[typeddict-item]
    if data.get("DomainControllerIp") is not None:
        out["domain_controller_ip"] = data["DomainControllerIp"]
    if data.get("Validations") is not None:
        import capo_directory_service.types.assessment_validations

        out["validations"] = (
            capo_directory_service.types.assessment_validations.deserialize_cbor(
                data["Validations"]
            )
        )
    return out
