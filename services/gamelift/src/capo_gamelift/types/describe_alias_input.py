"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.alias_id_or_arn


class DescribeAliasInput(TypedDict, closed=True):
    alias_id: NotRequired["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"]
    """<p>The unique identifier for the fleet alias that you want to retrieve. You can use either the alias ID or ARN value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAliasInput) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAliasInput:
    out: DescribeAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAliasInput) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    return out


def deserialize_cbor(data: dict) -> DescribeAliasInput:
    out: DescribeAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    return out
