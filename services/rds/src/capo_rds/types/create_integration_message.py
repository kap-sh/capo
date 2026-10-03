"""Generated from Smithy shape ``com.amazonaws.rds#CreateIntegrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.arn
    import capo_rds.types.data_filter
    import capo_rds.types.encryption_context_map
    import capo_rds.types.integration_description
    import capo_rds.types.integration_name
    import capo_rds.types.source_arn
    import capo_rds.types.string
    import capo_rds.types.tag_list


class CreateIntegrationMessage(TypedDict, closed=True):
    source_arn: NotRequired["capo_rds.types.source_arn.SourceArn"]
    """<p>The Amazon Resource Name (ARN) of the database to use as the source for replication.</p>"""
    target_arn: NotRequired["capo_rds.types.arn.Arn"]
    """<p>The ARN of the Redshift data warehouse to use as the target for replication.</p>"""
    integration_name: NotRequired["capo_rds.types.integration_name.IntegrationName"]
    """<p>The name of the integration.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Key Management System (Amazon Web Services KMS) key identifier for the key to use to encrypt the integration. If you don't specify an encryption key, RDS uses a default Amazon Web Services owned key. </p>"""
    additional_encryption_context: NotRequired[
        "capo_rds.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>An optional set of non-secret key–value pairs that contains additional contextual information about the data. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context">Encryption context</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p> <p>You can only include this parameter if you specify the <code>KMSKeyId</code> parameter.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    data_filter: NotRequired["capo_rds.types.data_filter.DataFilter"]
    """<p>Data filtering options for the integration. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.filtering.html">Data filtering for Aurora zero-ETL integrations with Amazon Redshift</a> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.filtering.html">Data filtering for Amazon RDS zero-ETL integrations with Amazon Redshift</a>. </p>"""
    description: NotRequired[
        "capo_rds.types.integration_description.IntegrationDescription"
    ]
    """<p>A description of the integration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateIntegrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_arn" in value:
        pairs.append((f"{key_prefix}SourceArn", str(value["source_arn"])))
    if "target_arn" in value:
        pairs.append((f"{key_prefix}TargetArn", str(value["target_arn"])))
    if "integration_name" in value:
        pairs.append((f"{key_prefix}IntegrationName", str(value["integration_name"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KMSKeyId", str(value["kms_key_id"])))
    if "additional_encryption_context" in value:
        import capo_rds.types.encryption_context_map

        capo_rds.types.encryption_context_map.serialize_query(
            value["additional_encryption_context"],
            pairs,
            f"{key_prefix}AdditionalEncryptionContext",
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "data_filter" in value:
        pairs.append((f"{key_prefix}DataFilter", str(value["data_filter"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_query(el: Element) -> CreateIntegrationMessage:
    out: CreateIntegrationMessage = {}  # type: ignore[typeddict-item]
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    child_target_arn = el.find("TargetArn")
    if child_target_arn is not None:
        out["target_arn"] = str(child_target_arn.text or "")
    child_integration_name = el.find("IntegrationName")
    if child_integration_name is not None:
        out["integration_name"] = str(child_integration_name.text or "")
    child_kms_key_id = el.find("KMSKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_additional_encryption_context = el.find("AdditionalEncryptionContext")
    if child_additional_encryption_context is not None:
        import capo_rds.types.encryption_context_map

        out["additional_encryption_context"] = (
            capo_rds.types.encryption_context_map.deserialize_query(
                child_additional_encryption_context
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_data_filter = el.find("DataFilter")
    if child_data_filter is not None:
        out["data_filter"] = str(child_data_filter.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
