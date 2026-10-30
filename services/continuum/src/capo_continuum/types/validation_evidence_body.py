"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationEvidenceBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.attack_flow_ids
    import capo_continuum.types.exploitability_verdict
    import capo_continuum.types.flow_verdicts
    import capo_continuum.types.per_finding_results
    import capo_continuum.types.validation_executed_proof
    import capo_continuum.types.validation_exploit_artifact
    import capo_continuum.types.validation_source_analysis
    import capo_continuum.types.validation_terminal_status


class ValidationEvidenceBody(TypedDict, closed=True):
    exploitable: "capo_continuum.types.exploitability_verdict.ExploitabilityVerdict"
    """Exploitability verdict. Explicit UNCERTAIN replaces the producer's tri-state `exploitable: true | false | null`, so an absent verdict is never confused with a negative one."""
    terminal_status: NotRequired[
        "capo_continuum.types.validation_terminal_status.ValidationTerminalStatus"
    ]
    """How the validation run ended. Absent when the producer reported a status with no mapping yet: the rest of the body still projects, so one unmapped enum never costs a customer the whole artifact."""
    flow_verdicts: NotRequired["capo_continuum.types.flow_verdicts.FlowVerdicts"]
    """One verdict per attack flow assessed in the bundle."""
    attack_flows_confirmed: NotRequired[
        "capo_continuum.types.attack_flow_ids.AttackFlowIds"
    ]
    """Identifiers of attack flows upgraded to Confirmed provenance."""
    exploit_artifact: NotRequired[
        "capo_continuum.types.validation_exploit_artifact.ValidationExploitArtifact"
    ]
    """Concrete payload and its observed effect, when validation produced one by sending an HTTP request. Only an HTTP proof projects here. A validation agent that proves exploitability by RUNNING code against the repository projects `executedProof`, and one that proves it by reading the source projects `sourceAnalysis`. All three are mutually exclusive: at most one is present."""
    executed_proof: NotRequired[
        "capo_continuum.types.validation_executed_proof.ValidationExecutedProof"
    ]
    """Proof the agent produced by executing code against the repository under test, with the output that execution produced."""
    source_analysis: NotRequired[
        "capo_continuum.types.validation_source_analysis.ValidationSourceAnalysis"
    ]
    """Proof the agent produced by reading the repository's source, with nothing built or run."""
    per_finding_results: NotRequired[
        "capo_continuum.types.per_finding_results.PerFindingResults"
    ]
    """Per-finding breakdown for a multi-finding bundle. Absent for a single-finding bundle."""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationEvidenceBody) -> dict:
    out: dict = {}
    import capo_continuum.types.exploitability_verdict

    out["exploitable"] = capo_continuum.types.exploitability_verdict.serialize_json(
        value["exploitable"]
    )
    if "terminal_status" in value:
        import capo_continuum.types.validation_terminal_status

        out["terminalStatus"] = (
            capo_continuum.types.validation_terminal_status.serialize_json(
                value["terminal_status"]
            )
        )
    if "flow_verdicts" in value:
        import capo_continuum.types.flow_verdicts

        out["flowVerdicts"] = capo_continuum.types.flow_verdicts.serialize_json(
            value["flow_verdicts"]
        )
    if "attack_flows_confirmed" in value:
        import capo_continuum.types.attack_flow_ids

        out["attackFlowsConfirmed"] = (
            capo_continuum.types.attack_flow_ids.serialize_json(
                value["attack_flows_confirmed"]
            )
        )
    if "exploit_artifact" in value:
        import capo_continuum.types.validation_exploit_artifact

        out["exploitArtifact"] = (
            capo_continuum.types.validation_exploit_artifact.serialize_json(
                value["exploit_artifact"]
            )
        )
    if "executed_proof" in value:
        import capo_continuum.types.validation_executed_proof

        out["executedProof"] = (
            capo_continuum.types.validation_executed_proof.serialize_json(
                value["executed_proof"]
            )
        )
    if "source_analysis" in value:
        import capo_continuum.types.validation_source_analysis

        out["sourceAnalysis"] = (
            capo_continuum.types.validation_source_analysis.serialize_json(
                value["source_analysis"]
            )
        )
    if "per_finding_results" in value:
        import capo_continuum.types.per_finding_results

        out["perFindingResults"] = (
            capo_continuum.types.per_finding_results.serialize_json(
                value["per_finding_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationEvidenceBody:
    out: ValidationEvidenceBody = {}  # type: ignore[typeddict-item]
    if data.get("exploitable") is not None:
        import capo_continuum.types.exploitability_verdict

        out["exploitable"] = (
            capo_continuum.types.exploitability_verdict.deserialize_json(
                data["exploitable"]
            )
        )
    else:
        import typing

        out["exploitable"] = typing.cast(
            "capo_continuum.types.exploitability_verdict.ExploitabilityVerdict", ""
        )
    if data.get("terminalStatus") is not None:
        import capo_continuum.types.validation_terminal_status

        out["terminal_status"] = (
            capo_continuum.types.validation_terminal_status.deserialize_json(
                data["terminalStatus"]
            )
        )
    if data.get("flowVerdicts") is not None:
        import capo_continuum.types.flow_verdicts

        out["flow_verdicts"] = capo_continuum.types.flow_verdicts.deserialize_json(
            data["flowVerdicts"]
        )
    if data.get("attackFlowsConfirmed") is not None:
        import capo_continuum.types.attack_flow_ids

        out["attack_flows_confirmed"] = (
            capo_continuum.types.attack_flow_ids.deserialize_json(
                data["attackFlowsConfirmed"]
            )
        )
    if data.get("exploitArtifact") is not None:
        import capo_continuum.types.validation_exploit_artifact

        out["exploit_artifact"] = (
            capo_continuum.types.validation_exploit_artifact.deserialize_json(
                data["exploitArtifact"]
            )
        )
    if data.get("executedProof") is not None:
        import capo_continuum.types.validation_executed_proof

        out["executed_proof"] = (
            capo_continuum.types.validation_executed_proof.deserialize_json(
                data["executedProof"]
            )
        )
    if data.get("sourceAnalysis") is not None:
        import capo_continuum.types.validation_source_analysis

        out["source_analysis"] = (
            capo_continuum.types.validation_source_analysis.deserialize_json(
                data["sourceAnalysis"]
            )
        )
    if data.get("perFindingResults") is not None:
        import capo_continuum.types.per_finding_results

        out["per_finding_results"] = (
            capo_continuum.types.per_finding_results.deserialize_json(
                data["perFindingResults"]
            )
        )
    return out
