"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetMonitorScopeSuggestionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.account_to_add_list
    import capo_networkflowmonitor.types.iso8601_timestamp
    import capo_networkflowmonitor.types.scope_coverage_status


class GetMonitorScopeSuggestionsOutput(TypedDict, closed=True):
    status: "capo_networkflowmonitor.types.scope_coverage_status.ScopeCoverageStatus"
    """<p>The coverage status of the monitoring scope for the monitor. The status can be one of the following</p> <ul> <li> <p> <code>COMPLETE</code>: The scope includes every account that sends traffic to, or receives traffic from, resources in the monitor.</p> </li> <li> <p> <code>INCOMPLETE</code>: There are accounts that you can add to the scope.</p> </li> <li> <p> <code>PENDING</code>: Network Flow Monitor is determining the coverage of the scope.</p> </li> <li> <p> <code>STALE</code>: The coverage of the scope was last determined too long ago to be current.</p> </li> </ul>"""
    accounts_to_add: (
        "capo_networkflowmonitor.types.account_to_add_list.AccountToAddList"
    )
    """<p>The accounts that you can add to the monitoring scope, so that Network Flow Monitor can resolve the network paths for traffic to and from resources in those accounts.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    updated_at: NotRequired[
        "capo_networkflowmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The date and time when Network Flow Monitor last determined the coverage of the monitoring scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorScopeSuggestionsOutput) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.scope_coverage_status

    out["status"] = capo_networkflowmonitor.types.scope_coverage_status.serialize_json(
        value["status"]
    )
    import capo_networkflowmonitor.types.account_to_add_list

    out["accountsToAdd"] = (
        capo_networkflowmonitor.types.account_to_add_list.serialize_json(
            value["accounts_to_add"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "updated_at" in value:
        import capo_networkflowmonitor.types.iso8601_timestamp

        out["updatedAt"] = (
            capo_networkflowmonitor.types.iso8601_timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMonitorScopeSuggestionsOutput:
    out: GetMonitorScopeSuggestionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_networkflowmonitor.types.scope_coverage_status

        out["status"] = (
            capo_networkflowmonitor.types.scope_coverage_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_networkflowmonitor.types.scope_coverage_status.ScopeCoverageStatus",
            "",
        )
    if data.get("accountsToAdd") is not None:
        import capo_networkflowmonitor.types.account_to_add_list

        out["accounts_to_add"] = (
            capo_networkflowmonitor.types.account_to_add_list.deserialize_json(
                data["accountsToAdd"]
            )
        )
    else:
        out["accounts_to_add"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("updatedAt") is not None:
        import capo_networkflowmonitor.types.iso8601_timestamp

        out["updated_at"] = (
            capo_networkflowmonitor.types.iso8601_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
