"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberAccountRankings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.member_account_ranking

MemberAccountRankings: TypeAlias = list[
    "capo_guardduty.types.member_account_ranking.MemberAccountRanking"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberAccountRankings) -> list:
    import capo_guardduty.types.member_account_ranking

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.member_account_ranking.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberAccountRankings:
    import capo_guardduty.types.member_account_ranking

    out: MemberAccountRankings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.member_account_ranking.deserialize_json(item))
    return out
