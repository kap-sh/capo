"""Generated from Smithy shape ``com.amazonaws.kinesis#HashKeyRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.hash_key


class HashKeyRange(TypedDict, closed=True):
    starting_hash_key: "capo_kinesis.types.hash_key.HashKey"
    """<p>The starting hash key of the hash key range.</p>"""
    ending_hash_key: "capo_kinesis.types.hash_key.HashKey"
    """<p>The ending hash key of the hash key range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HashKeyRange) -> dict:
    out: dict = {}
    out["StartingHashKey"] = value["starting_hash_key"]
    out["EndingHashKey"] = value["ending_hash_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HashKeyRange:
    out: HashKeyRange = {}  # type: ignore[typeddict-item]
    if data.get("StartingHashKey") is not None:
        out["starting_hash_key"] = data["StartingHashKey"]
    else:
        out["starting_hash_key"] = ""
    if data.get("EndingHashKey") is not None:
        out["ending_hash_key"] = data["EndingHashKey"]
    else:
        out["ending_hash_key"] = ""
    return out
