"""Generated from Smithy shape ``com.amazonaws.rds#ModifyIntegrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.data_filter
    import capo_rds.types.integration_description
    import capo_rds.types.integration_identifier
    import capo_rds.types.integration_name


class ModifyIntegrationMessage(TypedDict, closed=True):
    integration_identifier: NotRequired[
        "capo_rds.types.integration_identifier.IntegrationIdentifier"
    ]
    """<p>The unique identifier of the integration to modify.</p>"""
    integration_name: NotRequired["capo_rds.types.integration_name.IntegrationName"]
    """<p>A new name for the integration.</p>"""
    data_filter: NotRequired["capo_rds.types.data_filter.DataFilter"]
    """<p>A new data filter for the integration. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Zero_ETL_Filtering.html">Data filtering for Aurora zero-ETL integrations with Amazon Redshift</a> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.filtering.html">Data filtering for Amazon RDS zero-ETL integrations with Amazon Redshift</a>.</p>"""
    description: NotRequired[
        "capo_rds.types.integration_description.IntegrationDescription"
    ]
    """<p>A new description for the integration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyIntegrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "integration_identifier" in value:
        pairs.append(
            (f"{key_prefix}IntegrationIdentifier", str(value["integration_identifier"]))
        )
    if "integration_name" in value:
        pairs.append((f"{key_prefix}IntegrationName", str(value["integration_name"])))
    if "data_filter" in value:
        pairs.append((f"{key_prefix}DataFilter", str(value["data_filter"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_query(el: Element) -> ModifyIntegrationMessage:
    out: ModifyIntegrationMessage = {}  # type: ignore[typeddict-item]
    child_integration_identifier = el.find("IntegrationIdentifier")
    if child_integration_identifier is not None:
        out["integration_identifier"] = str(child_integration_identifier.text or "")
    child_integration_name = el.find("IntegrationName")
    if child_integration_name is not None:
        out["integration_name"] = str(child_integration_name.text or "")
    child_data_filter = el.find("DataFilter")
    if child_data_filter is not None:
        out["data_filter"] = str(child_data_filter.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
