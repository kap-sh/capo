"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentResolvedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.account_pool_id
    import capo_datazone.types.aws_account_id
    import capo_datazone.types.aws_region


class EnvironmentResolvedAccount(TypedDict, closed=True):
    aws_account_id: "capo_datazone.types.aws_account_id.AwsAccountId"
    """<p>The ID of the resolved account.</p>"""
    region_name: "capo_datazone.types.aws_region.AwsRegion"
    """<p>The name of the resolved Region.</p>"""
    source_account_pool_id: NotRequired[
        "capo_datazone.types.account_pool_id.AccountPoolId"
    ]
    """<p>The ID of the account pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentResolvedAccount) -> dict:
    out: dict = {}
    out["awsAccountId"] = value["aws_account_id"]
    out["regionName"] = value["region_name"]
    if "source_account_pool_id" in value:
        out["sourceAccountPoolId"] = value["source_account_pool_id"]
    return out


def deserialize_json(data: dict) -> EnvironmentResolvedAccount:
    out: EnvironmentResolvedAccount = {}  # type: ignore[typeddict-item]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    else:
        out["aws_account_id"] = ""
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    else:
        out["region_name"] = ""
    if data.get("sourceAccountPoolId") is not None:
        out["source_account_pool_id"] = data["sourceAccountPoolId"]
    return out
