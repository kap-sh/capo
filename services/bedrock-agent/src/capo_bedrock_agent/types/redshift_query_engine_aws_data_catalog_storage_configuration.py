"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineAwsDataCatalogStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.aws_data_catalog_table_names


class RedshiftQueryEngineAwsDataCatalogStorageConfiguration(TypedDict, closed=True):
    table_names: (
        "capo_bedrock_agent.types.aws_data_catalog_table_names.AwsDataCatalogTableNames"
    )
    """<p>A list of names of the tables to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: RedshiftQueryEngineAwsDataCatalogStorageConfiguration,
) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.aws_data_catalog_table_names

    out["tableNames"] = (
        capo_bedrock_agent.types.aws_data_catalog_table_names.serialize_json(
            value["table_names"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> RedshiftQueryEngineAwsDataCatalogStorageConfiguration:
    out: RedshiftQueryEngineAwsDataCatalogStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("tableNames") is not None:
        import capo_bedrock_agent.types.aws_data_catalog_table_names

        out["table_names"] = (
            capo_bedrock_agent.types.aws_data_catalog_table_names.deserialize_json(
                data["tableNames"]
            )
        )
    else:
        out["table_names"] = []
    return out
