"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeduplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.deduplication_type


class DeduplicationConfiguration(TypedDict, closed=True):
    deduplication_type: "capo_eventbridgev2.types.deduplication_type.DeduplicationType"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeduplicationConfiguration) -> dict:
    out: dict = {}
    import capo_eventbridgev2.types.deduplication_type

    out["DeduplicationType"] = (
        capo_eventbridgev2.types.deduplication_type.serialize_cbor(
            value["deduplication_type"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> DeduplicationConfiguration:
    out: DeduplicationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DeduplicationType") is not None:
        import capo_eventbridgev2.types.deduplication_type

        out["deduplication_type"] = (
            capo_eventbridgev2.types.deduplication_type.deserialize_cbor(
                data["DeduplicationType"]
            )
        )
    else:
        import typing

        out["deduplication_type"] = typing.cast(
            "capo_eventbridgev2.types.deduplication_type.DeduplicationType", ""
        )
    return out
