"""Generated from Smithy shape ``com.amazonaws.continuum#FindingPosture``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.finding_category
    import capo_continuum.types.finding_compliance_check_list
    import capo_continuum.types.finding_description
    import capo_continuum.types.finding_string_list


class FindingPosture(TypedDict, closed=True):
    application: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """The application the posture was assessed against."""
    application_uid: NotRequired[
        "capo_continuum.types.finding_category.FindingCategory"
    ]
    application_version: NotRequired[
        "capo_continuum.types.finding_category.FindingCategory"
    ]
    control: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """The control assessed, and the producer's description of it."""
    description: NotRequired[
        "capo_continuum.types.finding_description.FindingDescription"
    ]
    standards: NotRequired["capo_continuum.types.finding_string_list.FindingStringList"]
    """Standards and requirements the control maps to."""
    requirements: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]
    checks: NotRequired[
        "capo_continuum.types.finding_compliance_check_list.FindingComplianceCheckList"
    ]
    """The individual checks performed."""
    status: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """The producer's compliance status, and the enum value behind it."""
    status_id: NotRequired["int"]
    """The producer's numeric enum value for `status`."""
    remediation: NotRequired[
        "capo_continuum.types.finding_description.FindingDescription"
    ]
    remediation_references: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FindingPosture) -> dict:
    out: dict = {}
    if "application" in value:
        out["application"] = value["application"]
    if "application_uid" in value:
        out["applicationUid"] = value["application_uid"]
    if "application_version" in value:
        out["applicationVersion"] = value["application_version"]
    if "control" in value:
        out["control"] = value["control"]
    if "description" in value:
        out["description"] = value["description"]
    if "standards" in value:
        import capo_continuum.types.finding_string_list

        out["standards"] = capo_continuum.types.finding_string_list.serialize_json(
            value["standards"]
        )
    if "requirements" in value:
        import capo_continuum.types.finding_string_list

        out["requirements"] = capo_continuum.types.finding_string_list.serialize_json(
            value["requirements"]
        )
    if "checks" in value:
        import capo_continuum.types.finding_compliance_check_list

        out["checks"] = (
            capo_continuum.types.finding_compliance_check_list.serialize_json(
                value["checks"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_id" in value:
        out["statusId"] = value["status_id"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    if "remediation_references" in value:
        import capo_continuum.types.finding_string_list

        out["remediationReferences"] = (
            capo_continuum.types.finding_string_list.serialize_json(
                value["remediation_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingPosture:
    out: FindingPosture = {}  # type: ignore[typeddict-item]
    if data.get("application") is not None:
        out["application"] = data["application"]
    if data.get("applicationUid") is not None:
        out["application_uid"] = data["applicationUid"]
    if data.get("applicationVersion") is not None:
        out["application_version"] = data["applicationVersion"]
    if data.get("control") is not None:
        out["control"] = data["control"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("standards") is not None:
        import capo_continuum.types.finding_string_list

        out["standards"] = capo_continuum.types.finding_string_list.deserialize_json(
            data["standards"]
        )
    if data.get("requirements") is not None:
        import capo_continuum.types.finding_string_list

        out["requirements"] = capo_continuum.types.finding_string_list.deserialize_json(
            data["requirements"]
        )
    if data.get("checks") is not None:
        import capo_continuum.types.finding_compliance_check_list

        out["checks"] = (
            capo_continuum.types.finding_compliance_check_list.deserialize_json(
                data["checks"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusId") is not None:
        out["status_id"] = data["statusId"]
    if data.get("remediation") is not None:
        out["remediation"] = data["remediation"]
    if data.get("remediationReferences") is not None:
        import capo_continuum.types.finding_string_list

        out["remediation_references"] = (
            capo_continuum.types.finding_string_list.deserialize_json(
                data["remediationReferences"]
            )
        )
    return out
