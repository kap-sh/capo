"""Generated from Smithy shape ``com.amazonaws.accountaccess#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.application_arn


class CreateApplicationResponse(TypedDict, closed=True):
    application_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the created application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    out["applicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    else:
        raise DeserializationError("CreateApplicationResponse.application_arn required")
    return out
