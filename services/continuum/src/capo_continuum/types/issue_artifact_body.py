"""Generated from Smithy shape ``com.amazonaws.continuum#IssueArtifactBody``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError, SerializationError
from capo_continuum.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_continuum.types.issue_artifact_content
    import capo_continuum.types.patch_body
    import capo_continuum.types.prevalidation_signals_body
    import capo_continuum.types.remediation_proposal_body
    import capo_continuum.types.validation_evidence_body


class IssueArtifactBodyValidationEvidenceMember(TypedDict, closed=True):
    validationEvidence: (
        "capo_continuum.types.validation_evidence_body.ValidationEvidenceBody"
    )


class IssueArtifactBodyPrevalidationSignalsMember(TypedDict, closed=True):
    prevalidationSignals: (
        "capo_continuum.types.prevalidation_signals_body.PrevalidationSignalsBody"
    )


class IssueArtifactBodyRemediationProposalMember(TypedDict, closed=True):
    remediationProposal: (
        "capo_continuum.types.remediation_proposal_body.RemediationProposalBody"
    )


class IssueArtifactBodyPatchMember(TypedDict, closed=True):
    patch: "capo_continuum.types.patch_body.PatchBody"


class IssueArtifactBodyRawMember(TypedDict, closed=True):
    raw: "capo_continuum.types.issue_artifact_content.IssueArtifactContent"


IssueArtifactBody: TypeAlias = (
    IssueArtifactBodyValidationEvidenceMember
    | IssueArtifactBodyPrevalidationSignalsMember
    | IssueArtifactBodyRemediationProposalMember
    | IssueArtifactBodyPatchMember
    | IssueArtifactBodyRawMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IssueArtifactBody) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IssueArtifactBody: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "validationEvidence" in value:
        import capo_continuum.types.validation_evidence_body

        return {
            "validationEvidence": capo_continuum.types.validation_evidence_body.serialize_json(
                value["validationEvidence"]
            )
        }
    elif "prevalidationSignals" in value:
        import capo_continuum.types.prevalidation_signals_body

        return {
            "prevalidationSignals": capo_continuum.types.prevalidation_signals_body.serialize_json(
                value["prevalidationSignals"]
            )
        }
    elif "remediationProposal" in value:
        import capo_continuum.types.remediation_proposal_body

        return {
            "remediationProposal": capo_continuum.types.remediation_proposal_body.serialize_json(
                value["remediationProposal"]
            )
        }
    elif "patch" in value:
        import capo_continuum.types.patch_body

        return {"patch": capo_continuum.types.patch_body.serialize_json(value["patch"])}
    elif "raw" in value:
        return {"raw": value["raw"]}
    else:
        raise SerializationError("IssueArtifactBody: no variant present")


def deserialize_json(data: dict) -> IssueArtifactBody:
    if data.get("validationEvidence") is not None:
        import capo_continuum.types.validation_evidence_body

        return {
            "validationEvidence": capo_continuum.types.validation_evidence_body.deserialize_json(
                data["validationEvidence"]
            )
        }
    elif data.get("prevalidationSignals") is not None:
        import capo_continuum.types.prevalidation_signals_body

        return {
            "prevalidationSignals": capo_continuum.types.prevalidation_signals_body.deserialize_json(
                data["prevalidationSignals"]
            )
        }
    elif data.get("remediationProposal") is not None:
        import capo_continuum.types.remediation_proposal_body

        return {
            "remediationProposal": capo_continuum.types.remediation_proposal_body.deserialize_json(
                data["remediationProposal"]
            )
        }
    elif data.get("patch") is not None:
        import capo_continuum.types.patch_body

        return {
            "patch": capo_continuum.types.patch_body.deserialize_json(data["patch"])
        }
    elif data.get("raw") is not None:
        return {"raw": data["raw"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IssueArtifactBody: no recognized variant key")
