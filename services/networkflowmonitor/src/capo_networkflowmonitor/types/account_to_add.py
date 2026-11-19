"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#AccountToAdd``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.account_id
    import capo_networkflowmonitor.types.aws_region
    import capo_networkflowmonitor.types.org_membership_status


class AccountToAdd(TypedDict, closed=True):
    account_id: "capo_networkflowmonitor.types.account_id.AccountId"
    """<p>The ID of the account that you can add to the monitoring scope.</p>"""
    region: "capo_networkflowmonitor.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region of the traffic that Network Flow Monitor identified for the account.</p>"""
    membership: (
        "capo_networkflowmonitor.types.org_membership_status.OrgMembershipStatus"
    )
    """<p>Whether the account is a member of the same organization as the account that owns the monitor. The membership status can be one of the following</p> <ul> <li> <p> <code>IN_ORG</code>: The account is a member of the same organization.</p> </li> <li> <p> <code>NOT_IN_ORG</code>: The account isn't a member of the same organization.</p> </li> <li> <p> <code>UNKNOWN</code>: Network Flow Monitor can't determine the organization membership of the account.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountToAdd) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["region"] = value["region"]
    import capo_networkflowmonitor.types.org_membership_status

    out["membership"] = (
        capo_networkflowmonitor.types.org_membership_status.serialize_json(
            value["membership"]
        )
    )
    return out


def deserialize_json(data: dict) -> AccountToAdd:
    out: AccountToAdd = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("membership") is not None:
        import capo_networkflowmonitor.types.org_membership_status

        out["membership"] = (
            capo_networkflowmonitor.types.org_membership_status.deserialize_json(
                data["membership"]
            )
        )
    else:
        import typing

        out["membership"] = typing.cast(
            "capo_networkflowmonitor.types.org_membership_status.OrgMembershipStatus",
            "",
        )
    return out
