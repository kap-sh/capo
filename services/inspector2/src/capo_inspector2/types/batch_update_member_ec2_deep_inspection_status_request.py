"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchUpdateMemberEc2DeepInspectionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.member_account_ec2_deep_inspection_status_list


class BatchUpdateMemberEc2DeepInspectionStatusRequest(TypedDict, closed=True):
    account_ids: "capo_inspector2.types.member_account_ec2_deep_inspection_status_list.MemberAccountEc2DeepInspectionStatusList"
    """<p>The unique identifiers for the Amazon Web Services accounts to change Amazon Inspector deep inspection status for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateMemberEc2DeepInspectionStatusRequest) -> dict:
    out: dict = {}
    import capo_inspector2.types.member_account_ec2_deep_inspection_status_list

    out["accountIds"] = (
        capo_inspector2.types.member_account_ec2_deep_inspection_status_list.serialize_json(
            value["account_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateMemberEc2DeepInspectionStatusRequest:
    out: BatchUpdateMemberEc2DeepInspectionStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_inspector2.types.member_account_ec2_deep_inspection_status_list

        out["account_ids"] = (
            capo_inspector2.types.member_account_ec2_deep_inspection_status_list.deserialize_json(
                data["accountIds"]
            )
        )
    else:
        out["account_ids"] = []
    return out
