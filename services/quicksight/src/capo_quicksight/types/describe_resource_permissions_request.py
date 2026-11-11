"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeResourcePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id


class DescribeResourcePermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account whose service role configuration you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourcePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeResourcePermissionsRequest:
    out: DescribeResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
