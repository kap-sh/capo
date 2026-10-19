"""Generated from Smithy shape ``com.amazonaws.quicksight#QBusinessParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.application_arn


class QBusinessParameters(TypedDict, closed=True):
    application_arn: "capo_quicksight.types.application_arn.ApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QBusinessParameters) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> QBusinessParameters:
    out: QBusinessParameters = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    return out
