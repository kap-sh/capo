"""Generated from Smithy shape ``com.amazonaws.aiops#ListInvestigationGroupsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_aiops.types.sensitive_string_with_length_limits


class ListInvestigationGroupsInput(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_aiops.types.sensitive_string_with_length_limits.SensitiveStringWithLengthLimits"
    ]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of service operations.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationGroupsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInvestigationGroupsInput:
    out: ListInvestigationGroupsInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListInvestigationGroupsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
