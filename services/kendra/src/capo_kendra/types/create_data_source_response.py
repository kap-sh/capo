"""Generated from Smithy shape ``com.amazonaws.kendra#CreateDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id


class CreateDataSourceResponse(TypedDict, closed=True):
    id: "capo_kendra.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataSourceResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataSourceResponse:
    out: CreateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
