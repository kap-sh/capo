"""Generated from Smithy shape ``com.amazonaws.appstream#StorageConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.domain_list
    import capo_appstream.types.resource_identifier
    import capo_appstream.types.storage_connector_type


class StorageConnector(TypedDict, closed=True):
    connector_type: NotRequired[
        "capo_appstream.types.storage_connector_type.StorageConnectorType"
    ]
    """<p>The type of storage connector.</p>"""
    resource_identifier: NotRequired[
        "capo_appstream.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The ARN of the storage connector.</p>"""
    domains: NotRequired["capo_appstream.types.domain_list.DomainList"]
    """<p>The names of the domains for the account.</p>"""
    domains_require_admin_consent: NotRequired[
        "capo_appstream.types.domain_list.DomainList"
    ]
    """<p>The OneDrive for Business domains where you require admin consent when users try to link their OneDrive account to WorkSpaces Applications. The attribute can only be specified when ConnectorType=ONE_DRIVE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnector) -> dict:
    out: dict = {}
    if "connector_type" in value:
        import capo_appstream.types.storage_connector_type

        out["ConnectorType"] = (
            capo_appstream.types.storage_connector_type.serialize_aws_json_1_1(
                value["connector_type"]
            )
        )
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "domains" in value:
        import capo_appstream.types.domain_list

        out["Domains"] = capo_appstream.types.domain_list.serialize_aws_json_1_1(
            value["domains"]
        )
    if "domains_require_admin_consent" in value:
        import capo_appstream.types.domain_list

        out["DomainsRequireAdminConsent"] = (
            capo_appstream.types.domain_list.serialize_aws_json_1_1(
                value["domains_require_admin_consent"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageConnector:
    out: StorageConnector = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorType") is not None:
        import capo_appstream.types.storage_connector_type

        out["connector_type"] = (
            capo_appstream.types.storage_connector_type.deserialize_aws_json_1_1(
                data["ConnectorType"]
            )
        )
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if data.get("Domains") is not None:
        import capo_appstream.types.domain_list

        out["domains"] = capo_appstream.types.domain_list.deserialize_aws_json_1_1(
            data["Domains"]
        )
    if data.get("DomainsRequireAdminConsent") is not None:
        import capo_appstream.types.domain_list

        out["domains_require_admin_consent"] = (
            capo_appstream.types.domain_list.deserialize_aws_json_1_1(
                data["DomainsRequireAdminConsent"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StorageConnector) -> dict:
    out: dict = {}
    if "connector_type" in value:
        import capo_appstream.types.storage_connector_type

        out["ConnectorType"] = (
            capo_appstream.types.storage_connector_type.serialize_cbor(
                value["connector_type"]
            )
        )
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "domains" in value:
        import capo_appstream.types.domain_list

        out["Domains"] = capo_appstream.types.domain_list.serialize_cbor(
            value["domains"]
        )
    if "domains_require_admin_consent" in value:
        import capo_appstream.types.domain_list

        out["DomainsRequireAdminConsent"] = (
            capo_appstream.types.domain_list.serialize_cbor(
                value["domains_require_admin_consent"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StorageConnector:
    out: StorageConnector = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorType") is not None:
        import capo_appstream.types.storage_connector_type

        out["connector_type"] = (
            capo_appstream.types.storage_connector_type.deserialize_cbor(
                data["ConnectorType"]
            )
        )
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if data.get("Domains") is not None:
        import capo_appstream.types.domain_list

        out["domains"] = capo_appstream.types.domain_list.deserialize_cbor(
            data["Domains"]
        )
    if data.get("DomainsRequireAdminConsent") is not None:
        import capo_appstream.types.domain_list

        out["domains_require_admin_consent"] = (
            capo_appstream.types.domain_list.deserialize_cbor(
                data["DomainsRequireAdminConsent"]
            )
        )
    return out
