"""Generated from Smithy shape ``com.amazonaws.lambda#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.pattern


class Filter(TypedDict, closed=True):
    pattern: NotRequired["capo_lambda.types.pattern.Pattern"]
    """<p> A filter pattern. For more information on the syntax of a filter pattern, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax"> Filter rule syntax</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    return out
