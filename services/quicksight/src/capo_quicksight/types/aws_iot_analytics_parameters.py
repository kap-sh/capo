"""Generated from Smithy shape ``com.amazonaws.quicksight#AwsIotAnalyticsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_name


class AwsIotAnalyticsParameters(TypedDict, closed=True):
    data_set_name: "capo_quicksight.types.data_set_name.DataSetName"
    """<p>Dataset name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIotAnalyticsParameters) -> dict:
    out: dict = {}
    out["DataSetName"] = value["data_set_name"]
    return out


def deserialize_json(data: dict) -> AwsIotAnalyticsParameters:
    out: AwsIotAnalyticsParameters = {}  # type: ignore[typeddict-item]
    if data.get("DataSetName") is not None:
        out["data_set_name"] = data["DataSetName"]
    else:
        out["data_set_name"] = ""
    return out
