"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ItemValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.metric_definition
    import capo_ssm_incidents.types.pager_duty_incident_detail
    import capo_ssm_incidents.types.url


class ItemValueArnMember(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"


class ItemValueUrlMember(TypedDict, closed=True):
    url: "capo_ssm_incidents.types.url.Url"


class ItemValueMetricDefinitionMember(TypedDict, closed=True):
    metricDefinition: "capo_ssm_incidents.types.metric_definition.MetricDefinition"


class ItemValuePagerDutyIncidentDetailMember(TypedDict, closed=True):
    pagerDutyIncidentDetail: (
        "capo_ssm_incidents.types.pager_duty_incident_detail.PagerDutyIncidentDetail"
    )


ItemValue: TypeAlias = (
    ItemValueArnMember
    | ItemValueUrlMember
    | ItemValueMetricDefinitionMember
    | ItemValuePagerDutyIncidentDetailMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ItemValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ItemValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "arn" in value:
        return {"arn": value["arn"]}
    elif "url" in value:
        return {"url": value["url"]}
    elif "metricDefinition" in value:
        return {"metricDefinition": value["metricDefinition"]}
    elif "pagerDutyIncidentDetail" in value:
        import capo_ssm_incidents.types.pager_duty_incident_detail

        return {
            "pagerDutyIncidentDetail": capo_ssm_incidents.types.pager_duty_incident_detail.serialize_json(
                value["pagerDutyIncidentDetail"]
            )
        }
    else:
        raise SerializationError("ItemValue: no variant present")


def deserialize_json(data: dict) -> ItemValue:
    if data.get("arn") is not None:
        return {"arn": data["arn"]}
    elif data.get("url") is not None:
        return {"url": data["url"]}
    elif data.get("metricDefinition") is not None:
        return {"metricDefinition": data["metricDefinition"]}
    elif data.get("pagerDutyIncidentDetail") is not None:
        import capo_ssm_incidents.types.pager_duty_incident_detail

        return {
            "pagerDutyIncidentDetail": capo_ssm_incidents.types.pager_duty_incident_detail.deserialize_json(
                data["pagerDutyIncidentDetail"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ItemValue: no recognized variant key")
