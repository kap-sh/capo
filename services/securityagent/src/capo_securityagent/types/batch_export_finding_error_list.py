"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchExportFindingErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.batch_export_finding_error

BatchExportFindingErrorList: TypeAlias = list[
    "capo_securityagent.types.batch_export_finding_error.BatchExportFindingError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchExportFindingErrorList) -> list:
    import capo_securityagent.types.batch_export_finding_error

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.batch_export_finding_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchExportFindingErrorList:
    import capo_securityagent.types.batch_export_finding_error

    out: BatchExportFindingErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.batch_export_finding_error.deserialize_json(item)
        )
    return out
