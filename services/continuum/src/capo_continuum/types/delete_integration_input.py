"""Generated from Smithy shape ``com.amazonaws.continuum#DeleteIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_id


class DeleteIntegrationInput(TypedDict, closed=True):
    integration_id: "capo_continuum.types.integration_id.IntegrationId"
    """The unique identifier of the integration to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntegrationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIntegrationInput:
    out: DeleteIntegrationInput = {}  # type: ignore[typeddict-item]
    return out
