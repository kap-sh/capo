"""Generated from Smithy shape ``com.amazonaws.gamelift#GetGameSessionLogUrlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string


class GetGameSessionLogUrlOutput(TypedDict, closed=True):
    pre_signed_url: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Location of the requested game session logs, available for download. This URL is valid for 15 minutes, after which S3 will reject any download request using this URL. You can request a new URL any time within the 14-day period that the logs are retained.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGameSessionLogUrlOutput) -> dict:
    out: dict = {}
    if "pre_signed_url" in value:
        out["PreSignedUrl"] = value["pre_signed_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGameSessionLogUrlOutput:
    out: GetGameSessionLogUrlOutput = {}  # type: ignore[typeddict-item]
    if data.get("PreSignedUrl") is not None:
        out["pre_signed_url"] = data["PreSignedUrl"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetGameSessionLogUrlOutput) -> dict:
    out: dict = {}
    if "pre_signed_url" in value:
        out["PreSignedUrl"] = value["pre_signed_url"]
    return out


def deserialize_cbor(data: dict) -> GetGameSessionLogUrlOutput:
    out: GetGameSessionLogUrlOutput = {}  # type: ignore[typeddict-item]
    if data.get("PreSignedUrl") is not None:
        out["pre_signed_url"] = data["PreSignedUrl"]
    return out
