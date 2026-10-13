"""Generated from Smithy shape ``com.amazonaws.voiceid#DomainSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.arn
    import capo_voice_id.types.description
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.domain_name
    import capo_voice_id.types.domain_status
    import capo_voice_id.types.server_side_encryption_configuration
    import capo_voice_id.types.server_side_encryption_update_details
    import capo_voice_id.types.timestamp
    import capo_voice_id.types.watchlist_details


class DomainSummary(TypedDict, closed=True):
    domain_id: NotRequired["capo_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain.</p>"""
    arn: NotRequired["capo_voice_id.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the domain.</p>"""
    name: NotRequired["capo_voice_id.types.domain_name.DomainName"]
    """<p>The client-provided name for the domain.</p>"""
    description: NotRequired["capo_voice_id.types.description.Description"]
    """<p>The description of the domain.</p>"""
    domain_status: NotRequired["capo_voice_id.types.domain_status.DomainStatus"]
    """<p>The current status of the domain.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The server-side encryption configuration containing the KMS key identifier you want Voice ID to use to encrypt your data.</p>"""
    created_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the domain was created.</p>"""
    updated_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the domain was last updated.</p>"""
    server_side_encryption_update_details: NotRequired[
        "capo_voice_id.types.server_side_encryption_update_details.ServerSideEncryptionUpdateDetails"
    ]
    """<p>Details about the most recent server-side encryption configuration update. When the server-side encryption configuration is changed, dependency on the old KMS key is removed through an asynchronous process. When this update is complete, the domain's data can only be accessed using the new KMS key.</p>"""
    watchlist_details: NotRequired[
        "capo_voice_id.types.watchlist_details.WatchlistDetails"
    ]
    """<p>Provides information about <code>watchlistDetails</code> and <code>DefaultWatchlistID</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "domain_status" in value:
        out["DomainStatus"] = value["domain_status"]
    if "server_side_encryption_configuration" in value:
        import capo_voice_id.types.server_side_encryption_configuration

        out["ServerSideEncryptionConfiguration"] = (
            capo_voice_id.types.server_side_encryption_configuration.serialize_aws_json_1_0(
                value["server_side_encryption_configuration"]
            )
        )
    if "created_at" in value:
        import capo_voice_id.types.timestamp

        out["CreatedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_voice_id.types.timestamp

        out["UpdatedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    if "server_side_encryption_update_details" in value:
        import capo_voice_id.types.server_side_encryption_update_details

        out["ServerSideEncryptionUpdateDetails"] = (
            capo_voice_id.types.server_side_encryption_update_details.serialize_aws_json_1_0(
                value["server_side_encryption_update_details"]
            )
        )
    if "watchlist_details" in value:
        import capo_voice_id.types.watchlist_details

        out["WatchlistDetails"] = (
            capo_voice_id.types.watchlist_details.serialize_aws_json_1_0(
                value["watchlist_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DomainStatus") is not None:
        out["domain_status"] = data["DomainStatus"]
    if data.get("ServerSideEncryptionConfiguration") is not None:
        import capo_voice_id.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_voice_id.types.server_side_encryption_configuration.deserialize_aws_json_1_0(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_voice_id.types.timestamp

        out["created_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_voice_id.types.timestamp

        out["updated_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    if data.get("ServerSideEncryptionUpdateDetails") is not None:
        import capo_voice_id.types.server_side_encryption_update_details

        out["server_side_encryption_update_details"] = (
            capo_voice_id.types.server_side_encryption_update_details.deserialize_aws_json_1_0(
                data["ServerSideEncryptionUpdateDetails"]
            )
        )
    if data.get("WatchlistDetails") is not None:
        import capo_voice_id.types.watchlist_details

        out["watchlist_details"] = (
            capo_voice_id.types.watchlist_details.deserialize_aws_json_1_0(
                data["WatchlistDetails"]
            )
        )
    return out


def redact_sensitive(value: DomainSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
