"""Generated from Smithy shape ``com.amazonaws.appsync#ElasticsearchDataSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.string


class ElasticsearchDataSourceConfig(TypedDict, closed=True):
    endpoint: "capo_appsync.types.string.String"
    """<p>The endpoint.</p>"""
    aws_region: "capo_appsync.types.string.String"
    """<p>The Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchDataSourceConfig) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    out["awsRegion"] = value["aws_region"]
    return out


def deserialize_json(data: dict) -> ElasticsearchDataSourceConfig:
    out: ElasticsearchDataSourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("awsRegion") is not None:
        out["aws_region"] = data["awsRegion"]
    else:
        out["aws_region"] = ""
    return out
