"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#GetTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.template_identifier


class GetTemplateInput(TypedDict, closed=True):
    template_identifier: (
        "capo_network_security_manager.types.template_identifier.TemplateIdentifier"
    )
    """<p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTemplateInput:
    out: GetTemplateInput = {}  # type: ignore[typeddict-item]
    return out
