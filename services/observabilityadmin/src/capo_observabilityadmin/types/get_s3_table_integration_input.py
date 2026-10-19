"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetS3TableIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.resource_arn


class GetS3TableIntegrationInput(TypedDict, closed=True):
    arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the S3 Table integration to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetS3TableIntegrationInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetS3TableIntegrationInput:
    out: GetS3TableIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
