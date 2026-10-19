"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_level
    import capo_s3_control.types.config_id
    import capo_s3_control.types.exclude
    import capo_s3_control.types.include
    import capo_s3_control.types.is_enabled
    import capo_s3_control.types.storage_lens_arn
    import capo_s3_control.types.storage_lens_aws_org
    import capo_s3_control.types.storage_lens_data_export
    import capo_s3_control.types.storage_lens_expanded_prefixes_data_export
    import capo_s3_control.types.storage_lens_prefix_level_delimiter


class StorageLensConfiguration(TypedDict, closed=True):
    id: "capo_s3_control.types.config_id.ConfigId"
    """<p>A container for the Amazon S3 Storage Lens configuration ID.</p>"""
    account_level: "capo_s3_control.types.account_level.AccountLevel"
    """<p>A container for all the account-level configurations of your S3 Storage Lens configuration.</p>"""
    include: NotRequired["capo_s3_control.types.include.Include"]
    """<p>A container for what is included in this configuration. This container can only be valid if there is no <code>Exclude</code> container submitted, and it's not empty. </p>"""
    exclude: NotRequired["capo_s3_control.types.exclude.Exclude"]
    """<p>A container for what is excluded in this configuration. This container can only be valid if there is no <code>Include</code> container submitted, and it's not empty. </p>"""
    data_export: NotRequired[
        "capo_s3_control.types.storage_lens_data_export.StorageLensDataExport"
    ]
    """<p>A container to specify the properties of your S3 Storage Lens metrics export including, the destination, schema and format.</p>"""
    expanded_prefixes_data_export: NotRequired[
        "capo_s3_control.types.storage_lens_expanded_prefixes_data_export.StorageLensExpandedPrefixesDataExport"
    ]
    """<p>A container that configures your S3 Storage Lens expanded prefixes metrics report. </p>"""
    is_enabled: "capo_s3_control.types.is_enabled.IsEnabled"
    """<p>A container for whether the S3 Storage Lens configuration is enabled.</p>"""
    aws_org: NotRequired["capo_s3_control.types.storage_lens_aws_org.StorageLensAwsOrg"]
    """<p>A container for the Amazon Web Services organization for this S3 Storage Lens configuration.</p>"""
    storage_lens_arn: NotRequired[
        "capo_s3_control.types.storage_lens_arn.StorageLensArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 Storage Lens configuration. This property is read-only and follows the following format: <code> arn:aws:s3:<i>us-east-1</i>:<i>example-account-id</i>:storage-lens/<i>your-dashboard-name</i> </code> </p>"""
    prefix_delimiter: NotRequired[
        "capo_s3_control.types.storage_lens_prefix_level_delimiter.StorageLensPrefixLevelDelimiter"
    ]
    """<p>A container for all prefix delimiters that are used for object keys in this S3 Storage Lens configuration. The prefix delimiters determine how S3 Storage Lens counts prefix depth, by separating the hierarchical levels in object keys.</p> <note> <ul> <li> <p>If either a prefix delimiter or existing delimiter is undefined, Amazon S3 uses the delimiter that’s defined.</p> </li> <li> <p>If both the prefix delimiter and existing delimiter are undefined, S3 uses <code>/</code> as the default delimiter.</p> </li> <li> <p>When custom delimiters are used, both the prefix delimiter and existing delimiter must specify the same special character. Otherwise, your request results in an error.</p> </li> </ul> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: StorageLensConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_s3_control.types.account_level

    capo_s3_control.types.account_level.serialize_xml(
        value["account_level"], el, "AccountLevel"
    )
    if "include" in value:
        import capo_s3_control.types.include

        capo_s3_control.types.include.serialize_xml(value["include"], el, "Include")
    if "exclude" in value:
        import capo_s3_control.types.exclude

        capo_s3_control.types.exclude.serialize_xml(value["exclude"], el, "Exclude")
    if "data_export" in value:
        import capo_s3_control.types.storage_lens_data_export

        capo_s3_control.types.storage_lens_data_export.serialize_xml(
            value["data_export"], el, "DataExport"
        )
    if "expanded_prefixes_data_export" in value:
        import capo_s3_control.types.storage_lens_expanded_prefixes_data_export

        capo_s3_control.types.storage_lens_expanded_prefixes_data_export.serialize_xml(
            value["expanded_prefixes_data_export"], el, "ExpandedPrefixesDataExport"
        )
    SubElement(el, "IsEnabled").text = (
        "true" if value.get("is_enabled", False) else "false"
    )
    if "aws_org" in value:
        import capo_s3_control.types.storage_lens_aws_org

        capo_s3_control.types.storage_lens_aws_org.serialize_xml(
            value["aws_org"], el, "AwsOrg"
        )
    if "storage_lens_arn" in value:
        SubElement(el, "StorageLensArn").text = str(value["storage_lens_arn"])
    if "prefix_delimiter" in value:
        SubElement(el, "PrefixDelimiter").text = str(value["prefix_delimiter"])


def deserialize_xml(el: Element) -> StorageLensConfiguration:
    out: StorageLensConfiguration = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_account_level = el.find("AccountLevel")
    if child_account_level is not None:
        import capo_s3_control.types.account_level

        out["account_level"] = capo_s3_control.types.account_level.deserialize_xml(
            child_account_level
        )
    else:
        raise DeserializationError("StorageLensConfiguration.account_level required")
    child_include = el.find("Include")
    if child_include is not None:
        import capo_s3_control.types.include

        out["include"] = capo_s3_control.types.include.deserialize_xml(child_include)
    child_exclude = el.find("Exclude")
    if child_exclude is not None:
        import capo_s3_control.types.exclude

        out["exclude"] = capo_s3_control.types.exclude.deserialize_xml(child_exclude)
    child_data_export = el.find("DataExport")
    if child_data_export is not None:
        import capo_s3_control.types.storage_lens_data_export

        out["data_export"] = (
            capo_s3_control.types.storage_lens_data_export.deserialize_xml(
                child_data_export
            )
        )
    child_expanded_prefixes_data_export = el.find("ExpandedPrefixesDataExport")
    if child_expanded_prefixes_data_export is not None:
        import capo_s3_control.types.storage_lens_expanded_prefixes_data_export

        out["expanded_prefixes_data_export"] = (
            capo_s3_control.types.storage_lens_expanded_prefixes_data_export.deserialize_xml(
                child_expanded_prefixes_data_export
            )
        )
    child_is_enabled = el.find("IsEnabled")
    if child_is_enabled is not None:
        out["is_enabled"] = (child_is_enabled.text or "").lower() == "true"
    else:
        out["is_enabled"] = False
    child_aws_org = el.find("AwsOrg")
    if child_aws_org is not None:
        import capo_s3_control.types.storage_lens_aws_org

        out["aws_org"] = capo_s3_control.types.storage_lens_aws_org.deserialize_xml(
            child_aws_org
        )
    child_storage_lens_arn = el.find("StorageLensArn")
    if child_storage_lens_arn is not None:
        out["storage_lens_arn"] = str(child_storage_lens_arn.text or "")
    child_prefix_delimiter = el.find("PrefixDelimiter")
    if child_prefix_delimiter is not None:
        out["prefix_delimiter"] = str(child_prefix_delimiter.text or "")
    return out
