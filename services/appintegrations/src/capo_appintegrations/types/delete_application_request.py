"""Generated from Smithy shape ``com.amazonaws.appintegrations#DeleteApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.arn_or_uuid
    import capo_appintegrations.types.boolean


class DeleteApplicationRequest(TypedDict, closed=True):
    arn: "capo_appintegrations.types.arn_or_uuid.ArnOrUUID"
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""
    force: NotRequired["capo_appintegrations.types.boolean.Boolean"]
    """<p>Specifies whether to delete the application even if it still has application associations. If <code>true</code>, the operation removes the application and its associations. If <code>false</code> or absent, the delete fails when associations exist.</p> <important> <p>Setting this parameter to <code>true</code> permanently removes all of the application's associations. Doing so might impact other resources that rely on and reference the application. This action can't be undone.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApplicationRequest:
    out: DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
