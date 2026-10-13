"""Generated from Smithy shape ``com.amazonaws.drs#DescribeReplicationConfigurationTemplatesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pagination_token
    import capo_drs.types.replication_configuration_templates


class DescribeReplicationConfigurationTemplatesResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_drs.types.replication_configuration_templates.ReplicationConfigurationTemplates"
    ]
    """<p>An array of Replication Configuration Templates.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Replication Configuration Template to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReplicationConfigurationTemplatesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_drs.types.replication_configuration_templates

        out["items"] = (
            capo_drs.types.replication_configuration_templates.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeReplicationConfigurationTemplatesResponse:
    out: DescribeReplicationConfigurationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_drs.types.replication_configuration_templates

        out["items"] = (
            capo_drs.types.replication_configuration_templates.deserialize_json(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(
    value: DescribeReplicationConfigurationTemplatesResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_drs.types.replication_configuration_templates

        out["items"] = (
            capo_drs.types.replication_configuration_templates.redact_sensitive(
                value["items"]
            )
        )
    return out
