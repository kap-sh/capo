"""Generated from Smithy shape ``com.amazonaws.snowball#GetSnowballUsageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.integer


class GetSnowballUsageResult(TypedDict, closed=True):
    snowball_limit: NotRequired["capo_snowball.types.integer.Integer"]
    """<p>The service limit for number of Snow devices this account can have at once. The default service limit is 1 (one).</p>"""
    snowballs_in_use: NotRequired["capo_snowball.types.integer.Integer"]
    """<p>The number of Snow devices that this account is currently using.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSnowballUsageResult) -> dict:
    out: dict = {}
    if "snowball_limit" in value:
        out["SnowballLimit"] = value["snowball_limit"]
    if "snowballs_in_use" in value:
        out["SnowballsInUse"] = value["snowballs_in_use"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSnowballUsageResult:
    out: GetSnowballUsageResult = {}  # type: ignore[typeddict-item]
    if data.get("SnowballLimit") is not None:
        out["snowball_limit"] = data["SnowballLimit"]
    if data.get("SnowballsInUse") is not None:
        out["snowballs_in_use"] = data["SnowballsInUse"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSnowballUsageResult) -> dict:
    out: dict = {}
    if "snowball_limit" in value:
        out["SnowballLimit"] = value["snowball_limit"]
    if "snowballs_in_use" in value:
        out["SnowballsInUse"] = value["snowballs_in_use"]
    return out


def deserialize_cbor(data: dict) -> GetSnowballUsageResult:
    out: GetSnowballUsageResult = {}  # type: ignore[typeddict-item]
    if data.get("SnowballLimit") is not None:
        out["snowball_limit"] = data["SnowballLimit"]
    if data.get("SnowballsInUse") is not None:
        out["snowballs_in_use"] = data["SnowballsInUse"]
    return out
