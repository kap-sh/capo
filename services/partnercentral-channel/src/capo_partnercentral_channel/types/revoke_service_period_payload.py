"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RevokeServicePeriodPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.note
    import capo_partnercentral_channel.types.program_management_account_identifier


class RevokeServicePeriodPayload(TypedDict, closed=True):
    program_management_account_identifier: "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account.</p>"""
    note: NotRequired["capo_partnercentral_channel.types.note.Note"]
    """<p>A note explaining the reason for revoking the service period.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RevokeServicePeriodPayload) -> dict:
    out: dict = {}
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    if "note" in value:
        out["note"] = value["note"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RevokeServicePeriodPayload:
    out: RevokeServicePeriodPayload = {}  # type: ignore[typeddict-item]
    if data.get("programManagementAccountIdentifier") is not None:
        out["program_management_account_identifier"] = data[
            "programManagementAccountIdentifier"
        ]
    else:
        out["program_management_account_identifier"] = ""
    if data.get("note") is not None:
        out["note"] = data["note"]
    return out
