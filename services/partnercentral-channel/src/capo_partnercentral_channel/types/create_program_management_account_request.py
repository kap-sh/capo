"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateProgramManagementAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.client_token
    import capo_partnercentral_channel.types.program
    import capo_partnercentral_channel.types.program_management_account_display_name
    import capo_partnercentral_channel.types.tag_list


class CreateProgramManagementAccountRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the program management account.</p>"""
    program: "capo_partnercentral_channel.types.program.Program"
    """<p>The program type for the management account.</p>"""
    display_name: "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
    """<p>A human-readable name for the program management account.</p>"""
    account_id: "capo_partnercentral_channel.types.account_id.AccountId"
    """<p>The AWS account ID to associate with the program management account.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_channel.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    tags: NotRequired["capo_partnercentral_channel.types.tag_list.TagList"]
    """<p>Key-value pairs to associate with the program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProgramManagementAccountRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    import capo_partnercentral_channel.types.program

    out["program"] = capo_partnercentral_channel.types.program.serialize_aws_json_1_0(
        value["program"]
    )
    out["displayName"] = value["display_name"]
    out["accountId"] = value["account_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = capo_partnercentral_channel.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProgramManagementAccountRequest:
    out: CreateProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("program") is not None:
        import capo_partnercentral_channel.types.program

        out["program"] = (
            capo_partnercentral_channel.types.program.deserialize_aws_json_1_0(
                data["program"]
            )
        )
    else:
        import typing

        out["program"] = typing.cast(
            "capo_partnercentral_channel.types.program.Program", ""
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = (
            capo_partnercentral_channel.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
