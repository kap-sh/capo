"""Generated from Smithy shape ``com.amazonaws.snowball#GetJobUnlockCodeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.string


class GetJobUnlockCodeResult(TypedDict, closed=True):
    unlock_code: NotRequired["capo_snowball.types.string.String"]
    """<p>The <code>UnlockCode</code> value for the specified job. The <code>UnlockCode</code> value can be accessed for up to 360 days after the job has been created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobUnlockCodeResult) -> dict:
    out: dict = {}
    if "unlock_code" in value:
        out["UnlockCode"] = value["unlock_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobUnlockCodeResult:
    out: GetJobUnlockCodeResult = {}  # type: ignore[typeddict-item]
    if data.get("UnlockCode") is not None:
        out["unlock_code"] = data["UnlockCode"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetJobUnlockCodeResult) -> dict:
    out: dict = {}
    if "unlock_code" in value:
        out["UnlockCode"] = value["unlock_code"]
    return out


def deserialize_cbor(data: dict) -> GetJobUnlockCodeResult:
    out: GetJobUnlockCodeResult = {}  # type: ignore[typeddict-item]
    if data.get("UnlockCode") is not None:
        out["unlock_code"] = data["UnlockCode"]
    return out
