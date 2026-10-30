"""Generated from Smithy shape ``com.amazonaws.continuum#GetIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_id


class GetIntegrationInput(TypedDict, closed=True):
    integration_id: "capo_continuum.types.integration_id.IntegrationId"
    """The unique identifier of the integration to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntegrationInput:
    out: GetIntegrationInput = {}  # type: ignore[typeddict-item]
    return out
