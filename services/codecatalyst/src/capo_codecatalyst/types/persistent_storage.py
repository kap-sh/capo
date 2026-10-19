"""Generated from Smithy shape ``com.amazonaws.codecatalyst#PersistentStorage``."""

from typing_extensions import TypedDict


class PersistentStorage(TypedDict, closed=True):
    size_in_gi_b: "int"
    """<p>The size of the persistent storage in gigabytes (specifically GiB).</p> <note> <p>Valid values for storage are based on memory sizes in 16GB increments. Valid values are 16, 32, and 64.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PersistentStorage) -> dict:
    out: dict = {}
    out["sizeInGiB"] = value["size_in_gi_b"]
    return out


def deserialize_json(data: dict) -> PersistentStorage:
    out: PersistentStorage = {}  # type: ignore[typeddict-item]
    if data.get("sizeInGiB") is not None:
        out["size_in_gi_b"] = data["sizeInGiB"]
    else:
        out["size_in_gi_b"] = 0
    return out
