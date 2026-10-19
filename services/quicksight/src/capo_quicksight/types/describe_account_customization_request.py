"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAccountCustomizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.namespace


class DescribeAccountCustomizationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to describe Quick Sight customizations for.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The Quick Sight namespace that you want to describe Quick Sight customizations for.</p>"""
    resolved: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>The <code>Resolved</code> flag works with the other parameters to determine which view of Quick Sight customizations is returned. You can add this flag to your command to use the same view that Quick Sight uses to identify which customizations to apply to the console. Omit this flag, or set it to <code>no-resolved</code>, to reveal customizations that are configured at different levels. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountCustomizationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccountCustomizationRequest:
    out: DescribeAccountCustomizationRequest = {}  # type: ignore[typeddict-item]
    return out
