"""Generated from Smithy shape ``com.amazonaws.accountaccess#GetApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.application_arn


class GetApplicationRequest(TypedDict, closed=True):
    application_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationRequest:
    out: GetApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
