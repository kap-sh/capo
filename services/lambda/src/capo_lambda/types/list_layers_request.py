"""Generated from Smithy shape ``com.amazonaws.lambda#ListLayersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.architecture
    import capo_lambda.types.max_layer_list_items
    import capo_lambda.types.runtime
    import capo_lambda.types.string


class ListLayersRequest(TypedDict, closed=True):
    compatible_architecture: NotRequired["capo_lambda.types.architecture.Architecture"]
    """<p>The compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architecture</a>.</p>"""
    compatible_runtime: NotRequired["capo_lambda.types.runtime.Runtime"]
    """<p>A runtime identifier.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported">Supported runtimes</a>.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>A pagination token returned by a previous call.</p>"""
    max_items: NotRequired["capo_lambda.types.max_layer_list_items.MaxLayerListItems"]
    """<p>The maximum number of layers to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLayersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLayersRequest:
    out: ListLayersRequest = {}  # type: ignore[typeddict-item]
    return out
