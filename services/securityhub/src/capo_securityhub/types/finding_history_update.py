"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class FindingHistoryUpdate(TypedDict, closed=True):
    updated_field: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ASFF field that changed during the finding change event. </p>"""
    old_value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The value of the ASFF field before the finding change event. </p>"""
    new_value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The value of the ASFF field after the finding change event. To preserve storage and readability, Security Hub CSPM omits this value if <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingHistoryRecord.html"> <code>FindingHistoryRecord</code> </a> exceeds database limits. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryUpdate) -> dict:
    out: dict = {}
    if "updated_field" in value:
        out["UpdatedField"] = value["updated_field"]
    if "old_value" in value:
        out["OldValue"] = value["old_value"]
    if "new_value" in value:
        out["NewValue"] = value["new_value"]
    return out


def deserialize_json(data: dict) -> FindingHistoryUpdate:
    out: FindingHistoryUpdate = {}  # type: ignore[typeddict-item]
    if data.get("UpdatedField") is not None:
        out["updated_field"] = data["UpdatedField"]
    if data.get("OldValue") is not None:
        out["old_value"] = data["OldValue"]
    if data.get("NewValue") is not None:
        out["new_value"] = data["NewValue"]
    return out
