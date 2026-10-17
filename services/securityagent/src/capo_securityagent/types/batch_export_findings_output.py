"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchExportFindingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.batch_export_finding_error_list
    import capo_securityagent.types.batch_export_finding_result_list


class BatchExportFindingsOutput(TypedDict, closed=True):
    results: "capo_securityagent.types.batch_export_finding_result_list.BatchExportFindingResultList"
    """<p>The findings whose issue was created, each with its linked issue.</p>"""
    errors: "capo_securityagent.types.batch_export_finding_error_list.BatchExportFindingErrorList"
    """<p>The findings whose issue could not be created, each with a customer-facing reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchExportFindingsOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.batch_export_finding_result_list

    out["results"] = (
        capo_securityagent.types.batch_export_finding_result_list.serialize_json(
            value["results"]
        )
    )
    import capo_securityagent.types.batch_export_finding_error_list

    out["errors"] = (
        capo_securityagent.types.batch_export_finding_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchExportFindingsOutput:
    out: BatchExportFindingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_securityagent.types.batch_export_finding_result_list

        out["results"] = (
            capo_securityagent.types.batch_export_finding_result_list.deserialize_json(
                data["results"]
            )
        )
    else:
        raise DeserializationError("BatchExportFindingsOutput.results required")
    if data.get("errors") is not None:
        import capo_securityagent.types.batch_export_finding_error_list

        out["errors"] = (
            capo_securityagent.types.batch_export_finding_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchExportFindingsOutput.errors required")
    return out
