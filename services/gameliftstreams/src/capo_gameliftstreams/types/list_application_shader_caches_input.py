"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListApplicationShaderCachesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier


class ListApplicationShaderCachesInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationShaderCachesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationShaderCachesInput:
    out: ListApplicationShaderCachesInput = {}  # type: ignore[typeddict-item]
    return out
