"""Generated from Smithy shape ``com.amazonaws.amp#ScraperSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.destination
    import capo_amp.types.exporter_list
    import capo_amp.types.iam_role_arn
    import capo_amp.types.role_configuration
    import capo_amp.types.scraper_alias
    import capo_amp.types.scraper_arn
    import capo_amp.types.scraper_id
    import capo_amp.types.scraper_status
    import capo_amp.types.source
    import capo_amp.types.status_reason
    import capo_amp.types.tag_map


class ScraperSummary(TypedDict, closed=True):
    alias: NotRequired["capo_amp.types.scraper_alias.ScraperAlias"]
    """<p>(Optional) A name associated with the scraper.</p>"""
    scraper_id: "capo_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper.</p>"""
    arn: "capo_amp.types.scraper_arn.ScraperArn"
    """<p>The Amazon Resource Name (ARN) of the scraper.</p>"""
    role_arn: "capo_amp.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.</p>"""
    status: "capo_amp.types.scraper_status.ScraperStatus"
    """<p>A structure that contains the current status of the scraper.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the scraper was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The date and time that the scraper was last modified.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>(Optional) The list of tag keys and values associated with the scraper.</p>"""
    status_reason: NotRequired["capo_amp.types.status_reason.StatusReason"]
    """<p>If there is a failure, the reason for the failure.</p>"""
    source: "capo_amp.types.source.Source"
    """<p>The Amazon EKS cluster from which the scraper collects metrics.</p>"""
    destination: "capo_amp.types.destination.Destination"
    """<p>The destination where the scraper sends metrics. Valid destinations are Amazon Managed Service for Prometheus workspaces and CloudWatch datasets.</p>"""
    role_configuration: NotRequired[
        "capo_amp.types.role_configuration.RoleConfiguration"
    ]
    """<p>This structure displays information about the IAM roles used for cross-account scraping configuration.</p>"""
    exporters: NotRequired["capo_amp.types.exporter_list.ExporterList"]
    """<p>The exporter configurations for the scraper, if configured. The list contains at most one configuration for an Amazon OpenSearch Service domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScraperSummary) -> dict:
    out: dict = {}
    if "alias" in value:
        out["alias"] = value["alias"]
    out["scraperId"] = value["scraper_id"]
    out["arn"] = value["arn"]
    out["roleArn"] = value["role_arn"]
    import capo_amp.types.scraper_status

    out["status"] = capo_amp.types.scraper_status.serialize_json(value["status"])
    import capo_amp.types._prelude.timestamp

    out["createdAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_amp.types._prelude.timestamp

    out["lastModifiedAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["last_modified_at"]
    )
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_amp.types.source

    out["source"] = capo_amp.types.source.serialize_json(value["source"])
    import capo_amp.types.destination

    out["destination"] = capo_amp.types.destination.serialize_json(value["destination"])
    if "role_configuration" in value:
        import capo_amp.types.role_configuration

        out["roleConfiguration"] = capo_amp.types.role_configuration.serialize_json(
            value["role_configuration"]
        )
    if "exporters" in value:
        import capo_amp.types.exporter_list

        out["exporters"] = capo_amp.types.exporter_list.serialize_json(
            value["exporters"]
        )
    return out


def deserialize_json(data: dict) -> ScraperSummary:
    out: ScraperSummary = {}  # type: ignore[typeddict-item]
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    if data.get("scraperId") is not None:
        out["scraper_id"] = data["scraperId"]
    else:
        out["scraper_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("status") is not None:
        import capo_amp.types.scraper_status

        out["status"] = capo_amp.types.scraper_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("ScraperSummary.status required")
    if data.get("createdAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["created_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModifiedAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["last_modified_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["lastModifiedAt"]
        )
    else:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("tags") is not None:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("source") is not None:
        import capo_amp.types.source

        out["source"] = capo_amp.types.source.deserialize_json(data["source"])
    else:
        out["source"] = {"$unknown": {"name": ""}}
    if data.get("destination") is not None:
        import capo_amp.types.destination

        out["destination"] = capo_amp.types.destination.deserialize_json(
            data["destination"]
        )
    else:
        out["destination"] = {"$unknown": {"name": ""}}
    if data.get("roleConfiguration") is not None:
        import capo_amp.types.role_configuration

        out["role_configuration"] = capo_amp.types.role_configuration.deserialize_json(
            data["roleConfiguration"]
        )
    if data.get("exporters") is not None:
        import capo_amp.types.exporter_list

        out["exporters"] = capo_amp.types.exporter_list.deserialize_json(
            data["exporters"]
        )
    return out
