"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration_identifier


class DeleteIntegrationInput(TypedDict, closed=True):
    identifier: "capo_cloudwatchomni.types.integration_identifier.IntegrationIdentifier"
    """Identifies the integration to delete — exactly one of integrationId, integrationArn, or integrationName."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteIntegrationInput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.integration_identifier

    out["identifier"] = capo_cloudwatchomni.types.integration_identifier.serialize_cbor(
        value["identifier"]
    )
    return out


def deserialize_cbor(data: dict) -> DeleteIntegrationInput:
    out: DeleteIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        import capo_cloudwatchomni.types.integration_identifier

        out["identifier"] = (
            capo_cloudwatchomni.types.integration_identifier.deserialize_cbor(
                data["identifier"]
            )
        )
    else:
        import capo_cloudwatchomni.types._unknown

        out["identifier"] = capo_cloudwatchomni.types._unknown.UnknownUnionMember("")
    return out
