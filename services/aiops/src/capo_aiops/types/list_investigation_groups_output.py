"""Generated from Smithy shape ``com.amazonaws.aiops#ListInvestigationGroupsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_aiops.types.investigation_groups
    import capo_aiops.types.sensitive_string_with_length_limits


class ListInvestigationGroupsOutput(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_aiops.types.sensitive_string_with_length_limits.SensitiveStringWithLengthLimits"
    ]
    """<p>Include this value in your next use of this operation to get the next set of service operations.</p>"""
    investigation_groups: NotRequired[
        "capo_aiops.types.investigation_groups.InvestigationGroups"
    ]
    """<p>An array of structures, where each structure contains the information about one investigation group in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationGroupsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "investigation_groups" in value:
        import capo_aiops.types.investigation_groups

        out["investigationGroups"] = (
            capo_aiops.types.investigation_groups.serialize_json(
                value["investigation_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListInvestigationGroupsOutput:
    out: ListInvestigationGroupsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("investigationGroups") is not None:
        import capo_aiops.types.investigation_groups

        out["investigation_groups"] = (
            capo_aiops.types.investigation_groups.deserialize_json(
                data["investigationGroups"]
            )
        )
    return out


def redact_sensitive(value: ListInvestigationGroupsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
