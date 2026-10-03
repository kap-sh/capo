"""Generated from Smithy shape ``com.amazonaws.glue#GovernedCatalogSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name
    import capo_glue.types.s3_source_additional_options


class GovernedCatalogSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data store.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The database to read from.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The database table to read from.</p>"""
    partition_predicate: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Partitions satisfying this predicate are deleted. Files within the retention period in these partitions are not deleted. Set to <code>""</code> – empty by default.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.s3_source_additional_options.S3SourceAdditionalOptions"
    ]
    """<p>Specifies additional connection options.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GovernedCatalogSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "partition_predicate" in value:
        out["PartitionPredicate"] = value["partition_predicate"]
    if "additional_options" in value:
        import capo_glue.types.s3_source_additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.s3_source_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GovernedCatalogSource:
    out: GovernedCatalogSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GovernedCatalogSource.name required")
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("GovernedCatalogSource.database required")
    if data.get("Table") is not None:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("GovernedCatalogSource.table required")
    if data.get("PartitionPredicate") is not None:
        out["partition_predicate"] = data["PartitionPredicate"]
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.s3_source_additional_options

        out["additional_options"] = (
            capo_glue.types.s3_source_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    return out
