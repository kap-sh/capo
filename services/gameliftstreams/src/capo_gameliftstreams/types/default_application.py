"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#DefaultApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.arn
    import capo_gameliftstreams.types.id


class DefaultApplication(TypedDict, closed=True):
    id: NotRequired["capo_gameliftstreams.types.id.Id"]
    """<p>An ID that uniquely identifies the application resource. Example ID: <code>a-9ZY8X7Wv6</code>. </p>"""
    arn: NotRequired["capo_gameliftstreams.types.arn.Arn"]
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultApplication) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DefaultApplication:
    out: DefaultApplication = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
