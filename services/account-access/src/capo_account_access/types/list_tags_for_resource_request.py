"""Generated from Smithy shape ``com.amazonaws.accountaccess#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.application_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the resource to list tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
