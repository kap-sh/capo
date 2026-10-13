"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormsSummary``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.metadata_form_summary

MetadataFormsSummary: TypeAlias = list[
    "capo_datazone.types.metadata_form_summary.MetadataFormSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormsSummary) -> list:
    import capo_datazone.types.metadata_form_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.metadata_form_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataFormsSummary:
    import capo_datazone.types.metadata_form_summary

    out: MetadataFormsSummary = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.metadata_form_summary.deserialize_json(item))
    return out


def redact_sensitive(value: MetadataFormsSummary) -> list[Any]:
    import capo_datazone.types.metadata_form_summary

    return [
        capo_datazone.types.metadata_form_summary.redact_sensitive(item)
        for item in value
    ]
