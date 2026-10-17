"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchExportFindingResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.batch_export_finding_result

BatchExportFindingResultList: TypeAlias = list[
    "capo_securityagent.types.batch_export_finding_result.BatchExportFindingResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchExportFindingResultList) -> list:
    import capo_securityagent.types.batch_export_finding_result

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.batch_export_finding_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchExportFindingResultList:
    import capo_securityagent.types.batch_export_finding_result

    out: BatchExportFindingResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.batch_export_finding_result.deserialize_json(item)
        )
    return out
