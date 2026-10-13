"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateDataSourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.data_source


class UpdateDataSourceResponse(TypedDict, closed=True):
    data_source: "capo_bedrock_agent.types.data_source.DataSource"
    """<p>Contains details about the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.data_source

    out["dataSource"] = capo_bedrock_agent.types.data_source.serialize_json(
        value["data_source"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataSourceResponse:
    out: UpdateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataSource") is not None:
        import capo_bedrock_agent.types.data_source

        out["data_source"] = capo_bedrock_agent.types.data_source.deserialize_json(
            data["dataSource"]
        )
    else:
        raise DeserializationError("UpdateDataSourceResponse.data_source required")
    return out


def redact_sensitive(value: UpdateDataSourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_source" in value:
        import capo_bedrock_agent.types.data_source

        out["data_source"] = capo_bedrock_agent.types.data_source.redact_sensitive(
            value["data_source"]
        )
    return out
