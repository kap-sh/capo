"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationStringFilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class RemediationStringFilterCondition(TypedDict, closed=True):
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value the string filter is comparing against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationStringFilterCondition) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> RemediationStringFilterCondition:
    out: RemediationStringFilterCondition = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
