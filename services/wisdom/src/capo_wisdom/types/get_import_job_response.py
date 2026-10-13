"""Generated from Smithy shape ``com.amazonaws.wisdom#GetImportJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.import_job_data


class GetImportJobResponse(TypedDict, closed=True):
    import_job: NotRequired["capo_wisdom.types.import_job_data.ImportJobData"]
    """<p>The import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportJobResponse) -> dict:
    out: dict = {}
    if "import_job" in value:
        import capo_wisdom.types.import_job_data

        out["importJob"] = capo_wisdom.types.import_job_data.serialize_json(
            value["import_job"]
        )
    return out


def deserialize_json(data: dict) -> GetImportJobResponse:
    out: GetImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("importJob") is not None:
        import capo_wisdom.types.import_job_data

        out["import_job"] = capo_wisdom.types.import_job_data.deserialize_json(
            data["importJob"]
        )
    return out


def redact_sensitive(value: GetImportJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "import_job" in value:
        import capo_wisdom.types.import_job_data

        out["import_job"] = capo_wisdom.types.import_job_data.redact_sensitive(
            value["import_job"]
        )
    return out
