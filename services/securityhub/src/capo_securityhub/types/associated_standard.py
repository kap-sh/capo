"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociatedStandard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AssociatedStandard(TypedDict, closed=True):
    standards_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html">DescribeStandards</a> API response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedStandard) -> dict:
    out: dict = {}
    if "standards_id" in value:
        out["StandardsId"] = value["standards_id"]
    return out


def deserialize_json(data: dict) -> AssociatedStandard:
    out: AssociatedStandard = {}  # type: ignore[typeddict-item]
    if data.get("StandardsId") is not None:
        out["standards_id"] = data["StandardsId"]
    return out
