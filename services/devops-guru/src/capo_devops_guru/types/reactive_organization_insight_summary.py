"""Generated from Smithy shape ``com.amazonaws.devopsguru#ReactiveOrganizationInsightSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.aws_account_id
    import capo_devops_guru.types.insight_id
    import capo_devops_guru.types.insight_name
    import capo_devops_guru.types.insight_severity
    import capo_devops_guru.types.insight_status
    import capo_devops_guru.types.insight_time_range
    import capo_devops_guru.types.organizational_unit_id
    import capo_devops_guru.types.resource_collection
    import capo_devops_guru.types.service_collection


class ReactiveOrganizationInsightSummary(TypedDict, closed=True):
    id: NotRequired["capo_devops_guru.types.insight_id.InsightId"]
    """<p>The ID of the insight summary.</p>"""
    account_id: NotRequired["capo_devops_guru.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account. </p>"""
    organizational_unit_id: NotRequired[
        "capo_devops_guru.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The ID of the organizational unit.</p>"""
    name: NotRequired["capo_devops_guru.types.insight_name.InsightName"]
    """<p>The name of the insight summary.</p>"""
    severity: NotRequired["capo_devops_guru.types.insight_severity.InsightSeverity"]
    """<p> An array of severity values used to search for insights. For more information, see <a href="https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities">Understanding insight severities</a> in the <i>Amazon DevOps Guru User Guide</i>.</p>"""
    status: NotRequired["capo_devops_guru.types.insight_status.InsightStatus"]
    """<p> An array of status values used to search for insights. </p>"""
    insight_time_range: NotRequired[
        "capo_devops_guru.types.insight_time_range.InsightTimeRange"
    ]
    resource_collection: NotRequired[
        "capo_devops_guru.types.resource_collection.ResourceCollection"
    ]
    service_collection: NotRequired[
        "capo_devops_guru.types.service_collection.ServiceCollection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ReactiveOrganizationInsightSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "organizational_unit_id" in value:
        out["OrganizationalUnitId"] = value["organizational_unit_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "severity" in value:
        import capo_devops_guru.types.insight_severity

        out["Severity"] = capo_devops_guru.types.insight_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import capo_devops_guru.types.insight_status

        out["Status"] = capo_devops_guru.types.insight_status.serialize_json(
            value["status"]
        )
    if "insight_time_range" in value:
        import capo_devops_guru.types.insight_time_range

        out["InsightTimeRange"] = (
            capo_devops_guru.types.insight_time_range.serialize_json(
                value["insight_time_range"]
            )
        )
    if "resource_collection" in value:
        import capo_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            capo_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    if "service_collection" in value:
        import capo_devops_guru.types.service_collection

        out["ServiceCollection"] = (
            capo_devops_guru.types.service_collection.serialize_json(
                value["service_collection"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReactiveOrganizationInsightSummary:
    out: ReactiveOrganizationInsightSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("OrganizationalUnitId") is not None:
        out["organizational_unit_id"] = data["OrganizationalUnitId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Severity") is not None:
        import capo_devops_guru.types.insight_severity

        out["severity"] = capo_devops_guru.types.insight_severity.deserialize_json(
            data["Severity"]
        )
    if data.get("Status") is not None:
        import capo_devops_guru.types.insight_status

        out["status"] = capo_devops_guru.types.insight_status.deserialize_json(
            data["Status"]
        )
    if data.get("InsightTimeRange") is not None:
        import capo_devops_guru.types.insight_time_range

        out["insight_time_range"] = (
            capo_devops_guru.types.insight_time_range.deserialize_json(
                data["InsightTimeRange"]
            )
        )
    if data.get("ResourceCollection") is not None:
        import capo_devops_guru.types.resource_collection

        out["resource_collection"] = (
            capo_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if data.get("ServiceCollection") is not None:
        import capo_devops_guru.types.service_collection

        out["service_collection"] = (
            capo_devops_guru.types.service_collection.deserialize_json(
                data["ServiceCollection"]
            )
        )
    return out
