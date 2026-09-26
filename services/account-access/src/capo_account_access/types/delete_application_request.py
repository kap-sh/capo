"""Generated from Smithy shape ``com.amazonaws.accountaccess#DeleteApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.application_arn


class DeleteApplicationRequest(TypedDict, closed=True):
    application_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApplicationRequest:
    out: DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
