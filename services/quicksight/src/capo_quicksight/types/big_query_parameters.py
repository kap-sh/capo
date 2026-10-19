"""Generated from Smithy shape ``com.amazonaws.quicksight#BigQueryParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_region
    import capo_quicksight.types.project_id


class BigQueryParameters(TypedDict, closed=True):
    project_id: "capo_quicksight.types.project_id.ProjectId"
    """<p>The Google Cloud Platform project ID where your datasource was created.</p>"""
    data_set_region: NotRequired["capo_quicksight.types.data_set_region.DataSetRegion"]
    """<p>The storage location where you create a Google BigQuery data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BigQueryParameters) -> dict:
    out: dict = {}
    out["ProjectId"] = value["project_id"]
    if "data_set_region" in value:
        out["DataSetRegion"] = value["data_set_region"]
    return out


def deserialize_json(data: dict) -> BigQueryParameters:
    out: BigQueryParameters = {}  # type: ignore[typeddict-item]
    if data.get("ProjectId") is not None:
        out["project_id"] = data["ProjectId"]
    else:
        out["project_id"] = ""
    if data.get("DataSetRegion") is not None:
        out["data_set_region"] = data["DataSetRegion"]
    return out
