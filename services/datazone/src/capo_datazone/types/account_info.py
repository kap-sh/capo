"""Generated from Smithy shape ``com.amazonaws.datazone#AccountInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.aws_account_id
    import capo_datazone.types.aws_account_name
    import capo_datazone.types.aws_region_list


class AccountInfo(TypedDict, closed=True):
    aws_account_id: "capo_datazone.types.aws_account_id.AwsAccountId"
    """<p>The account ID.</p>"""
    supported_regions: "capo_datazone.types.aws_region_list.AwsRegionList"
    """<p>The regions supported for an account within an account pool. </p>"""
    aws_account_name: NotRequired["capo_datazone.types.aws_account_name.AwsAccountName"]
    """<p>The account name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountInfo) -> dict:
    out: dict = {}
    out["awsAccountId"] = value["aws_account_id"]
    import capo_datazone.types.aws_region_list

    out["supportedRegions"] = capo_datazone.types.aws_region_list.serialize_json(
        value["supported_regions"]
    )
    if "aws_account_name" in value:
        out["awsAccountName"] = value["aws_account_name"]
    return out


def deserialize_json(data: dict) -> AccountInfo:
    out: AccountInfo = {}  # type: ignore[typeddict-item]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    else:
        out["aws_account_id"] = ""
    if data.get("supportedRegions") is not None:
        import capo_datazone.types.aws_region_list

        out["supported_regions"] = capo_datazone.types.aws_region_list.deserialize_json(
            data["supportedRegions"]
        )
    else:
        out["supported_regions"] = []
    if data.get("awsAccountName") is not None:
        out["aws_account_name"] = data["awsAccountName"]
    return out


def redact_sensitive(value: AccountInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "aws_account_name" in value:
        out["aws_account_name"] = "*** Sensitive Data Redacted ***"
    return out
