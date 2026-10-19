"""Generated from Smithy shape ``com.amazonaws.s3files#ExpirationDataRule``."""

from typing_extensions import TypedDict


class ExpirationDataRule(TypedDict, closed=True):
    days_after_last_access: "int"
    """<p>The number of days after last access before cached data expires from the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpirationDataRule) -> dict:
    out: dict = {}
    out["daysAfterLastAccess"] = value["days_after_last_access"]
    return out


def deserialize_json(data: dict) -> ExpirationDataRule:
    out: ExpirationDataRule = {}  # type: ignore[typeddict-item]
    if data.get("daysAfterLastAccess") is not None:
        out["days_after_last_access"] = data["daysAfterLastAccess"]
    else:
        out["days_after_last_access"] = 0
    return out
